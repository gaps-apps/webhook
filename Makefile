.PHONY: all run tests 

run: stop
	docker-compose up webhook --build -d

stop:
	docker-compose kill webhook

tests: stop run
	docker-compose exec -ti webhook bash -c "cd /opt; pipenv run pytest -vv tests/"

format:
	isort .
	black .

mypy:
	mypy --follow-imports skip --ignore-missing-imports --warn-unreachable --pretty --tb .

make logs:
	docker-compose logs webhook
