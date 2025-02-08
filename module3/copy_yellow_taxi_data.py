import requests
import os


url_base = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'

for file in ['yellow_tripdata_2024-01.parquet', 
             'yellow_tripdata_2024-02.parquet', 
             'yellow_tripdata_2024-03.parquet',
             'yellow_tripdata_2024-04.parquet',
             'yellow_tripdata_2024-05.parquet',
             'yellow_tripdata_2024-06.parquet'
             ]:
    url = url_base + file
    
    with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(file, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
            
    print(f'Uploading {file} to GCS')
    os.system(f'gcloud storage cp {file} gs://chrisg-taxi-data/')

print('Data copied successfully')
