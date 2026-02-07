class SoilAgent:
    def analyze(self, context):
        moisture = context["moisture"]

        if moisture > 60:
            return {
                "soil": "REFUSE",
                "reason": "Soil moisture sufficient"
            }
        elif moisture >= 41:
            return {
                "soil": "LIMITED",
                "reason": "Moderate soil moisture detected"
            }
        else:
            return {
                "soil": "ALLOW",
                "reason": "Soil moisture low"
            }
