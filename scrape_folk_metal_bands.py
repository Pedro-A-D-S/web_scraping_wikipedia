import urllib.request
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

url = 'https://en.wikipedia.org/wiki/List_of_folk_metal_bands'

with urllib.request.urlopen(url) as i:
        html = i.read()

data = pd.read_html(html)[0]
print(data)

data.to_csv('folk_metal_bands.csv')