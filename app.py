import streamlit as st
import pandas as pd
from src.DataSage.ai_agent import AnalystAgent
from src.DataSage.ollama_handlers import ollama_llm_api
from src.DataSage.config import Config
import os

# Sample DataFrame
data = {
    "city": ["Tokyo", "New York", "London"],
    "population": [37000000, 18000000, 9000000],
}
df = pd.DataFrame(data)

llm = ollama_llm_api(model_name="llama3.1:8b", base_url=Config.OLLAMA_API)

# Create the agent
agent = AnalystAgent(
    llm=llm,
    name="DataBot",
    task_description="analyzes pandas dataframes and provides insights",
)

# Streamlit UI
st.title("📊 Data Analyst Agent")
st.write("Ask a question about the dataset:")


def file_selector(folder_path="."):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select a file", filenames)
    return os.path.join(folder_path, selected_filename)


filename = file_selector()
st.write("You selected `%s`" % filename)

user_query = st.text_input(
    "Your question", placeholder="e.g. What is the city with the highest population?"
)

if user_query:
    with st.spinner("Analyzing..."):
        response = agent.analyze_dataframes(df, user_query)
        st.markdown("### 🔍 Answer")
        st.write(response.response)  # .response if you're using llama-index
