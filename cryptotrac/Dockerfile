

FROM python:3.10

# set work directory
COPY . /app
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py InitialSetup