import pandas as pd
from flat_processing_job.database.connection import get_engine_and_session


def get_dataset() -> pd.DataFrame:
    engine, session = get_engine_and_session()
    return pd.read_sql_table("partially_parsed_flats", engine)