FROM python:3.7-slim

EXPOSE 5678

WORKDIR /api-service

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install ./extras/opentoken-python-master.zip

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5678"]