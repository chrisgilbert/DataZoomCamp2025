
docker compose up -d
docker build . -t ingest-image

docker run --rm ingest-image ingest_green_taxi.py --user root --password root --host 172.17.0.1 --port 5432 --db ny_taxi

docker run --rm ingest-image ingest_zones.py --user root --password root --host 172.17.0.1 --port 5432 --db ny_taxi