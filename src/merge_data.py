import pandas as pd
import yaml

class DataLoader:
    
    def __init__(self, config_path: str):
        self.config_path = config_path
    
    def open_yaml(yaml_file: str) -> dict:
        '''
        Opens a yaml file and return a dictionary
        
        Args:
            yaml_file (str): path to yaml file
        
        Returns:
            dict: dictionary of yaml file
        '''
        with open(yaml_file) as file:
            config = yaml.safe_load(file)
        return config

    def get_dataframes(self) -> tuple:
        '''
        Read in a json file and a csv file and return two dataframes
        
        Returns:
            tuple: two dataframes
        '''
        continents = pd.read_json(self.config['path']['continent'])
        bands = pd.read_csv(self.config['path']['folk-metal'])
        return continents, bands

    def merge_dataframes(self, continents: pd.DataFrame, bands: pd.DataFrame) -> pd.DataFrame:
        '''
        Merge two dataframes
        
        Args:
            continents (pd.DataFrame): dataframe of continents
            bands (pd.DataFrame): dataframe of bands
        
        Returns:
            pd.DataFrame: merged dataframe
        '''
        merged = pd.merge(right = continents, left = bands, 
                        how = 'inner', right_on = 'country',
                        left_on = 'Country')
        return merged

    def drop_and_rename(self, df: pd.DataFrame, drop_col: str, rename_col: str) -> pd.DataFrame:
        '''
        Drop a column and rename another column
        
        Args:
            df (pd.DataFrame): dataframe
            drop_col (str): column to drop
            rename_col (str): column to rename
        
        Returns:
            pd.DataFrame: dataframe with dropped and renamed columns
        '''
        df.drop(columns = drop_col, inplace = True)
        df.rename(columns = {rename_col: 'Continent'}, inplace = True)
        
        return df

    # Create a function to save the data
    def save_data(self, df: pd.DataFrame) -> None:
        '''
        Save dataframe to a csv file
        
        Args:
            df (pd.DataFrame): dataframe
        
        Returns:
            None
        '''
        df.to_csv(self.config['df']['save'], index = False)
        
        return None