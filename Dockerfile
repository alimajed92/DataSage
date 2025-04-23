# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Set the environment variable to avoid Streamlit's interactive prompts
ENV STREAMLIT_HOME=/app
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run the Streamlit application
CMD ["streamlit", "run", "app.py"]