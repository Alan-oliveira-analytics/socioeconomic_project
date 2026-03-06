from datetime import datetime, timedelta
from airflow.decorators import dag, task
from pathlib import Path
import sys, os


sys.path.insert(0, '/opt/airflow/src')

from extract_data import extract_data
from transform_data import transform_data
from load_data import load_socioeconomic_data
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / 'config' / '.env'

load_dotenv(dotenv_path)


gdp_per_capta = '77823'
education_expenditures = '77819'
health_expenditures = '77820'

latin_america = '|'.join(['BR', 'AR', 'CL', 'CO', 'PE', 'VE', 'EC', 'BO', 'PY', 'UY', 'MX', 'CU', 'DO', 'HT', 'JM', 'TT', 'PA', 'CR', 'NI', 'HN', 'SV', 'GT', 'BZ', 'GY', 'SR', 'GF'])


url_gdp = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{gdp_per_capta}'
url_education = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{education_expenditures}'
url_health = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{health_expenditures}'



@dag(
    dag_id='socio_economic_project',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    },
    description='Pipeline Projeto Socioeconômico',
    schedule='0 */1 * * *',
    start_date=datetime(2026, 3, 6)
)
def economic_pipeline():
    
    @task
    def extract():
        extract_data(url_gdp, 'gdp_per_capta.json')
        extract_data(url_education, 'education_expenditures.json')
        extract_data(url_health, 'health_expenditures.json')

    @task
    def transform():
        df = transform_data()
        df.to_parquet('/opt/airflow/data/socio_economic_data.parquet', index=False)

    @task
    def load():
        import pandas as pd
        df = pd.read_parquet('/opt/airflow/data/socio_economic_data.parquet')
        load_socioeconomic_data('socioeconomic_data', df)

    extract() >> transform() >> load()


economic_pipeline()