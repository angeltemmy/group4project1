# Envioroment Imports
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv
import os
from graphlib import TopologicalSorter
from pathlib import Path
import schedule
import time
import yaml

# Project Imports
from etl_project.connectors.postgresql import PostgreSqlClient
from etl_project.assets.pipeline_logging import PipelineLogging
from etl_project.assets.metadata_logging import MetaDataLogging, MetaDataLoggingStatus
from etl_project.assets.extract_load_transform import (
    extract_load,
    transform,
    SqlTransform,
)




def run_pipeline(pipeline_config: dict, postgresql_logging_client: PostgreSqlClient):
    metadata_logging = MetaDataLogging(
        pipeline_name=pipeline_config.get("name"),
        postgresql_client=postgresql_logging_client,
        config=pipeline_config.get("config"),
    )
    pipeline_logging = PipelineLogging(
        pipeline_name=pipeline_config.get("name"),
        log_folder_path=pipeline_config.get("config").get("log_folder_path"),
    )
    


    SOURCE_DATABASE_NAME = os.environ.get("SOURCE_DATABASE_NAME")
    SOURCE_SERVER_NAME = os.environ.get("SOURCE_SERVER_NAME")
    SOURCE_DB_USERNAME = os.environ.get("SOURCE_DB_USERNAME")
    SOURCE_DB_PASSWORD = os.environ.get("SOURCE_DB_PASSWORD")
    SOURCE_PORT = os.environ.get("SOURCE_PORT")
    TARGET_DATABASE_NAME = os.environ.get("TARGET_DATABASE_NAME")
    TARGET_SERVER_NAME = os.environ.get("TARGET_SERVER_NAME")
    TARGET_DB_USERNAME = os.environ.get("TARGET_DB_USERNAME")
    TARGET_DB_PASSWORD = os.environ.get("TARGET_DB_PASSWORD")
    TARGET_PORT = os.environ.get("TARGET_PORT")

    try:
        metadata_logging.log()
        pipeline_logging.logger.info("Creating source client")
        source_postgresql_client = PostgreSqlClient(
            server_name=SOURCE_SERVER_NAME,
            database_name=SOURCE_DATABASE_NAME,
            username=SOURCE_DB_USERNAME,
            password=SOURCE_DB_PASSWORD,
            port=SOURCE_PORT,
        )
        pipeline_logging.logger.info("Creating target client")
        target_postgresql_client = PostgreSqlClient(
            server_name=TARGET_SERVER_NAME,
            database_name=TARGET_DATABASE_NAME,
            username=TARGET_DB_USERNAME,
            password=TARGET_DB_PASSWORD,
            port=TARGET_PORT,
        )
        extract_template_environment = Environment(
            loader=FileSystemLoader(
                pipeline_config.get("config").get("extract_template_path")
            )
        )
        pipeline_logging.logger.info("Perform extract and load")
        extract_load(
            template_environment=extract_template_environment,
            source_postgresql_client=source_postgresql_client,
            target_postgresql_client=target_postgresql_client,
        )
        transform_template_environment = Environment(
            loader=FileSystemLoader(
                pipeline_config.get("config").get("transform_template_path")
            )
        )
        # create nodes
        transformation_load_earthquakes = SqlTransform(
            table_name="transformation_load_earthquakes",
            postgresql_client=target_postgresql_client,
            environment=extract_template_environment,
        )

        earthquake_regions = SqlTransform(
            table_name="earthquake_regions",
            postgresql_client=target_postgresql_client,
            environment=transform_template_environment,
        )

        avg_mag_region = SqlTransform(
            table_name="avg_mag_region",
            postgresql_client=target_postgresql_client,
            environment=transform_template_environment,
        )
        
        avg_max_min_mag_region = SqlTransform(
            table_name="avg_max_min_mag_region",
            postgresql_client=target_postgresql_client,
            environment=transform_template_environment,
        )

        earthquakes_for_place = SqlTransform(
            table_name="earthquakes_for_place",
            postgresql_client=target_postgresql_client,
            environment=transform_template_environment,
        )

        max_mag_region = SqlTransform(
            table_name="max_mag_region",
            postgresql_client=target_postgresql_client,
            environment=transform_template_environment,
        )

        region_more_earthquakes = SqlTransform(
            table_name="region_more_earthquakes",
            postgresql_client=target_postgresql_client,
            environment=transform_template_environment,
        )


        # create DAG
        dag = TopologicalSorter()
        dag.add(earthquake_regions, transformation_load_earthquakes)
        dag.add(avg_mag_region)
        dag.add(avg_max_min_mag_region)
        dag.add(earthquakes_for_place)
        dag.add(max_mag_region)
        dag.add(region_more_earthquakes)


        # dag.add( serving_sales_cumulative, serving_sales_month_end)
        # run transform
        pipeline_logging.logger.info("Perform transform")
        transform(dag=dag)
        pipeline_logging.logger.info("Pipeline complete")
        metadata_logging.log(
            status=MetaDataLoggingStatus.RUN_SUCCESS, logs=pipeline_logging.get_logs()
        )
        pipeline_logging.logger.handlers.clear()
    except BaseException as e:
        pipeline_logging.logger.error(f"Pipeline failed with exception {e}")
        metadata_logging.log(
            status=MetaDataLoggingStatus.RUN_FAILURE, logs=pipeline_logging.get_logs()
        )
        pipeline_logging.logger.handlers.clear()


if __name__ == "__main__":
    load_dotenv()
    LOGGING_SERVER_NAME = os.environ.get("LOGGING_SERVER_NAME")
    LOGGING_DATABASE_NAME = os.environ.get("LOGGING_DATABASE_NAME")
    LOGGING_USERNAME = os.environ.get("LOGGING_USERNAME")
    LOGGING_PASSWORD = os.environ.get("LOGGING_PASSWORD")
    LOGGING_PORT = os.environ.get("LOGGING_PORT")

    postgresql_logging_client = PostgreSqlClient(
        server_name=LOGGING_SERVER_NAME,
        database_name=LOGGING_DATABASE_NAME,
        username=LOGGING_USERNAME,
        password=LOGGING_PASSWORD,
        port=LOGGING_PORT,
    )

    # get config variables
    yaml_file_path = __file__.replace(".py", ".yaml")
    if Path(yaml_file_path).exists():
        with open(yaml_file_path) as yaml_file:
            pipeline_config = yaml.safe_load(yaml_file)
    else:
        raise Exception(
            f"Missing {yaml_file_path} file! Please create the yaml file with at least a `name` key for the pipeline name."
        )

    
    # set schedule
    schedule.every(pipeline_config.get("schedule").get("run_seconds")).seconds.do(
        run_pipeline,
        pipeline_config=pipeline_config,
        postgresql_logging_client=postgresql_logging_client,
    )

    while True:
        schedule.run_pending()
        time.sleep(pipeline_config.get("schedule").get("poll_seconds"))





