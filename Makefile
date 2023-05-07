ENV_FILE ?= .env.dev
manager = server/manage.py
.DEFAULT_GOAL: docker-up
.DEFAULT: docker-up
.PHONY: client server migrations
docker-up:
	docker-compose --env-file $(ENV_FILE) --file docker-compose.yml up -d
build:
	npm --prefix client/ install
	pip install -r server/requirements.txt
	python3 server/manage.py makemigrations
	python3 server/manage.py migrate
client:
	npm run --prefix client/ dev
server:
	python server/manage.py runserver
docker-client:
	docker-compose --env-file $(ENV_FILE) --file docker-compose.yml up -d --no-deps client
docker-server:
	docker-compose --env-file $(ENV_FILE) --file docker-compose.yml up -d db server
docker-cdb:
	docker-compose --env-file $(ENV_FILE) --file docker-compose.yml up -d db client
docker-down:
	docker-compose down --rmi all
migrations:
	python3 server/manage.py makemigrations
	python3 server/manage.py migrate
