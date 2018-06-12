#!/bin/bash
source venv3/bin/activate
python pump_controller.py &
python manage.py runserver 0.0.0.0:8081
