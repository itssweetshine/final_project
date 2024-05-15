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
    """
    Template for loading data from API
    """
    url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2021-07-22T14-40-16Z-2021-03-31-organogram-junior.csv'
        
    return pd.read_csv(url)


@test
def test_output(df) -> None:
    """
    Template code for testing the output of the block.
    Ensures that each DataFrame in the list is not None and is not empty.
    """
    assert df is not None, 'The output list is undefined'
