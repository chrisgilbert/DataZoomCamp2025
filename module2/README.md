## Homework

Q1: Check the size of the file on GCS - Gives: `128.3MB`

Q2:  Given config:
```
variables:
  file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"

...

"{{render(vars.file)}}"
```
Would make `green_tripdata_2020-04.csv`

Q3:  SQL Query:
```
with yellow_months as (
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_01` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_02` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_03` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_04` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_05` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_06` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_07` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_08` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_09` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_10` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_11` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.yellow_tripdata_2020_12` 
)
select sum(cnt) from yellow_months
```

Gives `24648499`

Q4: SQL:

```
with green_months as (
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_01` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_02` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_03` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_04` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_05` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_06` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_07` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_08` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_09` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_10` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_11` 
union all
SELECT count(*) cnt FROM `kestra_taxi_data.green_tripdata_2020_12` 
)
select sum(cnt) from green_months
```
Gives: `1734051`

Q5: SQL
```
select count(*) from kestra_taxi_data.yellow_tripdata_2021_03
```
Gives: `1925152`

Q6: Trigger section of 06_gcp_taxi_scheduled,yaml should look like this:
```
triggers:
  - id: green_schedule
    type: io.kestra.plugin.core.trigger.Schedule
    timezone: America/New_York
    cron: "0 9 1 * *"
    inputs:
      taxi: green

  - id: yellow_schedule
    type: io.kestra.plugin.core.trigger.Schedule
    timezone: America/New_York
    cron: "0 10 1 * *"
    inputs:
      taxi: yellow
```