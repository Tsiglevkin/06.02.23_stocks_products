FROM python:3.10

COPY ./requirements.txt /src/requirements.txt

RUN pip install -r /src/requirements.txt

ENV SECRET_KEY=9s9i5_0@%+y^6l*t-+qz5%b+1)onhujknbkyyfqq4)mm7&8hs8
ENV DEBUG=True
ENV ALLOWED_HOSTS=127.0.0.1
ENV DB_ENGINE=django.db.backends.sqlite3
ENV DB_NAME=docker_base

RUN ['python', 'manage.py', 'migrate']

EXPOSE 6060
WORKDIR src

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stocks_products.wsgi"]
