from flask import Flask
from flask_demo.orm.database import db_session
from flask_cors import CORS
from flask_demo.api.video_api import video_bp
from flask_demo.config.config import flask_config


app = Flask(__name__)
# load the config file
app.config.from_object(flask_config)
# register blueprints
app.register_blueprint(video_bp, url_prefix='/video')
CORS(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=8088)
