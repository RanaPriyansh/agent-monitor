# Agent Monitor

[![GitHub](https://img.shields.io/badge/GitHub-000000?logo=github)](https://github.com/RanaPriyansh/agent-monitor)
[![License](https://img.shields.io/github/license/RanaPriyansh/agent-monitor)](https://github.com/RanaPriyansh/agent-monitor/blob/main/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/RanaPriyansh/agent-monitor)](https://github.com/RanaPriyansh/agent-monitor/commits/main)

Structured telemetry and JSONL event logging for agent systems.

## What works now

- Track token usage totals, cost, and call counts
- Track latency count, average, and max
- Emit structured JSONL events per agent
- Snapshot current metrics for dashboards or APIs

## Quick start

```bash
cd /root/git-repos/agent-monitor
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Programmatic usage:

```python
from agent_monitor import Monitor

monitor = Monitor(agent_name="hermes")
monitor.track_token_usage(100, 0.15)
monitor.track_latency(1.23)
monitor.log("info", "agent run completed", extra={"phase": "build"})
print(monitor.snapshot())
```

Events are written to:

```bash
logs/<agent>.events.jsonl
```

## Why this matters

Interesting agent infrastructure is not just models or tools. It is observability.

Without telemetry you cannot:
- understand cost
- understand performance drift
- see failure patterns
- build credible portfolio dashboards

This repo is now the seed crystal for the monitoring layer of the agent internet stack.

## Validation

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## License

MIT
