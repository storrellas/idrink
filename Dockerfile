FROM python:2.7.15
MAINTAINER Sergi Torrellas

# Add folder
ADD . /repo/
WORKDIR /repo/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations combiner
RUN python manage.py migrate
RUN python manage.py loaddata drinks ingredients

EXPOSE 8000

# Run container
CMD ["python", "/repo/manage.py", "runserver", "0.0.0.0:8000"]
#sudo docker run -t -p8000:8000 42f0347aa4c6
