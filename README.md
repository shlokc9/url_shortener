# url_shortener

This repository consists of a URL shortener application.

It is a REST API based application which converts long URL to short URL. It also returns a corresponding long URL for previously converted short URL

There are two APIs that achieve the said functionality.


Following is the pre-built image on docker hub.

https://hub.docker.com/repository/docker/shlokc/url_shortener_application

Please use following command to run the image as container.

``` {.sourceCode .bash}
docker run -d --restart=always \
	-p 0.0.0.0:8080:5000 
	--name url_shortener 
	-v /url_shortener_data:/app/data
	-v /url_shortener_logs:/app/logs
	shlokc/url_shortener_application:1.1
```


Please find API specifications below.

``` {.sourceCode .bash}
POST http://0.0.0.0:8080/short_url
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

``` {.sourceCode .bash}
GET http://0.0.0.0:8080/long_url
```

Request payload:

``` {.sourceCode .bash}
{
	'url': 'https://bit.ly/3zELeF6'
}
```

Response:

``` {.sourceCode .bash}
{
	'message': 'Fetched long URL using given short URL ',
	'outcome': 'success',
	'url': 'http://google.com/'
}
```

Please note that the application is not SSL-certified.
