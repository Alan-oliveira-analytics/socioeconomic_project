import pandas as pd
import numpy as np
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


gdp_path = BASE_DIR / 'data' / 'gdp_per_capta.json'
education_path = BASE_DIR / 'data' / 'education_expenditures.json'
health_path = BASE_DIR / 'data' / 'health_expenditures.json'


def normalize_data(path: Path) -> pd.DataFrame:
    with open(path) as f:
        data = json.load(f)
    return pd.json_normalize(data)


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for item in df['series'][0]:
        country = item.get('pais', {})
        name = country.get('nome')
        country_id = country.get('id')
        serie = item.get('serie', [])
        for entry in serie:
            for year, gdp in entry.items():
                rows.append({
                    'country': name,
                    'country_id': country_id,
                    'year': year,
                    'indicator': gdp
                })

    df = pd.DataFrame(rows)

    df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
    df['indicator'] = pd.to_numeric(df['indicator'], errors='coerce')

    df = df.dropna(subset=['indicator', 'year']).reset_index(drop=True)


    return df


def main() -> pd.DataFrame:
    education_df = transform_data(normalize_data(education_path))
    gdp_df = transform_data(normalize_data(gdp_path))
    health_df = transform_data(normalize_data(health_path))

    education_df = education_df.rename(columns={'indicator': 'public_education_expenditure'})
    health_df = health_df.rename(columns={'indicator': 'public_health_expenditure'})
    gdp_df = gdp_df.rename(columns={'indicator': 'gdp_per_capita'})

    final_df = pd.merge(gdp_df, education_df, on=['country', 'country_id', 'year'], how='outer')
    final_df = pd.merge(final_df, health_df, on=['country', 'country_id', 'year'], how='outer')

    metric_cols = ['gdp_per_capita', 'public_education_expenditure', 'public_health_expenditure']
    final_df = final_df.dropna(subset=metric_cols).reset_index(drop=True)

    return final_df



if __name__ == "__main__":
    df = main()
