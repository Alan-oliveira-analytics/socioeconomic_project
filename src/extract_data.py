import requests
import json
from pathlib import Path
from pprint import pprint

BASE_DIR = Path(__file__).resolve().parent.parent

gdp_per_capta = '77823'
education_expenditures = '77819'
health_expenditures = '77820'

latin_america = '|'.join(['BR', 'AR', 'CL', 'CO', 'PE', 'VE', 'EC', 'BO', 'PY', 'UY', 'MX', 'CU', 'DO', 'HT', 'JM', 'TT', 'PA', 'CR', 'NI', 'HN', 'SV', 'GT', 'BZ', 'GY', 'SR', 'GF'])


url_gdp = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{gdp_per_capta}'
url_education = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{education_expenditures}'
url_health = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{health_expenditures}'


def extract_data(url: str, output_file: str) -> list:

    response = requests.get(url)

    data = response.json()


    output_path = BASE_DIR / 'data' / output_file
    
    output_path.parent.mkdir(parents=True, exist_ok=True)



    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)


    if response.status_code == 200:
        return data
    
    elif not data:
        raise Exception('No data found for the given URL.')
    

    else:
        raise Exception(f'Error {response.status_code}: {response.text}')
    

def main():
    extract_data(url_gdp, 'gdp_per_capta.json')
    extract_data(url_education, 'education_expenditures.json')
    extract_data(url_health, 'health_expenditures.json')



if __name__ == "__main__":
    main()
    print("Data extraction completed successfully.")