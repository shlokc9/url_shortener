"""
    Module to run a flask application that serves an API for an URL shortener
"""

__author__ = "Shlok Chaudhari"


from flask import request
from app import logger, create_app
from app.url_shortener import URLShortener


def error_response(message):
    logger.exception(message)
    exp_dict = {"outcome": "failure", "message": message}
    return exp_dict, 400


app = create_app()


@app.route("/shorten_url", methods=["POST"])
def convert_long_to_short():
    """
        Converts the long URL in the request
        to a shortened URL
    Return:
         response: shortened URL
    """
    try:
        logger.info("Starting /shorten_url API. Reading the request body")
        request_body = request.get_json()
    except Exception:
        return error_response("Unable from request body")

    logger.info("Reading the URL from request body")
    given_url = request_body.get("url", None)
    if not given_url:
        return error_response("Unable to read the URL from request body")

    try:
        logger.info("Executing URLShortener module")
        short_url = URLShortener(given_url).short_url
    except ValueError:
        return error_response("Received URL from the request is invalid")
    except KeyError:
        return error_response("Config file is invalid")

    logger.info("Returning the resultant short URL. Completed /shorten_url API")
    success_dict = {
        "outcome": "success",
        "message": "Converted the long URL to a short URL",
        "url": short_url
    }
    return success_dict, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
