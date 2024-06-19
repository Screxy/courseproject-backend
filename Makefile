REGISTRY := "screxy/courseproject"

up:
	docker compose -f docker-compose.yaml up -d

down:
	docker compose -f docker-compose.yaml down

build:
	docker build -f ./Dockerfile . -t ${REGISTRY}/backend:dev
