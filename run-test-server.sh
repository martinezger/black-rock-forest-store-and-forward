#!/bin/bash

python init_database.py
python mqtt_sub.py &
export FLASK_APP=app/app.py
export FLASK_DEBUG=True
export FLASK_ENV=development
flask run -p 2323 --host 0.0.0.0