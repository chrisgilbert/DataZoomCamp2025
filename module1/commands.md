
python ingest_green_taxi_data.py --user root --password root --host localhost --port 5432 --db  ny_taxi --table_name green_taxi_trips --url https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz


python ingest_zones.py --user root --password root --host localhost --port 5432 --db  ny_taxi
python ingest_green_taxi.py --user root --password root --host localhost --port 5432 --db  ny_taxi