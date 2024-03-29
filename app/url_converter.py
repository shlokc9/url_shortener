"""
    URL converter module
"""

__author__ = "Shlok Chaudhari"
__all__ = "URLConverter"


from app import logger
from app.constants import URLConverterConstants as const
from app.utils import get_base_url, is_url_in_store_file, read_url_store_file, \
    write_url_store_file, get_short_url, get_long_url


BASE_URL = get_base_url()


class URLConverter:
    """
        Class implementation of URL converter
    """

    def __init__(self, given_url, url_id, operation="shorten"):
        self._url_id = url_id
        logger.info("Reading URL store file")
        url_store_df = read_url_store_file()
        if operation == const.SHORTEN_OPERATION:
            self._convert_long_to_short(given_url, url_store_df)
        elif operation == const.EXPAND_OPERATION:
            self._fetch_long_url(given_url, url_store_df)
        else:
            raise TypeError("Given operation is not supported by the URLConverter")

    @property
    def url(self): return self._converted_url

    def _fetch_long_url(self, short_url, url_store_df):
        """
            Fetch corresponding long URL for
            a short URL
        Args:
            short_url: converted short URL
            url_store_df: URL store as a dataframe
        """
        logger.info("Checking if given URL in the store file")
        if is_url_in_store_file(short_url, url_store_df):
            logger.info("Given Short URL present in the store file")
            self._converted_url = get_long_url(short_url, url_store_df)
        else:
            raise ValueError("Given Short URL does not exist in store file")

    def _convert_long_to_short(self, long_url, url_store_df):
        """
            Convert the given_url to short URL
        Args:
            long_url: Long URL string
            url_store_df: URL store as a dataframe
        """
        logger.info("Checking if given URL in the store file")
        if is_url_in_store_file(long_url, url_store_df):
            logger.info("Given URL present in the store file")
            self._converted_url = get_short_url(long_url, url_store_df)
        else:
            logger.info("URL not present in the store file")
            self._converted_url = f"{BASE_URL}/{self.convert_base10_to_base62(self._url_id)}"
            logger.info("Writing new URL record to store file")
            write_url_store_file(long_url, self._converted_url, url_store_df)

    @staticmethod
    def convert_base10_to_base62(url_id):
        """
            Convert base10 URL ID to base62
        Args:
            url_id: unique URL ID
        Returns:
            URL ID to base62
        """
        logger.info("Converting long URL to short URL")
        result_base62 = []
        while url_id > 0:
            index = url_id % const.BASE62
            result_base62.append(const.SHORT_URL_CHARACTERS[index])
            url_id = url_id // const.BASE62
        return "".join(result_base62[::-1])
