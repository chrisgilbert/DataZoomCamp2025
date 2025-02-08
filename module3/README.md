# Module 3 Homework

Setup:

Create external table with:

```
CREATE OR REPLACE EXTERNAL TABLE `kestra_taxi_data.yellow_tripdata_2024_ext`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://chrisg-taxi-data/yellow_tripdata_2024-*.parquet']
);
```

Copy to new table

```
create table kestra_taxi_data.yellow_tripdata_2024 as (
  select * from kestra_taxi_data.yellow_tripdata_2024_ext
)
```

1. SQL 
```
select count(*) 
from kestra_taxi_data.yellow_tripdata_2024
```
Gives `20332093`

2. SQL:
```
select 
count(distinct PULocationID) 
from kestra_taxi_data.yellow_tripdata_2024
```

Gives `0 MB for the External Table and 155.12MB for the Materialized Table`

3. SQL
```
select 
PULocationID,
DOLocationID
from `kestra-test-449012.kestra_taxi_data.yellow_tripdata_2024`
```
Two columns: 310.24MB
One column: 155.12MB

BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

4. SQL:
```
select 
count(*)
from `kestra-test-449012.kestra_taxi_data.yellow_tripdata_2024`
where fare_amount = 0
```
Gives: `8333`

5. Should: 
`Partition by tpep_dropoff_datetime and Cluster on VendorID`
SQL
```
create table kestra_taxi_data.yellow_tripdata_2024_partitioned
partition by date(tpep_dropoff_datetime)
cluster by VendorID
as (
  select * from kestra_taxi_data.yellow_tripdata_2024
)
```

6. SQL 
```
select distinct VendorID
from kestra_taxi_data.yellow_tripdata_2024
where cast(tpep_dropoff_datetime as date) between '2024-03-01' and '2024-03-15'
```
Gives: `310.24 MB for non-partitioned table and 26.84 MB for the partitioned table`


7. `GCP Bucket`

8. `True`

9. The query will process`0 bytes`. This is because Bigquery has metadata on the table and knows how many rows it contains from that.