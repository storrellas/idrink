#Grab the latest alpine image
FROM alpine:3.18.3

MAINTAINER Sergi Torrellas

# Add folder
RUN apk add --no-cache --update python3 bash mosquitto
ADD . /repo/
WORKDIR /repo/
RUN pip3 install -r requirements3_sqlite.txt
RUN python3 manage.py makemigrations combiner
RUN python3 manage.py migrate
RUN python3 manage.py loaddata drinks ingredients

EXPOSE 8000

# Run container
CMD mosquitto & python3 /repo/pump_controller.py & python3 /repo/manage.py runserver 0.0.0.0:$PORT
#sudo docker run -t -p8000:8000 idrink
