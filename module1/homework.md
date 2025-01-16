

Homework:

1. 24.3.1

2. postgres:5432

3. 101100	199000	109644	27686	35201

select sum(miles_lt1),
	sum(miles_1to3),
	sum(miles_3to7),
	sum(miles_7to10),
	sum(miles_gt10)
from (
SELECT
	case
	when trip_distance < 1
	then 1 else 0
	end miles_lt1,
	case
	when trip_distance > 1 and trip_distance <= 3
	then 1 else 0
	end miles_1to3,
	case when trip_distance > 3 and trip_distance<= 7
	then 1 else 0
	end miles_3to7,
	case when trip_distance > 7 and trip_distance<= 10
	then 1 else 0
	end miles_7to10,
	case when trip_distance > 10
	then 1 else 0
	end miles_gt10

FROM public.green_taxi_trips t
where extract(month from lpep_pickup_datetime) = 10
) t


4. Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.

Tip: For every day, we only care about one single trip with the longest distance.

2019-10-11
2019-10-24
2019-10-26
2019-10-31 -- this one? 515.89

SELECT max(trip_distance) , lpep_pickup_datetime::date FROM public.green_taxi_trips
where lpep_pickup_datetime::date in ('2019-10-11', '2019-10-24', '2019-10-26', '2019-10-31')
group by lpep_pickup_datetime::date


5. Which were the top pickup locations with over 13,000 in total_amount (across all trips) for 2019-10-18?

Consider only lpep_pickup_datetime when filtering by date.

East Harlem North, East Harlem South, Morningside Heights
East Harlem North, Morningside Heights
Morningside Heights, Astoria Park, East Harlem South
Bedford, East Harlem North, Astoria Park

SELECT sum(total_amount) , lpep_pickup_datetime::date FROM public.green_taxi_trips
where lpep_pickup_datetime::date in ('2019-10-18')
and total_amount > 13000
group by lpep_pickup_datetime::date


SELECT 
  sum(t.total_amount),
  z."Zone"
FROM public.green_taxi_trips t
  join taxi_zones z
  on (t."DOLocationID" = z."LocationID")
where 
  lpep_pickup_datetime::date in ('2019-10-18')
  and sum(total_amount) > 13000
group by z."Zone"
order by total_amount desc



6. JFK Airport - 87.3

SELECT max(t.tip_amount) max_tip,
z."Zone"
FROM public.green_taxi_trips t
join taxi_zones z
on (t."DOLocationID" = z."LocationID")
where extract(month from lpep_pickup_datetime) = 10
and "PULocationID" in (
   select "LocationID" 
   from taxi_zones  
   where "Zone"='East Harlem North'
)
group by z."Zone"
order by max_tip desc