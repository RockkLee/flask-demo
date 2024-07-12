# Import Flask and Blueprint
from flask import Blueprint, request, jsonify
from flask_restx import Resource, Api, Namespace

from flask_demo.api.handler.handler import register_exception_handlers
from flask_demo.api.req.video_update_req import video_update_req
from flask_demo.api.req.video_create_req import video_create_req
from flask_demo.api.resp.video_resp import VideoRespMapper, video_resp
from flask_demo.service.dto.video_dto import VideoDto
from flask_demo.service.video_service import VideoService
from flask_demo.config import SWAGGER_DOC

# use this for the blueprint implementation
video_bp = Blueprint('video_bp', __name__)
api = Api(video_bp, title="Directory API", version="0.1.0", doc=SWAGGER_DOC)
ns = Namespace('video_ns', description='Version 1 API')
ns.models = {
    # register request model
    video_create_req.name: video_create_req,
    video_update_req.name: video_update_req
}
api.add_namespace(ns, path="/")
register_exception_handlers(api)


class VideoApi(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._video_service = VideoService()


@ns.route('/<int:video_id>')
class GetVideoById(VideoApi):
    @ns.marshal_with(video_resp)
    def get(self, video_id):
        video = VideoRespMapper.from_video_dto(
            self._video_service.get_video_by_id(video_id)
        )
        return video, 200


@ns.route('/add')
class AddVideo(VideoApi):
    @ns.expect(video_create_req, validate=True)
    def post(self):
        video_req = request.get_json()
        dto = VideoDto(**video_req)
        msg = self._video_service.add_video(dto)
        return msg, 200


@ns.route('/update')
class UpdateVideo(VideoApi):
    @ns.expect(video_update_req, validate=True)
    def put(self):
        video_req = request.get_json()
        msg = self._video_service.update_video(VideoDto(**video_req))
        return msg, 200


@ns.route('/delete/<int:video_id>')
class DeleteVideo(VideoApi):
    def delete(self, video_id):
        msg = self._video_service.delete_video(video_id)
        return msg, 200