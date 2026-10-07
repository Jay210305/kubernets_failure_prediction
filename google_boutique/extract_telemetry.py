import datetime
import time
from typing import Dict, List
import numpy as np
import pandas as pd
import requests

# Configuración del entorno
PROMETHEUS_URL = "http://localhost:9095"
NAMESPACE = "demo-app"
STEP = "5s"  # Intervalo de muestreo Delta_t = 5s

# 11 Microservicios estándar de Google Online Boutique
SERVICES: List[str] = [
    "frontend",
    "cartservice",
    "productcatalogservice",
    "currencyservice",
    "paymentservice",
    "shippingservice",
    "emailservice",
    "checkoutservice",
    "recommendationservice",
    "adservice",
    "redis-cart",
]

# Definición de las 5 métricas clave en PromQL
# NOTA: las llaves literales de PromQL se escapan como {{ y }} para que
# .format(service=...) sólo reemplace el placeholder {service}.
METRIC_QUERIES: Dict[str, str] = {
    "cpu_usage": (
        'sum(rate(container_cpu_usage_seconds_total{{namespace="'
        + NAMESPACE
        + '", pod=~"{service}-.*", container!=""}}[30s]))'
    ),
    "memory_usage": (
        'sum(container_memory_working_set_bytes{{namespace="'
        + NAMESPACE
        + '", pod=~"{service}-.*", container!=""}})'
    ),
    "network_rx": (
        'sum(rate(container_network_receive_bytes_total{{namespace="'
        + NAMESPACE
        + '", pod=~"{service}-.*"}}[30s]))'
    ),
    "network_tx": (
        'sum(rate(container_network_transmit_bytes_total{{namespace="'
        + NAMESPACE
        + '", pod=~"{service}-.*"}}[30s]))'
    ),
    "http_errors": (
        'sum(rate(http_requests_total{{namespace="'
        + NAMESPACE
        + '", pod=~"{service}-.*", status=~"5.."}}[30s])) or vector(0)'
    ),
}


def query_prometheus_range(
    query: str, start_ts: float, end_ts: float, step: str = STEP
) -> list:
    """Ejecuta una consulta al endpoint query_range de Prometheus."""
    url = f"{PROMETHEUS_URL}/api/v1/query_range"
    params = {"query": query, "start": start_ts, "end": end_ts, "step": step}
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "success" and data["data"]["result"]:
            return data["data"]["result"][0]["values"]
        return []
    except Exception as e:
        print(f"Error consultando PromQL [{query}]: {e}")
        return []


def extract_dataset(
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    output_filename: str = "dataset_raw",
) -> pd.DataFrame:
    """Extrae las series temporales de todos los servicios y métricas,

    alineando timestamps mediante una malla temporal común.
    """
    start_ts = start_time.timestamp()
    end_ts = end_time.timestamp()

    # Malla temporal uniforme
    time_index = pd.date_range(
        start=start_time, end=end_time, freq="5s", name="timestamp"
    )
    df_combined = pd.DataFrame(index=time_index)

    print(
        f"Iniciando extracción: {start_time} -> {end_time} ({len(time_index)} timesteps)"
    )

    for service in SERVICES:
        for metric_name, query_template in METRIC_QUERIES.items():
            column_name = f"{service}_{metric_name}"
            promql = query_template.format(service=service)

            raw_values = query_prometheus_range(
                promql, start_ts, end_ts, step=STEP
            )

            if raw_values:
                # raw_values viene en formato: [[timestamp_epoch, "valor_str"], ...]
                records = [
                    (
                        pd.to_datetime(float(ts), unit="s", utc=True),
                        float(val),
                    )
                    for ts, val in raw_values
                ]
                metric_df = pd.DataFrame(
                    records, columns=["timestamp", column_name]
                ).set_index("timestamp")
                # Eliminar zona horaria para coincidir con el índice base si es necesario
                metric_df.index = metric_df.index.tz_localize(None)

                # Unir al DataFrame principal y rellenar valores faltantes
                df_combined = df_combined.join(metric_df, how="left")
            else:
                # Si la métrica no arrojó resultados (ej. errores 5xx = 0)
                df_combined[column_name] = 0.0

    # Imputación de datos faltantes por interpolación y rellenado hacia adelante
    df_combined = df_combined.ffill().bfill().fillna(0.0)

    # Guardar en CSV y Parquet
    df_combined.to_csv(f"{output_filename}.csv")
    df_combined.to_parquet(f"{output_filename}.parquet")

    print(f"Dataset exportado exitosamente: shape={df_combined.shape}")
    return df_combined


def build_spatiotemporal_tensor(
    df: pd.DataFrame, window_size: int = 36
) -> np.ndarray:
    """Convierte el DataFrame (T, 55) en un tensor 3D de ventanas deslizantes

    con dimensiones: (N_ventanas, window_size, N_servicios, N_métricas).
    """
    n_services = len(SERVICES)
    n_metrics = len(METRIC_QUERIES)
    total_timesteps = len(df)

    # Reshape del dataframe completo a (T, 11, 5)
    data_matrix = df.to_numpy().reshape(total_timesteps, n_services, n_metrics)

    # Construcción de ventanas deslizantes
    windows = []
    for i in range(total_timesteps - window_size + 1):
        window = data_matrix[i : i + window_size, :, :]
        windows.append(window)

    tensor = np.array(windows)
    print(f"Tensor spatio-temporal generado: shape={tensor.shape}")
    return tensor


if __name__ == "__main__":
    # Ejemplo: extraer los últimos 30 minutos de telemetría
    ahora = datetime.datetime.now()
    inicio = ahora - datetime.timedelta(minutes=30)

    df_telemetria = extract_dataset(inicio, ahora, "baseline_run_01")

    # Generar tensor con ventanas de 3 minutos (36 pasos de 5 segundos)
    tensor_x = build_spatiotemporal_tensor(df_telemetria, window_size=36)