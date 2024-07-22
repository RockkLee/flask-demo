# flask-demo
## Use the declarative extension in SQLAlchemy
- https://flask.palletsprojects.com/en/2.3.x/patterns/sqlalchemy/

<br>

## Use `flask.Blueprint` and `flask_restx` to build the api and swagger documents
### `video_api.py`
1. Create a `flask.Blueprint` called `video_bp`
2. Create a `flask_restx.Api` called `api` with  `video_bp`
3. Create a `flask_restx.NameSpace` called `ns` inside `api` (`flask_restx.Api`)
4. Use the decorator `@ns.route` to register HTTP APIs
### `app.py`
5. Register the blueprint `video_bp`

<br>

## Initialize Database tables 
- run `create_table.py`

<br>

## Deploy this app with gunicorn and docker
- Export dependencies from poetry.toml and exclude dev dependencies
    - `poetry export -f requirements.txt --output requirements.txt --without-hashes --only main`
- run `Dockerfile`
- run `docker-compose.yml`