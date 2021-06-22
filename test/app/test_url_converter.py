"""
    Pytest module for URL converter
"""

__author__ = "Shlok Chaudhari"


import random
import pytest
from app.url_converter import URLConverter


class TestURLShortener:
    """
        Class that defines all the unit test-cases
        for the URL converter
    """

    def test_pass_long_url_converter(self, valid_url):
        """
            Tests if URLConverter works successfully for converting
            long URL to short URL
        """
        url_id = random.randint(10000000000, 99999999999)
        pytest.short_url = URLConverter(valid_url, url_id).url
        message = "URLConverter has shortened the given URL"
        assert True, message

    def test_excp_long_url_converter(self, valid_url):
        """
            Tests if URLConverter throws TypeError while converting
            long URL to short URL
        """
        url_id = random.randint(10000000000, 99999999999)
        with pytest.raises(TypeError) as exception_info:
            short_url = URLConverter(valid_url, url_id, operation="dqd").url
        assert exception_info.match("Given operation is not supported by the URLConverter")

    def test_pass_short_url_converter(self, valid_url):
        """
            Tests if URLConverter works successfully for converting
            short URL to long URL
        """
        url_id = random.randint(10000000000, 99999999999)
        long_url = URLConverter(pytest.short_url, url_id, operation="expand").url
        assert long_url == valid_url

    def test_excp_short_url_converter(self, invalid_url):
        """
            Tests if URLConverter throws ValueError while converting
            short URL to long URL
        """
        url_id = random.randint(10000000000, 99999999999)
        with pytest.raises(ValueError) as exception_info:
            short_url = URLConverter(invalid_url, url_id, operation="expand").url
        assert exception_info.match("Given Short URL does not exist in store file")
