FROM python:3.10

WORKDIR /app

# Copy requirements (they are directly in flask-app/)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app.py
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
