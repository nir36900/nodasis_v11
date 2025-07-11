# NODASIS v11 Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "frontend/dashboard_app.py", "--server.port=8501", "--server.address=0.0.0.0"]