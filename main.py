# from src.extract_data import extract_data
# from src.transform_data import main as transform_data
# from src.load_data import load_socioeconomic_data

# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# gdp_per_capta = '77823'
# education_expenditures = '77819'
# health_expenditures = '77820'

# latin_america = '|'.join(['BR', 'AR', 'CL', 'CO', 'PE', 'VE', 'EC', 'BO', 'PY', 'UY', 'MX', 'CU', 'DO', 'HT', 'JM', 'TT', 'PA', 'CR', 'NI', 'HN', 'SV', 'GT', 'BZ', 'GY', 'SR', 'GF'])


# url_gdp = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{gdp_per_capta}'
# url_education = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{education_expenditures}'
# url_health = f'https://servicodados.ibge.gov.br/api/v1/paises/{latin_america}/indicadores/{health_expenditures}'


# def pipeline():
#     try:
#         extract_data(url_gdp, 'gdp_per_capta.json')
#         extract_data(url_education, 'education_expenditures.json')
#         extract_data(url_health, 'health_expenditures.json')

#         print("Data extraction completed successfully.")

#         transformed_df = transform_data()

#         print("Data transformation completed successfully.")

#         load_socioeconomic_data('socioeconomic_indicators', transformed_df)
#         print("Data loading completed successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")



# pipeline()