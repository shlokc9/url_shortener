"""
    Utils module
"""

__author__ = "Shlok Chaudhari"


import os
import pandas as pd
from flask import Flask


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
    if os.path.exists("./data/url_store.csv"):
        df = pd.read_csv("./data/url_store.csv", names=["given_url", "short_url"])
    else:
        df = pd.DataFrame(columns=["given_url", "short_url"])
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
    new_url_data = {"given_url": given_url, "short_url": short_url}
    url_store_df = url_store_df.append(new_url_data, ignore_index=True)
    url_store_df.to_csv("./data/url_store.csv")


def get_short_url(url, url_store_df) -> str:
    """
        Fetches short URL using given long URL
    Args:
        url: given URL string
        url_store_df: URL store file as dataframe
    Returns:
        (str): short URL
    """
    return url_store_df.loc[url_store_df["given_url"] == url, "short_url"].iloc[0]


def get_long_url(short_url, url_store_df) -> str:
    """
        Fetches long URL using short long URL
    Args:
        short_url: short URL string
        url_store_df: URL store file as dataframe
    Returns:
        (str): long URL
    """
    return url_store_df.loc[url_store_df["short_url"] == short_url, "given_url"].iloc[0]


def form_short_url(base62_uid) -> str:
    """
        Generates the short URL using the
        base62 UID
    Returns:
        short URL
    """
    return f"http://localhost:5000/{base62_uid}"
