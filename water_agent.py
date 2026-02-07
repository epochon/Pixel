class WaterAgent:
    def __init__(self, daily_limit=100):
        self.daily_limit = daily_limit

    def analyze(self, context):
        used = context["water_used"]
        if used >= self.daily_limit:
            return {"water": "REFUSE", "reason": "Daily water limit reached"}
        return {"water": "ALLOW", "reason": "Water available"}