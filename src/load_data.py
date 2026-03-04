from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd



BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / 'config' / '.env'

load_dotenv(dotenv_path)

user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")

host = "host.docker.internal"

def get_engine(): # creating the database engine using the credentials from the .env file
    return create_engine(
        f"postgresql+psycopg2://{user}:{quote_plus(password)}@{host}:5432/{database}"
    )

engine = get_engine()


def load_socioeconomic_data(table_name: str, df: pd.DataFrame):
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='append',
        index=False
    )


    df_check = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
    print(f"Data loaded into {table_name} successfully. Number of records: {len(df_check)}")



