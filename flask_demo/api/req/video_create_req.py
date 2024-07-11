from dataclasses import dataclass
from typing import Optional

from flask_restx import fields, Model

video_create_req = Model('VideoCreate', {
    'name': fields.String(required=True),
    'likes': fields.Integer(required=True),
    'views': fields.Integer(required=True)
})