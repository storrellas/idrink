FROM python:2.7.15
MAINTAINER Sergi Torrellas

# Add folder
ADD . /repo/
WORKDIR /repo/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations combiner
RUN python manage.py migrate
RUN python manage.py loaddata drinks ingredients
