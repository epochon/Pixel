class EthicsAgent:
    def decide(self, soil, weather, water, crop):

        if soil["soil"] == "REFUSE":
            return {
                "decision": "REFUSE IRRIGATION",
                "reason": soil["reason"]
            }

        if soil["soil"] == "LIMITED":
            return {
                "decision": "LIMITED IRRIGATION",
                "reason": soil["reason"]
            }

        return {
            "decision": "ALLOW IRRIGATION",
            "reason": soil["reason"]
        }
