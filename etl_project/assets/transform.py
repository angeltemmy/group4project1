import requests 
import pandas as pd


method = 'query'
url = f"https://earthquake.usgs.gov/fdsnws/event/1/{method}"

params = {
    'format':'geojson',
    'starttime': '2024-01-01',
    #'endtime':'2024-02-01',
    'limit':2000
}

response = requests.get(url,params=params)
data = response.json()['features']

df = pd.json_normalize(data)

method = 'query'
url = f"https://earthquake.usgs.gov/fdsnws/event/1/{method}"

params = {
    'format':'geojson',
    'starttime': '2024-01-01',
    #'endtime':'2024-02-01',
    'limit':2000
}

response = requests.get(url,params=params)
data = response.json()['features']

df = pd.json_normalize(data)

df.columns =  [column.replace(".", "_") for column in df.columns] 
df.columns 
df[['dt','place','d']] = df['properties_place'].str.split(',',expand=True)
df['place'] = df['place'].str.strip()
df.pop('d')
df=df.drop(["dt"],axis=1)
df=df.drop(["properties_place"],axis=1)

df=df.rename(columns={'properties_time':"timestamp", 
              'properties_updated':"timestamp_updated",
       'properties_place':"place",
         'geometry_coordinates':"coordinates", 
       'properties_title':"title",
       "properties_mag":"Magnitude",
       "properties_magType":"MagnitudeType",
       "properties_gap":"Gap",
       "properties_rms":"RMS",
       "properties_dmin":"MinDistance",
       "properties_nst":"NumStation"
       })
df['timestamp']=df['timestamp'].clip(-32768, 32767)
df['timestamp_updated']=df['timestamp_updated'].clip(-32768, 32767)
time_difference=df['time_difference']=(df['timestamp_updated']-df['timestamp']).clip(-32768, 32767)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df['timestamp_updated'] = pd.to_datetime(df['timestamp_updated'], unit='ms')

df.insert(5,'time_difference',df.pop('time_difference'))

df[['Longitude', 'Latitude', 'Depth']] = pd.DataFrame(df['coordinates'].tolist(), index=df.index)

df=df.drop(["coordinates"],axis=1)

df['id'] = df['id'].astype(str)  # Convert ID to string if needed
df['time_difference'] = df['time_difference'].fillna(0).astype(int)  # Convert time_difference to int
df['Longitude'] = df['Longitude'].astype(float)  # Convert Longitude to float
df['Latitude'] = df['Latitude'].astype(float)  # Convert Latitude to float
df['Depth'] = df['Depth'].astype(float) 

