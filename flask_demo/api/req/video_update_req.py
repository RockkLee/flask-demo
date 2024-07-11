from flask_restx import Model, fields

video_update_req = Model('VideoUpdate', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=False),
    'likes': fields.Integer(required=False),
    'views': fields.Integer(required=False)
})