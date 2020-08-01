import pandas as pd


class Data(object):
    @staticmethod
    def get_raw():
        df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
        return df

    @staticmethod
    def get_available_indicators(df) -> list:
        return df['Indicator Name'].unique()


"""
# get static data example
import os
DATASETS = os.path.abspath(os.path.dirname(__file__))
df=pd.read_csv(DATASETS+'/data.csv')
"""
