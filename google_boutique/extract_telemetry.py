"""Compatibility entry point for the auditable Phase 04 collector.

Capture bounds must be timezone-aware, and output_filename is a new directory.
Use --help for the explicit capture CLI; no baseline file is overwritten.
"""
try:
    from .telemetry_capture import (PROMETHEUS_URL, NAMESPACE, STEP, SERVICES,
        METRIC_QUERIES, query_prometheus_range, extract_dataset,
        build_spatiotemporal_tensor, main)
except ImportError:
    from telemetry_capture import (PROMETHEUS_URL, NAMESPACE, STEP, SERVICES,
        METRIC_QUERIES, query_prometheus_range, extract_dataset,
        build_spatiotemporal_tensor, main)

if __name__ == "__main__":
    main()
