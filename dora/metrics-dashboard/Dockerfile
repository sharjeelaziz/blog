FROM python:3.12.4-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY dashboard.html ./templates/

EXPOSE 5000

CMD ["python", "app.py"]