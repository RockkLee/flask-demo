from typing import Optional

from flask_sqlalchemy.session import Session

from flask_demo.helper.exception import CustomException
from flask_demo.helper.metaclass.singleton_meta import SingletonMeta
from flask_demo.orm.dao.video_dao import VideoDao
from flask_demo.orm.database import session
from flask_demo.service.dto.video_dto import VideoDto, VideoDtoMapper
from flask_demo.orm.models.video import VideoMapper


class VideoService(metaclass=SingletonMeta):
    def __init__(self):
        self.__video_dao = VideoDao()

    @session
    def get_video_by_id(self, video_id: int, s: Session) -> VideoDto:
        video = self.__video_dao.get(video_id, s)
        if video is None:
            raise CustomException("Video not found", 404)
        return VideoDtoMapper.from_video_model(video)

    @session
    def add_video(self, video_dto: VideoDto, s: Session) -> str:
        self.__video_dao.add(VideoMapper.from_video_dto(video_dto), s)
        print(video_dto)
        print(video_dto.name)
        return "Added video"

    @session
    def update_video(self, video_dto: VideoDto, s: Session) -> str:
        video = VideoMapper.from_video_dto(video_dto)
        self.__video_dao.update(video, s)
        return "Updated video"

    @session
    def delete_video(self, video_id, s: Session):
        self.__video_dao.delete(video_id, s)
        return "Deleted video"

