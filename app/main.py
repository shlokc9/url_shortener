"""
    Module to run a flask application that serves an API for an URL shortener
"""

__author__ = "Shlok Chaudhari"


from flask import request
from app import logger, create_app
from app.url_shortener import URLShortener


app = create_app()


@app.route("/shorten_url", methods=["POST"])
def convert_long_to_short():
    """
        Converts the long URL in the request
        to a shortened URL
    Return:
         response: shortened URL
    """
    logger.info("Starting /shorten_url API. Reading the request body")
    request_body = request.get_json()
    logger.info("Reading the URL from request body")
    given_url = request_body.get("url", None)
    logger.info("Executing URLShortener module")
    short_url = URLShortener(given_url).short_url
    logger.info("Returning the resultant short URL. Completed /shorten_url API")
    success_dict = {
        "outcome": "success",
        "message": "Converted the long URL to a short URL",
        "url": short_url
    }
    return success_dict, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
