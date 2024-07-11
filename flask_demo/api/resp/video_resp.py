from flask_restx import fields, Model

video_resp = Model('VideoCreate', {
    'id': fields.Integer,
    'name': fields.String,
    'likes': fields.Integer,
    'views': fields.Integer
})


class VideoRespMapper:
    @staticmethod
    def from_video_dto(video_dto) -> dict:
        return {
            'name': video_dto.name,
            'likes': video_dto.likes,
            'views': video_dto.views
        }