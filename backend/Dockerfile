FROM python:3-slim

RUN addgroup --system webapp && adduser --system --group webapp

WORKDIR /app

COPY app.py .

USER webapp

EXPOSE 8080

CMD ["python3", "app.py"]