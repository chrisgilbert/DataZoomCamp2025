# Module 6 - Stream Processing Homework


Q1.

Version:     v24.2.18
Git ref:     f9a22d4430
Build date:  2025-02-14T12:59:41Z
OS/Arch:     linux/arm64
Go version:  go1.23.1

Redpanda Cluster
  node-1  v24.2.18 - f9a22d443087b824803638623d6b7492ec8221f9


Q2 

redpanda@611101ef2563:/$ rpk topic create green-trips
TOPIC        STATUS
green-trips  OK

Q3

true

Q4

```
from time import time
topic_name='green-trips'

t0 = time()

csv = pandas.read_csv('green_tripdata_2019-10.csv.gz', 
    iterator=True, chunksize=1,
    usecols=[
    'lpep_pickup_datetime',
    'lpep_dropoff_datetime',
    'PULocationID',
    'DOLocationID',
    'passenger_count',
    'trip_distance',
    'tip_amount'
])


rows_sent = 0
while True: 
    try:   
        row = next(csv)

        row.lpep_pickup_datetime = pandas.to_datetime(row.lpep_pickup_datetime)
        row.lpep_dropoff_datetime = pandas.to_datetime(row.lpep_dropoff_datetime)
        row.passenger_count = pandas.to_numeric(row.passenger_count, errors='coerce').astype('Int64')

        producer.send(topic_name, value=row.to_dict())
        rows_sent += 1
        print(f"{rows_sent} rows sent")

    except StopIteration:
        print("Finished ingesting data into flink")
        break


producer.flush()
t1 = time()
took = t1 - t0
print(took)
```
1771s