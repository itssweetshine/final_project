import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    #url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2023-12-06T13-24-23Z-2023-03-31-organogram-junior.csv'
    #url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-department-for-levelling-up-housing-and-communities/resources/2023-12-18T15-08-44Z-2023-06-30-organogram-junior.csv'
    #url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2023-12-04T13-32-10Z-2022-03-31-organogram-junior.csv'
    #url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2023-12-04T11-19-54Z-2022-09-30-organogram-junior.csv'
    #url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-department-for-communities-and-local-government/resources/2023-04-17T13-10-20Z-2022-12-31-organogram-junior.csv'
    #url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-department-for-communities-and-local-government/resources/2022-09-26T16-48-50Z-2022-06-30-organogram-junior.csv'
    #url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2021-07-22T14-40-16Z-2021-03-31-organogram-junior.csv'
    #url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2022-04-04T13-43-11Z-2021-09-30-organogram-junior.csv'
    url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-department-for-communities-and-local-government/resources/2022-02-01T12-29-33Z-2021-12-31-organogram-junior.csv'
    #url = 'https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-crown-prosecution-service/resources/2021-03-26T13-52-24Z-2020-03-31-organogram-junior.csv'

    organogram_dtypes = {
        'Parent Department': str,
        'Organisation': str,
        'Unit': str,
        'Reporting Senior Post': str,
        'Grade': str,
        'Payscale Minimum (£)': pd.Int64Dtype(),
        'Payscale Maximum (£)': pd.Int64Dtype(),
        'Generic Job Title': str,
        'Number of Posts in FTE': str,
        'Professional/Occupational Group': str,
        'Office Region': str
    }

    return pd.read_csv(url, sep=',', dtype=organogram_dtypes)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
