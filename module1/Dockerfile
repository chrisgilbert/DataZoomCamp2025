FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2
RUN pip install wget gunzip

WORKDIR /app
COPY ingest_green_taxi.py .
COPY ingest_zones.py .

ENTRYPOINT [ "python" ]

