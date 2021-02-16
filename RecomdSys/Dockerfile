FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app/

COPY src/requirements.txt /app/
RUN pip install -r ./requirements.txt

ENV ENVIRONMENT production
 
COPY dataset/ /app/

COPY src/config.py src/main.py src/__init__.py /app/

