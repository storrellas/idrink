#Grab the latest alpine image
FROM alpine:latest

MAINTAINER Sergi Torrellas

ARG http_proxy=http://barc.proxy.corp.sopra:8080/
ARG https_proxy=http://barc.proxy.corp.sopra:8080/

# Add folder
RUN apk add --no-cache --update python py-pip bash
ADD . /repo/
WORKDIR /repo/
RUN pip install -r requirements_sqlite.txt
RUN python manage.py makemigrations combiner
RUN python manage.py migrate
RUN python manage.py loaddata drinks ingredients

EXPOSE 8000

# Run container
CMD python /repo/manage.py runserver 0.0.0.0:$PORT
#sudo docker run -t -p8000:8000 idrink
