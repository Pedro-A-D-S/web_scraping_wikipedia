# Ingestão de Dados de bandas - Wikipédia
Neste projeto, foi feita a ingestão de dados de bandas de rock da Wikipédia, utilizando a biblioteca `requests` do Python. O objetivo é criar um dataset com as bandas e suas respectivas regiões.

# Como executar
Para executar o projeto, basta executar o arquivo `scrape_folk_metal_bands.py`:
```
python scrape_folk_metal_bands.py
```

# Template
O template utilizado para este projeto foi o seguinte:
```
├── .github
│   ├── workflows
│   │   └── schedule.yaml
├── config
│   └── path.yaml
├── data
│   ├── intermediate
│   │   └── folk-metal-merged.csv
│   └── raw
│       ├── data.json
│       └── folk_metal_bands.csv
├── logs
├── notebooks
│   ├── 01_merge_data.ipynb
│   └── 02_DataViz.ipynb
├── README.md
└── src
    ├── __init__.py
    ├── requirements.txt
    └── scrape_folk_metal_bands.py
```

# Autor

