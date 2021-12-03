"""
    Module to define all the constants in the application - URL Shortener
"""

__author__ = "Shlok Chaudhari"
__all__ = [
    "ConstantPaths",
    "GenericConstants",
    "URLConverterConstants"
]


import string


class ConstantPaths:
    """
        Class implementation of all the constant paths 
        in URL Shortner
    """

    CONFIG = "./config/config.json"
    URL_FILE_STORE = "./data/url_store.csv"


class GenericConstants:
    """
        Class implementation of all generic constants 
        in URL Shortner
    """

    SHORT_URL = "short_url"
    GIVEN_URL = "given_url"
    APP_SERVICE_URL = "app_service_url"


class URLConverterConstants:
    """
        Class implementation of constants in URLConverter class
    """

    EXPAND_OPERATION = "expand"
    SHORTEN_OPERATION = "shorten"
    SHORT_URL_CHARACTERS = f"{string.digits}{string.ascii_lowercase}{string.ascii_uppercase}"
    BASE62 = len(SHORT_URL_CHARACTERS)
