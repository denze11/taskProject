#!/bin/bash
source '/home/www/code/taskProject/env/bin/activate'
exec gunicorn -c '/home/www/code/taskProject/taskProject/gunicorn_config.py' taskProject.wsgi
