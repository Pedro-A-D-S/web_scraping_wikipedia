import urllib.request
import pandas as pd
import yaml

with open('../config/path.yaml', 'r') as f:
    config = yaml.safe_load(f)

def get_data(url: str, data_path: str) -> pd.DataFrame:
    '''
    Scrapes data from a url and saves it to a csv file

    Parameters:
        url (str): The url to scrape
        data_path (str): The path to save the csv file
    returns:
        None
    '''
    with urllib.request.urlopen(url) as i:
            html = i.read()
    data = pd.read_html(html)[0]
    data.to_csv(data_path)
    return None

if __name__ == '__main__':
    
    url = config['scrape']['url']
    data_path = config['scrape']['save']
    get_data(url, data_path)