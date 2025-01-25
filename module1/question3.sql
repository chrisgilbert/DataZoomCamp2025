
select width_bucket(trip_distance, array[1.0000001, 3.00000000000001, 7.0000000001, 10.00000000001, 100000000]) as bucket, count(*) as count
from public.green_taxi_trips
where lpep_pickup_datetime::date between '2019-10-01' and '2019-10-31'
and lpep_dropoff_datetime::date between '2019-10-01' and '2019-10-31'
and trip_distance is not null
group by bucket