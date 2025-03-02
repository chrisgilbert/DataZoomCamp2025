# Homework Week 5

# Q1

Version:
`3.5.4`

# Q2
25MB (actually 22)

# Q3
Given
```
from pyspark.sql.functions import dayofmonth
filtered = y10p.filter(dayofmonth(y10p.tpep_pickup_datetime) == '15')
filtered.count()
```
`128893`  125,567??

# Q4
Given:
```
y10p\
    .withColumn("trip_duration", \
    (to_timestamp(y10p.tpep_dropoff_datetime).cast('long') \
    - to_timestamp(y10p.tpep_pickup_datetime).cast('long'))\
    / 60 / 60)\
    .agg(max_by('trip_duration', 'trip_duration'))\
.show()
```
Answer `162 hrs`

# Q5 
Port 4040

# Q6
Given:
```
spark.sql("""
    select count(1), Zone from yellow_2024_10
    left outer join zones on (PULocationID = LocationID)
    group by Zone
    order by count(1)
""").show()
```
Answer: Governor's Island/Ellis Island/Liberty Island