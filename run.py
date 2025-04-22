# import os
# import subprocess


# if __name__ == "__main__":
#     os.system("streamlit run app.py")

from src.DataSage.ai_agent import BaseAgent, AnalystAgent


agent = BaseAgent(name="Test Agent", role="Assistant", task_description="test task")
print(agent.define())

agent_2 = AnalystAgent(name="Test Analyst", task_description="analyzes data")
print(agent_2.define())
