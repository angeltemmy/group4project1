# Enviornment Imports
import pandas as pd
from pathlib import Path
from sqlalchemy import Table, MetaData
from datetime import datetime


# Project Imports
from etl_project.connectors.earthquakes import EarthquakesApiClient
from etl_project.connectors.postgresql import PostgreSqlClient


def extract_earthquakes_data(
        earthquakes_client: EarthquakesApiClient,
        start_time: str,
        end_time: str,
        layer_name: str
) -> pd.DataFrame:
    """
    Utilizes the client's get_data metod to build data into dataframe 
    """
    data = []
    data.extend(
        earthquakes_client.get_data(
            start_time=start_time,
            end_time=end_time,
            layer_name=layer_name
        )
    )

    df = pd.json_normalize(data=data, meta=["symbol"])
    return df

def transform(df: pd.DataFrame, selection_list: list) -> pd.DataFrame:
    """
    Performs transformations on dataframe produced from extract_earthquakes_data() function
    """
    for item in selection_list:
        if item == 'properties.time' or item == 'properties.updated':
            df[item] = pd.to_datetime(df[item], unit='ms')

    df = df[selection_list]
    print(df.head())
    return df

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