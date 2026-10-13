# Capture quality report

**Measurement verdict:** fail.
**Training:** not-ready: missing event oracle/episodes, topology acceptance and historical availability.

Rows: 121; CSV/Parquet parity: True; observed-mask parity: True; hashes: True; UTC grid: True; workload overlap: True.

| Series | Required | Observed / expected | Nonzero | Distinct | Fresh coverage | Verdict / reasons |
| --- | --- | --- | --- | --- | --- | --- |
| frontend_cpu_usage | True | 102/121 | 102 | 61 | 64.5% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| frontend_memory_usage | True | 121/121 | 121 | 39 | 64.5% | fail: fresh coverage below 95% (10s maximum age) |
| frontend_network_rx | True | 112/121 | 112 | 71 | 69.4% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| frontend_network_tx | True | 112/121 | 112 | 71 | 69.4% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| frontend_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| cartservice_cpu_usage | True | 103/121 | 103 | 65 | 65.3% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| cartservice_memory_usage | True | 121/121 | 121 | 39 | 65.3% | fail: fresh coverage below 95% (10s maximum age) |
| cartservice_network_rx | True | 107/121 | 107 | 67 | 66.9% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| cartservice_network_tx | True | 107/121 | 107 | 68 | 66.9% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| cartservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| productcatalogservice_cpu_usage | True | 112/121 | 112 | 77 | 68.6% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| productcatalogservice_memory_usage | True | 121/121 | 121 | 38 | 68.6% | fail: fresh coverage below 95% (10s maximum age) |
| productcatalogservice_network_rx | True | 116/121 | 116 | 80 | 71.9% | fail: fresh coverage below 95% (10s maximum age) |
| productcatalogservice_network_tx | True | 116/121 | 116 | 78 | 71.9% | fail: fresh coverage below 95% (10s maximum age) |
| productcatalogservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| currencyservice_cpu_usage | True | 101/121 | 101 | 61 | 63.6% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| currencyservice_memory_usage | True | 121/121 | 121 | 38 | 63.6% | fail: fresh coverage below 95% (10s maximum age) |
| currencyservice_network_rx | True | 107/121 | 107 | 64 | 64.5% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| currencyservice_network_tx | True | 107/121 | 107 | 65 | 64.5% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| currencyservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| paymentservice_cpu_usage | True | 101/121 | 101 | 56 | 63.6% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| paymentservice_memory_usage | True | 121/121 | 121 | 37 | 63.6% | fail: fresh coverage below 95% (10s maximum age) |
| paymentservice_network_rx | True | 112/121 | 112 | 79 | 70.2% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| paymentservice_network_tx | True | 112/121 | 112 | 79 | 70.2% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| paymentservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| shippingservice_cpu_usage | True | 110/121 | 110 | 70 | 67.8% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| shippingservice_memory_usage | True | 121/121 | 121 | 28 | 67.8% | fail: fresh coverage below 95% (10s maximum age) |
| shippingservice_network_rx | True | 104/121 | 104 | 67 | 65.3% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| shippingservice_network_tx | True | 104/121 | 104 | 68 | 65.3% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| shippingservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| emailservice_cpu_usage | True | 106/121 | 106 | 68 | 66.1% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| emailservice_memory_usage | True | 121/121 | 121 | 17 | 66.1% | fail: fresh coverage below 95% (10s maximum age) |
| emailservice_network_rx | True | 111/121 | 111 | 76 | 67.8% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| emailservice_network_tx | True | 111/121 | 111 | 75 | 67.8% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| emailservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| checkoutservice_cpu_usage | True | 112/121 | 112 | 75 | 67.8% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| checkoutservice_memory_usage | True | 121/121 | 121 | 26 | 67.8% | fail: fresh coverage below 95% (10s maximum age) |
| checkoutservice_network_rx | True | 106/121 | 106 | 72 | 67.8% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| checkoutservice_network_tx | True | 106/121 | 106 | 70 | 67.8% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| checkoutservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| recommendationservice_cpu_usage | True | 106/121 | 106 | 62 | 65.3% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| recommendationservice_memory_usage | True | 121/121 | 121 | 30 | 65.3% | fail: fresh coverage below 95% (10s maximum age) |
| recommendationservice_network_rx | True | 104/121 | 104 | 58 | 65.3% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| recommendationservice_network_tx | True | 104/121 | 104 | 58 | 65.3% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| recommendationservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| adservice_cpu_usage | True | 113/121 | 113 | 78 | 67.8% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| adservice_memory_usage | True | 121/121 | 121 | 40 | 67.8% | fail: fresh coverage below 95% (10s maximum age) |
| adservice_network_rx | True | 108/121 | 108 | 79 | 67.8% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| adservice_network_tx | True | 108/121 | 108 | 79 | 67.8% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| adservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| redis-cart_cpu_usage | True | 0/121 | 0 | 0 | 0.0% | fail: query/source/metadata errors; coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient; unexpected query shape |
| redis-cart_memory_usage | True | 0/121 | 0 | 0 | 0.0% | fail: query/source/metadata errors; coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient; unexpected query shape |
| redis-cart_network_rx | True | 0/121 | 0 | 0 | 0.0% | fail: query/source/metadata errors; coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient; unexpected query shape |
| redis-cart_network_tx | True | 0/121 | 0 | 0 | 0.0% | fail: query/source/metadata errors; coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient; unexpected query shape |
| redis-cart_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: query/source/metadata errors; coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient; unexpected query shape |

## Limits

- Query evaluation timestamps are not scrape timestamps; source ages are reported separately.
- Retrospective receipt times do not prove historical inference availability.
- Clock synchronization and replica/network aggregation still require review.
