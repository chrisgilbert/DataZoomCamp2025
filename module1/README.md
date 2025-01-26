

# Homework:

## Setup
Setup using docker compose with:
```
docker compose up -d
docker build . -t ingest-image

docker run --rm ingest-image ingest_green_taxi.py --user root --password root --host 172.17.0.1 --port 5432 --db ny_taxi

docker run --rm ingest-image ingest_zones.py --user root --password root --host 172.17.0.1 --port 5432 --db ny_taxi
```

## Questions:

1. Commands: 
```
docker run --rm -ti python:3.12.8 /bin/bash 
pip list
```
Gives: `24.3.1`

Set up with docker compose file, gives:
2. `postgres:5432` (or `db:5432`)

3. With [question3.sql](question3.sql)

`104,802; 198,924; 109,603; 27,678; 35,189`

4. With [question4.sql](question4.sql)

`2019-10-31 -- 515.89`

5. With [question5.sql](question5.sql)

`East Harlem North, East Harlem South, Morningside Heights`

6. With [question6.sql](question6.sql)

`JFK`

7. `terraform init, terraform apply -auto-approve, terraform destroy`