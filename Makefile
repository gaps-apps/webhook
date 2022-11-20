.PHONY: all run tests 

run: stop
	docker-compose up get_account_bot --build -d

stop:
	docker-compose kill get_account_bot

tests: stop run
	docker-compose exec -ti get_account_bot bash -c "cd /opt; pipenv run pytest -vv tests/"

black:
	black .

mypy:
	mypy --follow-imports skip --ignore-missing-imports --warn-unreachable --pretty --tb .

make logs:
	docker-compose logs get_account_bot