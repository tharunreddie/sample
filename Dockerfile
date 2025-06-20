FROM python:3.10-slim
WORKDIR /app
COPY etl.py /app/etl.py
CMD ["python", "etl.py"]
