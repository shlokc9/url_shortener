"""
    Utils module
"""

__author__ = "Shlok Chaudhari"


import os
import json
import pandas as pd
from flask import Flask
from app.constants import ConstantPaths as path, GenericConstants as const


def create_app() -> Flask:
    """
        Method to initialize the flask app. It should contain all the flask
        configuration
    Returns:
         Flask: instance of Flask application
    """
    flask_app = Flask(__name__)
    return flask_app


def is_url_in_store_file(url, url_store_df) -> bool:
    """
        Checks given URL in store file
    Args:
        url: given URL string
        url_store_df: URL store file as dataframe
    Returns:
         (bool): True if the URL is present
         in the store file else False
    """
    if url in url_store_df.values:
        return True
    else:
        return False


def read_url_store_file() -> pd.DataFrame:
    """
        Reads the URL store file as a dataframe
    Returns:
         pd.DataFrame: URL store file as a dataframe
    """
    if os.path.exists(path.URL_FILE_STORE):
        df = pd.read_csv(path.URL_FILE_STORE, names=[const.GIVEN_URL, const.SHORT_URL])
    else:
        df = pd.DataFrame(columns=[const.GIVEN_URL, const.SHORT_URL])
    return df.drop_duplicates(keep=False, ignore_index=True)


def write_url_store_file(given_url, short_url, url_store_df):
    """
        Writes the contents of the dataframe
        to the URL store file
    Args:
        given_url: given URL string
        short_url: converted short URL
        url_store_df: URL store file as pandas dataframe
    """
    new_url_data = {const.GIVEN_URL: given_url, const.SHORT_URL: short_url}
    url_store_df = url_store_df.append(new_url_data, ignore_index=True)
    url_store_df.to_csv(path.URL_FILE_STORE)


def get_short_url(url, url_store_df) -> str:
    """
        Fetches short URL using given long URL
    Args:
        url: given URL string
        url_store_df: URL store file as dataframe
    Returns:
        (str): short URL
    """
    return url_store_df.loc[url_store_df[const.GIVEN_URL] == url, const.SHORT_URL].iloc[0]


def get_long_url(short_url, url_store_df) -> str:
    """
        Fetches long URL using short long URL
    Args:
        short_url: short URL string
        url_store_df: URL store file as dataframe
    Returns:
        (str): long URL
    """
    return url_store_df.loc[url_store_df[const.SHORT_URL] == short_url, const.GIVEN_URL].iloc[0]


def form_short_url(base62_uid) -> str:
    """
        Generates the short URL using the
        base62 UID
    Returns:
        short URL
    """
    return f"{get_base_url()}/{base62_uid}"

def get_base_url():
    """
        Read configuration file and fetch
        application service URL
    Returns:
        service URL
    """
    with open(path.CONFIG) as file_obj:
        config = json.load(file_obj)
    return config[const.APP_SERVICE_URL]
