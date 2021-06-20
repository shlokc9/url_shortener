FROM python:3.7
LABEL PROJECT="url_shortener"

COPY . /app
WORKDIR /app

RUN /bin/bash ./docker/scripts/build.sh

RUN /bin/bash ./docker/scripts/test.sh

ENTRYPOINT ["/bin/bash", "./docker/scripts/run.sh"]
