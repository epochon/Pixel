class A2AManager:
    def __init__(self, context):
        self.context = context

    def run(self, agent):
        """
        Runs an agent using shared MCP context
        """
        return agent.analyze(self.context)
