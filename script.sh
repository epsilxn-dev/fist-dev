#!/bin/bash
cd client
npm install
cd ..
docker exec -it server bash -c "pip install -r requirements.txt && python manage.py migrate"