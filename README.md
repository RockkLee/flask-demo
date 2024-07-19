# flask-demo
## Use the declarative extension in SQLAlchemy
- https://flask.palletsprojects.com/en/2.3.x/patterns/sqlalchemy/

<br>

## Deploy this app with gunicorn and docker
- Export dependencies from poetry.toml and exclude dev dependencies
    - `poetry export -f requirements.txt --output requirements.txt --without-hashes --only main`
- run `Dockerfile`
- run `docker-compose.yml`