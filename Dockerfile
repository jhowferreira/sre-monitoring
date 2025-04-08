FROM python:3.10

WORKDIR /app

COPY app/app.py .

RUN pip install flask prometheus_client

CMD ["python", "app.py"]

