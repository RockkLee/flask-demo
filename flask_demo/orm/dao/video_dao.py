from flask_demo.helper.metaclass.singleton_meta import SingletonMeta
from flask_demo.orm.models.video import Video
from sqlalchemy.orm import Session


class VideoDao(metaclass=SingletonMeta):
    def __init__(self):
        pass

    def add(self, video: Video, s: Session):
        s.add(video)

    def update(self, video: Video, s: Session):
        mydict = video.__dict__
        del mydict['_sa_instance_state']
        s.query(Video).filter_by(id=video.id).update(mydict)

    def delete(self, video_id:Video, s: Session):
        result = s.query(Video).filter_by(id=video_id).first()
        s.delete(result)

    def get(self, video_id, s) -> Video:
        return s.query(Video).filter_by(id=video_id).first()