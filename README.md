# Pixel
# 🌱 Smart Irrigation System  
### EpochOn 2.0 Submission

## 📌 Project Overview
The Smart Irrigation System is an agent-based intelligent irrigation solution designed to optimize water usage in agriculture.  
The system automatically decides whether to **allow**, **limit**, or **refuse irrigation** based on soil moisture and environmental conditions, with a strong focus on **water conservation and sustainability**.

This project follows an **agentic architecture** where independent agents collaborate to make ethical and data-driven decisions.

---

## 🎯 Problem Statement
Traditional irrigation systems operate on fixed schedules without considering real-time soil and environmental conditions. This often leads to **water wastage**, **over-irrigation**, and **crop damage**.

The goal of this project is to build an intelligent system that can:
- Refuse unnecessary watering  
- Limit irrigation under moderate conditions  
- Allow irrigation only when crops genuinely need water  

---

## 🧠 Agentic Architecture
The system uses a **multi-agent approach** coordinated through shared context and structured communication.

### Agents Used:
- **Soil Agent** – Analyzes soil moisture levels
- **Weather Agent** – Evaluates rain conditions
- **Crop Agent** – Considers crop-specific water needs
- **Ethics Agent** – Makes the final sustainable decision
- **A2A Manager** – Handles agent-to-agent coordination
- **MCP (Model Context Protocol)** – Shared context for all agents

---

## ⚙️ Decision Logic
The irrigation decision is based on soil moisture levels:

| Soil Moisture (%) | Decision Output |
|------------------|----------------|
| 0 – 40           | ALLOW IRRIGATION |
| 41 – 60          | LIMITED IRRIGATION |
| > 60             | REFUSE IRRIGATION |

This ensures optimal water usage while protecting crop health.

---

## 🛠 Technology Stack
- **Python** – Core backend logic (rule-based, no LLM)
- **HTML, CSS, JavaScript** – User Interface
- **Agent-Based Architecture**
- **No Machine Learning / No LLMs**

---

## ▶️ How to Run the Project

### 1️⃣ Run Backend Logic
```bash
python main.py
