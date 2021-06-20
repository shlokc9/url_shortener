"""
    Utils module
"""

__author__ = "Shlok Chaudhari"


import os
import json
import pandas as pd


def read_config() -> dict:
    """
        Reads the config file
    Returns:
        (dict): config as a dictionary
    """
    with open("./config/config.json", 'r') as cfg_fs:
        config = json.load(cfg_fs)
    return config


def read_selected_service_from_config(config) -> tuple:
    """
        Reads the selected service type from the
        config and returns the service_type string
        and corresponding access_token string
    Args:
        config: config read as a dictionary
    Returns:
         (tuple): service_type, access_token
    """
    url_shortener_config = config["url_shortener"]
    service_type = url_shortener_config["type"]

    service_config = url_shortener_config[service_type]
    access_token = service_config["access_token"]

    return service_type, access_token


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
        return pd.read_csv("./data/url_store.csv", names=["given_url", "short_url"])
    else:
        return pd.DataFrame(columns=["given_url", "short_url"])


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

