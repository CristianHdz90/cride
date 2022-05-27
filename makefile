export COMPOSE_FILE=local.yml

most:
	docker-compose --profile most up

django:
	docker rm -f cride-platzi_django_1
	docker-compose -f local.yml run --rm --service-ports django

