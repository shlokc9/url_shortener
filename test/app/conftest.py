"""
    Pytest fixture for URLShortener Module
"""

__author__ = "Shlok Chaudhari"

import pytest


@pytest.fixture
def valid_url():
    return "https://www.linkedin.com/in/shlokchaudhari9/"


@pytest.fixture
def invalid_url():
    return "sdadw"
