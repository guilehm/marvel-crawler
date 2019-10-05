FROM python:3.7
ADD . /code
WORKDIR /code
COPY Pipfile* /tmp/
RUN pip install pipenv
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
EXPOSE 5000
