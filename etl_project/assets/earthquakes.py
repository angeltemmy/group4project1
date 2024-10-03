# Enviornment Imports
import pandas as pd
from pathlib import Path
from sqlalchemy import Table, MetaData



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