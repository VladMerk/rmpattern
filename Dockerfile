FROM python:3.10-alpine

RUN apk update && apk add git nodejs npm

WORKDIR /usr/rmpattern

COPY . /usr/rmpattern

RUN pip install -U pip -r requirements.txt

RUN mkdir /data

RUN python -m pytest

ENTRYPOINT ["python", "main.py"]

CMD ["--help"]
