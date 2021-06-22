"""
    Module to run a flask application that serves an API for an URL shortener
"""

__author__ = "Shlok Chaudhari"


import random
from flask import request, g
from app import logger, create_app
from app.url_converter import URLConverter


def error_response(message):
    logger.exception(message)
    exp_dict = {"outcome": "failure", "message": message}
    return exp_dict, 400


app = create_app()


@app.before_request
def generate_url_id():
    g.url_id = random.randint(10000000000, 99999999999)


@app.route("/short_url", methods=["POST"])
def convert_long_to_short():
    """
        Converts the long URL in the request
        to a shortened URL
    Return:
         response: shortened URL
    """
    try:
        logger.info("Starting /short_url API. Reading the request body")
        request_body = request.get_json()
    except Exception:
        return error_response("Unable to fetch request body")

    logger.info("Reading the URL from request body")
    given_url = request_body.get("url", None)
    if not given_url:
        return error_response("Unable to read the URL from request body")

    try:
        logger.info("Executing URLConverter module")
        short_url = URLConverter(given_url, g.url_id).url
    except TypeError:
        return error_response("Given operation is not supported by the URLConverter")

    logger.info("Returning the resultant short URL. Completed /short_url API")
    success_dict = {
        "outcome": "success",
        "message": "Converted the long URL to a short URL",
        "url": short_url
    }
    return success_dict, 200


@app.route("/long_url", methods=["GET"])
def fetch_long_url():
    """
        Fetches the corresponding long URL
        using the short URL in the request
    Return:
         response: corresponding long URL
    """
    try:
        logger.info("Starting /long_url API. Reading the request body")
        request_body = request.get_json()
    except Exception:
        return error_response("Unable from request body")

    logger.info("Reading the URL from request body")
    given_url = request_body.get("url", None)
    if not given_url:
        return error_response("Unable to read the URL from request body")

    try:
        logger.info("Executing URLConverter module")
        long_url = URLConverter(given_url, g.url_id, operation="expand").url
    except ValueError:
        return error_response("Given Short URL does not exist in store file")
    except TypeError:
        return error_response("Given operation is not supported by the URLConverter")

    logger.info("Returning the fetched long URL. Completed /long_url API")
    success_dict = {
        "outcome": "success",
        "message": "Fetched long URL using given short URL ",
        "url": long_url
    }
    return success_dict, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
