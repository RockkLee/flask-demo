from dataclasses import dataclass
from typing import Optional


@dataclass
class VideoDto:
    id: Optional[int] = None
    name: Optional[str] = None
    views: Optional[int] = None
    likes: Optional[int] = None


class VideoDtoMapper:
    @staticmethod
    def from_video_model(video):
        return VideoDto(
            id=video.id,
            name=video.name,
            views=video.views,
            likes=video.likes
        )