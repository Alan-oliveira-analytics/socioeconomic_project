import pandas as pd
from database import get_connection, release_connection


def get_indicators():
    conn = get_connection()

    query = """
    SELECT *
    FROM socioeconomic_data
    """

    df = pd.read_sql(query, conn)

    release_connection(conn)

    return df