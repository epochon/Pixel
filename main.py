from agents.soil_agent import SoilAgent
from agents.weather_agent import WeatherAgent
from agents.water_agent import WaterAgent
from agents.crop_agent import CropAgent
from agents.ethics_agent import EthicsAgent
from data.sensor_data import get_sensor_data
class MCPContext:
    def __init__(self, sensor_data):
        self.context = sensor_data

    def __getitem__(self, key):
        return self.context.get(key)

from a2a.debate import A2AManager

def main():
    # Step 1: Get sensor & farm data
    sensor_data = get_sensor_data()

    # Step 2: Create shared context (MCP)
    context = MCPContext(sensor_data)

    # Step 3: Initialize agents
    soil_agent = SoilAgent()
    weather_agent = WeatherAgent()
    water_agent = WaterAgent()
    crop_agent = CropAgent()
    ethics_agent = EthicsAgent()

    # Step 4: A2A manager
    a2a = A2AManager(context)

    # Step 5: Run agents
    soil_result = a2a.run(soil_agent)
    weather_result = a2a.run(weather_agent)
    water_result = a2a.run(water_agent)
    crop_result = a2a.run(crop_agent)

    # Step 6: Ethics agent makes FINAL decision
    final_decision = ethics_agent.decide(
        soil_result,
        weather_result,
        water_result,
        crop_result
    )

    # Step 7: Output
    print("\nFINAL IRRIGATION DECISION")
    print(final_decision)


if __name__ == "__main__":
    main()