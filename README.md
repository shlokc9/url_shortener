# url_shortener

This repository consists of a URL shortener application.

It is a REST API based application which serves a short URL when a long URL is passed as an argument over a request. 


Following is the pre-built image on docker hub.

https://hub.docker.com/repository/docker/shlokc/url_shortener_application

Please use following command to run the image as container.

``` {.sourceCode .bash}
docker run -d -p 0.0.0.0:8080:5000 --name url_shortener shlokc/url_shortener_application:1
```


Please find API specifications below.

``` {.sourceCode .bash}
POST http://0.0.0.0:8080/shorten_url
```

Request payload:

``` {.sourceCode .bash}
{
	'url': 'http://google.com/'
}
```

Response:

``` {.sourceCode .bash}
{
	'message': 'Converted the long URL to a short URL',
	'outcome': 'success',
	'url': 'https://bit.ly/3zELeF6'
}
```

Please note that the application is not SSL-certified.
