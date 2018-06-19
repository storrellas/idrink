#!/bin/bash
source venv3/bin/activate
./node_modules/.bin/webpack --config webpack.config.js --watch & ./manage.py runserver 0.0.0.0:8081
