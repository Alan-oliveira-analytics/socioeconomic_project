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


for item in df['series'][0]:
    print(item['pais'])