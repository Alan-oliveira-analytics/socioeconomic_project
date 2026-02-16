import requests
import json
from pathlib import Path
from pprint import pprint

gdp_per_capta = '77823'
education_expenditures = '77819'
health_expenditures = '77820'

latin_america = '|'.join(['BR', 'AR', 'CL', 'CO', 'PE', 'VE', 'EC', 'BO', 'PY', 'UY', 'MX', 'CU', 'DO', 'HT', 'JM', 'TT', 'PA', 'CR', 'NI', 'HN', 'SV', 'GT', 'BZ', 'GY', 'SR', 'GF'])


url = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{gdp_per_capta}'


def extract_gdp(url) -> list:

    response = requests.get(url)


    output_path = 'data/gdp_per_capta.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)