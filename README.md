# URL Shortener

This repository consists of a URL shortener application.

It is a REST API based application which converts long URL to short URL. It also returns a corresponding long URL for previously converted short URL

There are two APIs that achieve the said functionality.


Following is the pre-built image on docker hub.

https://hub.docker.com/repository/docker/shlokc/url_shortener_application

Following is the command to run the image as container.

``` {.sourceCode .bash}
docker run -d --restart=always \
	-p 0.0.0.0:8080:5000 \
	--name url_shortener \
	-v /url_shortener_data:/app/data \
	-v /url_shortener_logs:/app/logs \
	shlokc/url_shortener_application:1.2
```


API specifications:

``` {.sourceCode .bash}
POST http://0.0.0.0:8080/short_url

Request payload:
{
	'url': 'http://google.com/'
}

Response:
{
	'message': 'Converted the long URL to a short URL',
	'outcome': 'success',
	'url': 'http://localhost:8080/3zELeF6'
}
```

``` {.sourceCode .bash}
GET http://0.0.0.0:8080/long_url

Request payload:
{
	'url': 'http://localhost:8080/3zELeF6'
}

Response:
{
	'message': 'Fetched long URL using given short URL ',
	'outcome': 'success',
	'url': 'http://google.com/'
}
```

Redirection to the original URL is also handled when opening the short URL on browser.

Please note that the application is not SSL-certified.

Thank you :)
