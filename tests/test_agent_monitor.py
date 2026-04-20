import json
import tempfile
import unittest
from pathlib import Path

from agent_monitor import Monitor


class AgentMonitorTests(unittest.TestCase):
    def test_track_token_usage_accumulates_usage_and_cost(self):
        monitor = Monitor(agent_name="hermes")
        monitor.track_token_usage(100, 0.25)
        monitor.track_token_usage(50, 0.10)
        snapshot = monitor.snapshot()
        self.assertEqual(snapshot["token_usage"]["total_tokens"], 150)
        self.assertAlmostEqual(snapshot["token_usage"]["total_cost"], 0.35)
        self.assertEqual(snapshot["token_usage"]["calls"], 2)

    def test_track_latency_updates_count_and_average(self):
        monitor = Monitor(agent_name="hermes")
        monitor.track_latency(1.0)
        monitor.track_latency(2.0)
        snapshot = monitor.snapshot()
        self.assertEqual(snapshot["latency"]["count"], 2)
        self.assertAlmostEqual(snapshot["latency"]["avg_seconds"], 1.5)
        self.assertAlmostEqual(snapshot["latency"]["max_seconds"], 2.0)

    def test_log_writes_jsonl_event_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            monitor = Monitor(agent_name="hermes", log_dir=tmp)
            event = monitor.log("info", "Agent response generated", extra={"phase": "build"})
            events_path = Path(tmp) / "hermes.events.jsonl"
            self.assertTrue(events_path.exists())
            lines = [json.loads(line) for line in events_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0]["message"], "Agent response generated")
            self.assertEqual(lines[0]["phase"], "build")
            self.assertEqual(event["level"], "info")


if __name__ == "__main__":
    unittest.main()
