#!/bin/bash

cd server
screen -t server -d -m py manage.py runserver 0.0.0.0:8000

cd ../client
screen -t client -d -m py manage.py runserver 0.0.0.0:3000
