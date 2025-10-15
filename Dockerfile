# Start from a Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update && \
    apt-get install -y ffmpeg build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of your app
COPY . .

# Default command (adjust according to your app)
CMD ["python", "main.py"]
