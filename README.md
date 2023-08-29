# Ingestão de Dados de bandas - Wikipédia

## Resumo

Este projeto tem como objetivo ingerir dados de bandas de rock da Wikipédia, utilizando a biblioteca `requests` do Python. O objetivo é criar um dataset com as bandas e suas respectivas regiões.

## Objetivo

O objetivo deste projeto é criar um dataset de bandas de rock que possa ser usado para fins de pesquisa, análise e visualização.

# Como executar
Para executar o projeto, basta executar o arquivo `scrape_folk_metal_bands.py`:
```
python scrape_folk_metal_bands.py
```
Este comando irá executar o script Python que irá ingerir os dados da Wikipédia

# Template
O projeto foi criado usando o seguinte template:
```
├── .github
│   ├── workflows
│   │   └── schedule.yaml
|   │   └── pylint.yaml
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
O template inclui as seguintes ferramentas e arquivos:

* `.github/workflows/schedule.yaml`: Arquivo de configuração do GitHub Actions para agendar a execução do script Python.
* `.github/workflows/pylint.yaml`: Arquivo de configuração do GitHub Actions para executar o Pylint.
* `config/path.yaml`: Arquivo de configuração com os caminhos dos arquivos de entrada e saída.
* `data/intermediate/folk-metal-merged.csv`: Arquivo CSV com os dados de entrada e saída do script Python.
* `data/raw/data.json`: Arquivo JSON com os dados de entrada do script Python.
* `data/raw/folk_metal_bands.csv`: Arquivo CSV com os dados de saída do script Python.
* `logs`: Diretório para armazenar os logs de execução do script Python.
* `notebooks/01_merge_data.ipynb`: Notebook Jupyter para mesclar os dados de entrada e gerar os dados de saída.
* `notebooks/02_DataViz.ipynb`: Notebook Jupyter para visualizar os dados de saída.
* `src/__init__.py`: Arquivo para indicar que o diretório `src` é um pacote Python.
* `src/requirements.txt`: Arquivo com as dependências do projeto.
* `src/scrape_folk_metal_bands.py`: Script Python para ingerir os dados da Wikipédia.

# Autor
Este projeto foi criado por Pedro Alves
