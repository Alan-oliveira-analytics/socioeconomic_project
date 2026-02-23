import pandas as pd
import numpy as np
import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

gdp_path = BASE_DIR / 'data' / 'gdp_per_capta.json'


with open (gdp_path) as f:
    data = json.load(f)

df = pd.json_normalize(data)
df.head()



country_name = df['series'][0][0]['pais']['nome']


rows = []

for item in df['series'][0]:
    print(item['pais'])
    
    for item in df['series'][0]:
        pais = item.get('pais', {})
        nome = pais.get('nome')
        pais_id = pais.get('id')
        serie = item.get('serie', [])

        for entry in serie:
            for key, value in entry.items():
                year = key
                gdp = value

                rows.append({
                    'country': nome,
                    'country_id': pais_id,
                    'year': year,
                    'gdp': gdp
                })

gdp_df = pd.DataFrame(rows)

gdp_df['year'] = pd.to_numeric(gdp_df['year'], errors='coerce').astype('Int64')
gdp_df['gdp'] = pd.to_numeric(gdp_df['gdp'], errors='coerce')

# remover linhas com valores nulos em 'gdp' ou 'year'
gdp_df = gdp_df.dropna(subset=['gdp', 'year']).reset_index(drop=True)