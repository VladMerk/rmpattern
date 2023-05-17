FROM python:3.10-alpine

RUN apk update

WORKDIR /usr/rmpattern

COPY . .

RUN pip install -U pip -r requirements.txt

RUN python -m pytest

ENTRYPOINT ["python", "main.py"]

CMD ["--help"]
