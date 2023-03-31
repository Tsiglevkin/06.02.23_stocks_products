FROM python:3.10

COPY ./requirements.txt /src/requirements.txt

RUN pip3 install -r /src/requirements.txt

EXPOSE 6060
WORKDIR src

CMD ['python3', '-u', 'main.py', '--host', '127.0.0.1', '--port', '6060']
