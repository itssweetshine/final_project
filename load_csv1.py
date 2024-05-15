import io
import pandas as pd
import requests
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(**kwargs) -> DataFrame:
    urls = [
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2023-12-06T13-24-23Z-2023-03-31-organogram-junior.csv',
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-department-for-levelling-up-housing-and-communities/resources/2023-12-18T15-08-44Z-2023-06-30-organogram-junior.csv',
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2023-12-04T13-32-10Z-2022-03-31-organogram-junior.csv',
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2023-12-04T11-19-54Z-2022-09-30-organogram-junior.csv',
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-department-for-communities-and-local-government/resources/2023-04-17T13-10-20Z-2022-12-31-organogram-junior.csv',
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-department-for-communities-and-local-government/resources/2022-09-26T16-48-50Z-2022-06-30-organogram-junior.csv',
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2021-07-22T14-40-16Z-2021-03-31-organogram-junior.csv',
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2022-04-04T13-43-11Z-2021-09-30-organogram-junior.csv',
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-department-for-communities-and-local-government/resources/2022-02-01T12-29-33Z-2021-12-31-organogram-junior.csv',
        'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2021-03-26T13-52-24Z-2020-03-31-organogram-junior.csv'

    ]
        
    dataframes = []
    for url in urls:
        try:
            df = pd.read_csv(url)
            date_part = url.split('/')[-1]  
            date = date_part.split('Z-')[-1].split('-organogram-junior.csv')[0]  
            df['date'] = pd.to_datetime(date, format='%Y-%m-%d')  
            dataframes.append(df)
        except Exception as e:
            print(f"Error loading data from {url}: {e}")


    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    else:
        return pd.DataFrame()  