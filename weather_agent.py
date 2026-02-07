class WeatherAgent:
    def analyze(self, context):
        rain_expected = context["rain"]
        if rain_expected:
            return {"weather": "REFUSE", "reason": "Rain expected"}
        return {"weather": "ALLOW", "reason": "No rain expected"}