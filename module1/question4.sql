SELECT max(trip_distance) , lpep_pickup_datetime::date FROM public.green_taxi_trips
where lpep_pickup_datetime::date in ('2019-10-11', '2019-10-24', '2019-10-26', '2019-10-31')
group by lpep_pickup_datetime::date