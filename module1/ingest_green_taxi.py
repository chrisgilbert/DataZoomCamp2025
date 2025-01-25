#!/usr/bin/env python
# coding: utf-8

import os
import argparse

from time import time

import pandas as pd
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = 'green_taxi_trips'
    
    file_list = ['green_tripdata_2019-10.csv.gz']
    for file_name in file_list:
      url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/{file_name}'
      os.system(f"wget {url} -O {file_name}")
      os.system(f"gunzip {file_name}")

    csv_list= ['green_tripdata_2019-10.csv']

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    csv = csv_list[0]
    df_iter = pd.read_csv(csv, iterator=True, chunksize=100000)
    df = next(df_iter)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    for csv in csv_list:
      df_iter = pd.read_csv(csv, iterator=True, chunksize=100000)
      df = next(df_iter)
      df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
      df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
      df.to_sql(name=table_name, con=engine, if_exists='append')

      while True: 

          try:
              t_start = time()
              
              df = next(df_iter)

              df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
              df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

              df.to_sql(name=table_name, con=engine, if_exists='append')

              t_end = time()

              print('inserted another chunk, took %.3f second' % (t_end - t_start))

          except StopIteration:
              print("Finished ingesting data into the postgres database")
              break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')

    args = parser.parse_args()

    main(args)
