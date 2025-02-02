# Module 3 Homework

Setup:

Create external table with:

```
CREATE OR REPLACE EXTERNAL TABLE `kestra_taxi_data.green_tripdata_2022_ext`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://chrisg-taxi-data/green_tripdata_2022-*.parquet']
);
```

Copy to new table

```
create table kestra_taxi_data.green_tripdata_2022 as (
  select * from kestra_taxi_data.green_tripdata_2022_ext
)
```

1. SQL 
```
select count(*) 
from kestra_taxi_data.green_tripdata_2022
```
Gives `840402`

2. SQL:
```
select 
count(distinct PULocationID) 
from kestra_taxi_data.green_tripdata_2022
```

Gives `0 MB for the External Table and 6.41MB for the Materialized Table`

3. SQL
```
select 
count(1)
from `kestra-test-449012.kestra_taxi_data.green_tripdata_2022`
where fare_amount = 0
```

Gives: `1622`

4. Should: 
`Partition by lpep_pickup_datetime Cluster on PUlocationID`
SQL
```
create table kestra_taxi_data.green_tripdata_2022_partitioned
partition by date(lpep_pickup_datetime)
cluster by PUlocationID
as (
  select * from kestra_taxi_data.green_tripdata_2022
)
```

5. SQL 
```
select distinct PULocationID
from kestra_taxi_data.green_tripdata_2022
where cast(lpep_pickup_datetime as date) between '2022-06-01' and '2022-06-30'
```
Gives: `12.82 MB for non-partitioned table and 1.12 MB for the partitioned table`


6. `GCP Bucket`

7. `True`

8. The query will process`0 bytes`. This is because Bigquery has metadata on the table and knows how many rows it contains from that.