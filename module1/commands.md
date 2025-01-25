
docker compose up -d
docker build . -t ingest-image
docker run --rm ingest-image ingest_green_taxi.py --user kestra --password k3str4 --host 172.17.0.1 --port 5432 --db postgres-zoomcamp