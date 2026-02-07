def decide(mcp):
    if any(v["decision"] == "VETO" for v in mcp.agent_outputs.values()):
        return "REFUSE"

    decisions = [v["decision"] for v in mcp.agent_outputs.values()
                 if v["decision"] != "VETO"]

    agreement = max(decisions.count(d) for d in set(decisions)) / len(decisions)

    if agreement < 0.6:
        return "REFUSE"
    elif "WATER" in decisions:
        return "WATER"
    else:
        return "DELAY"
