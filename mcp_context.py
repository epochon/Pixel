class MCPContext:
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data
        self.agent_outputs = {}
        self.debate_logs = []
        self.final_decision = None
