"""
    URL shortener module
"""

__author__ = "Shlok Chaudhari"
__all__ = "URLShortener"


from app import logger
from pyshorteners import Shortener
from app.utils import read_config, read_selected_service_from_config,\
    is_url_in_store_file, read_url_store_file, write_url_store_file, get_short_url


class URLShortener:
    """
        Class implementation of URL shortener
    """

    _config = read_config()

    def __init__(self, given_url):
        logger.info("Reading URL store file")
        url_store_df = read_url_store_file()
        logger.info("Checking if given URL in the store file")
        if is_url_in_store_file(given_url, url_store_df):
            logger.info("Given URL present in the store file")
            self._short_url = get_short_url(given_url, url_store_df)
        else:
            logger.info("URL not present in the store file")
            self._short_url = self._convert(given_url)
            logger.info("Writing new URL record to store file")
            write_url_store_file(given_url, self._short_url, url_store_df)

    @property
    def short_url(self): return self._short_url

    def _convert(self, given_url) -> str:
        """
            Convert the given_url to short URL
        Args:
            given_url: Given URL
        Return:
            Short URL
        """
        url_shortener = self._init_url_shortener_service()
        logger.info("Converting long URL to short URL")
        try:
            return url_shortener.short(given_url)
        except Exception:
            raise ValueError("Given URL is invalid")

    def _init_url_shortener_service(self) -> object:
        """
            Initialize the URL shortener service
        Returns:
            object: URL manipulation service object
        """
        logger.info("Reading the selected service from config")
        try:
            service_type, access_token = read_selected_service_from_config(self._config)
        except KeyError:
            raise KeyError("Invalid config file found")
        logger.info("Initializing URL shortener service")
        shortener = Shortener(api_key=access_token)
        return shortener.__getattr__(service_type)
