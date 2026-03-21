# Thielon Agent Monitor

[![GitHub](https://img.shields.io/badge/GitHub-000000?logo=github)](https://github.com/thielon-apps/thielon-agent-monitor)
[![License](https://img.shields.io/github/license/thielon-apps/thielon-agent-monitor)](https://github.com/thielon-apps/thielon-agent-monitor/blob/main/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/thielon-apps/thielon-agent-monitor)](https://github.com/thielon-apps/thielon-agent-monitor/commits/main)

Observability for AI agents: metrics, logs, traces, cost tracking, performance dashboards.

## Features

- **Metrics**: Token usage, latency, error rates, throughput
- **Logs**: Structured logging with agent context
- **Traces**: Distributed tracing across tool calls
- **Cost Tracking**: Real-time API cost accumulation
- **Dashboard**: Streamlit-based real-time UI
- **Alerts**: Threshold-based notifications (Slack, email)

## Quick Start

```python
from thielon_monitor import Monitor

monitor = Monitor(agent_name="hermes")
monitor.track_token_usage(100, 0.0015)  # tokens, cost
monitor.track_latency(1.23)  # seconds
monitor.log("info", "Agent response generated")
```

Run dashboard:
```bash
streamlit run dashboard.py
```

## Install

```bash
pip install thielon-agent-monitor
```

## Why

You can't improve what you don't measure. This monitor gives you:
- Visibility into agent performance
- Cost control (see bills before they surprise you)
- Debugging capability (trace execution paths)
- Alerting on anomalies

## License

MIT
