FROM python:3.10-slim

WORKDIR /app
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "-u", "app.py"]