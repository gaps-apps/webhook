FROM python:3.11-bullseye

LABEL maintainer="fuzz88 <ivan@oschepkov.ru>"

RUN apt-get update
RUN apt-get upgrade -y

RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./Pipfile.* /opt/
WORKDIR /opt/

RUN pipenv --python 3.11
RUN pipenv -v sync 

COPY ./ /opt


CMD ["sh", "/opt/entrypoint.sh"]
