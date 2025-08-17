FROM python:3.12

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY src /app

RUN ls -la

RUN pwd

EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]