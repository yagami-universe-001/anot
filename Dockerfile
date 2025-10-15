FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y ffmpeg build-essential &&             pip install --upgrade pip && pip install -r requirements.txt &&             apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app
RUN mkdir -p /app/downloads /app/static

CMD ["python", "main.py"]
