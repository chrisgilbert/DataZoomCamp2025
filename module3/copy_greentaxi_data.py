import requests
import os


url_base = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'

for file in ['green_tripdata_2022-01.parquet', 
             'green_tripdata_2022-02.parquet', 
             'green_tripdata_2022-03.parquet',
             'green_tripdata_2022-04.parquet',
             'green_tripdata_2022-05.parquet',
             'green_tripdata_2022-06.parquet',
             'green_tripdata_2022-07.parquet',
             'green_tripdata_2022-08.parquet',
             'green_tripdata_2022-09.parquet',
             'green_tripdata_2022-10.parquet',
             'green_tripdata_2022-11.parquet',
             'green_tripdata_2022-12.parquet']:
    url = url_base + file
    
    with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(file, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
            
    print(f'Uploading {file} to GCS')
    os.system(f'gcloud storage cp {file} gs://chrisg-taxi-data/')

print('Data copied successfully')
