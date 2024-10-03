import pandas as pd
from etl_project.connectors.earthquakes import EarthquakesApiClient
from pathlib import Path
from sqlalchemy import Table, MetaData
from etl_project.connectors.postgresql import PostgreSqlClient
from datetime import datetime, timezone, timedelta



def extract_earthquakes_data(
    earthquakes_client: EarthquakesApiClient,
    start_time: str,
    end_time: str,
    #layer_name: str
) -> pd.DataFrame:
    """
    Perform extraction using a filepath which contains a list of cities.
    """

    data = []
    #for dates in _generate_datetime_ranges(start_date=start_date, end_date=end_date):
    data.extend(
            earthquakes_client.get_data(
                start_time=start_time,
                end_time=end_time,
                #layer_name=layer_name
            )
        )

    df = pd.json_normalize(data=data, meta=["symbol"])
    return df


"""Performs transformation on dataframe produced from extract() function."""

def transform(df: pd.DataFrame, df_exchange_codes: pd.DataFrame) -> pd.DataFrame:
    """Performs transformation on dataframe produced from extract() function."""
    df =df[['type','id','properties.mag','properties.time','properties.updated','geometry.type',
                             'properties.magType','properties.gap','properties.rms','properties.dmin','properties.nst',
                             'geometry.coordinates','properties.place','geometry.type','properties.title']]

    """Performs column rename on dataframe produced from extract() function."""

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
    df['id'] = df['id'].astype(str)  # Convert ID to string if needed

def load(
    df: pd.DataFrame,
    postgresql_client: PostgreSqlClient,
    table: Table,
    metadata: MetaData,
    load_method: str = "overwrite",
) -> None:
    """
    Load dataframe to a database.

    Args:
        df: dataframe to load
        postgresql_client: postgresql client
        table: sqlalchemy table
        metadata: sqlalchemy metadata
        load_method: supports one of: [insert, upsert, overwrite]
    """
    if load_method == "insert":
        postgresql_client.insert(
            data=df.to_dict(orient="records"), table=table, metadata=metadata
        )
    elif load_method == "upsert":
        postgresql_client.upsert(
            data=df.to_dict(orient="records"), table=table, metadata=metadata
        )
    elif load_method == "overwrite":
        postgresql_client.overwrite(
            data=df.to_dict(orient="records"), table=table, metadata=metadata
        )
    else:
        raise Exception(
            "Please specify a correct load method: [insert, upsert, overwrite]"
        )
