class Monitor:
    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.metrics = {}
    def track_token_usage(self, tokens, cost):
        pass
    def track_latency(self, seconds):
        pass
    def log(self, level, message):
        pass
