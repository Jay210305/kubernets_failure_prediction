# Capture quality report

**Measurement verdict:** fail.
**Training:** not-ready: missing event oracle/episodes, topology acceptance and historical availability.

Rows: 121; CSV/Parquet parity: True; observed-mask parity: True; hashes: True; UTC grid: True; workload overlap: True.

| Series | Required | Observed / expected | Nonzero | Distinct | Fresh coverage | Verdict / reasons |
| --- | --- | --- | --- | --- | --- | --- |
| frontend_cpu_usage | True | 102/121 | 102 | 61 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| frontend_memory_usage | True | 121/121 | 121 | 39 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| frontend_network_rx | True | 112/121 | 112 | 71 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| frontend_network_tx | True | 112/121 | 112 | 71 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| frontend_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| cartservice_cpu_usage | True | 103/121 | 103 | 65 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| cartservice_memory_usage | True | 121/121 | 121 | 39 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| cartservice_network_rx | True | 107/121 | 107 | 67 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| cartservice_network_tx | True | 107/121 | 107 | 68 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| cartservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| productcatalogservice_cpu_usage | True | 112/121 | 112 | 77 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| productcatalogservice_memory_usage | True | 121/121 | 121 | 38 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| productcatalogservice_network_rx | True | 116/121 | 116 | 80 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| productcatalogservice_network_tx | True | 116/121 | 116 | 78 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| productcatalogservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| currencyservice_cpu_usage | True | 101/121 | 101 | 61 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| currencyservice_memory_usage | True | 121/121 | 121 | 38 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| currencyservice_network_rx | True | 107/121 | 107 | 64 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| currencyservice_network_tx | True | 107/121 | 107 | 65 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| currencyservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| paymentservice_cpu_usage | True | 101/121 | 101 | 56 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| paymentservice_memory_usage | True | 121/121 | 121 | 37 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| paymentservice_network_rx | True | 112/121 | 112 | 79 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| paymentservice_network_tx | True | 112/121 | 112 | 79 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| paymentservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| shippingservice_cpu_usage | True | 110/121 | 110 | 70 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| shippingservice_memory_usage | True | 121/121 | 121 | 28 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| shippingservice_network_rx | True | 104/121 | 104 | 67 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| shippingservice_network_tx | True | 104/121 | 104 | 68 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| shippingservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| emailservice_cpu_usage | True | 106/121 | 106 | 68 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| emailservice_memory_usage | True | 121/121 | 121 | 17 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| emailservice_network_rx | True | 111/121 | 111 | 76 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| emailservice_network_tx | True | 111/121 | 111 | 75 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| emailservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| checkoutservice_cpu_usage | True | 112/121 | 112 | 75 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| checkoutservice_memory_usage | True | 121/121 | 121 | 26 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| checkoutservice_network_rx | True | 106/121 | 106 | 72 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| checkoutservice_network_tx | True | 106/121 | 106 | 70 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| checkoutservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| recommendationservice_cpu_usage | True | 106/121 | 106 | 62 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| recommendationservice_memory_usage | True | 121/121 | 121 | 30 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| recommendationservice_network_rx | True | 104/121 | 104 | 58 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| recommendationservice_network_tx | True | 104/121 | 104 | 58 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| recommendationservice_http_errors | False | 0/121 | 0 | 0 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age); no observed nonzero measurement; constant series; workload evidence insufficient |
| adservice_cpu_usage | True | 113/121 | 113 | 78 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| adservice_memory_usage | True | 121/121 | 121 | 40 | 0.0% | fail: fresh coverage below 95% (10s maximum age) |
| adservice_network_rx | True | 108/121 | 108 | 79 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
| adservice_network_tx | True | 108/121 | 108 | 79 | 0.0% | fail: coverage below 95%; fresh coverage below 95% (10s maximum age) |
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
