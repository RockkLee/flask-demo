from flask_demo.orm.database import Base
from sqlalchemy import Column, String, BigInteger, Integer

from flask_demo.service.dto.video_dto import VideoDto


class Video(Base):
    __tablename__ = 'videos'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    likes = Column(Integer)
    views = Column(Integer)


class VideoMapper:
    @staticmethod
    def from_video_dto(video_dto: VideoDto):
        return Video(
            id=video_dto.id,
            name=video_dto.name,
            likes=video_dto.likes,
            views=video_dto.views
        )