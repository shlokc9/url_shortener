"""
    Pytest module for URL shortener
"""

__author__ = "Shlok Chaudhari"


import pytest
from app.url_shortener import URLShortener


class TestURLShortener:
    """
        Class that defines all the unit test-cases
        for the URL shortener
    """

    def test_pass_url_shortener(self, valid_url):
        """
            Tests if URLShortener works successfully
        """
        short_url = URLShortener(valid_url).short_url
        message = "URLShortener has shortened the given URL"
        assert short_url, message

    def test_excp_url_shortener(self, invalid_url):
        """
            Tests if URLShortener throws ValueError
        """
        with pytest.raises(ValueError) as exception_info:
            short_url = URLShortener(invalid_url).short_url
        assert exception_info.match("Given URL is invalid")
