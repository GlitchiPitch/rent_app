import uuid

from pydantic import BaseModel

class AdCreate(BaseModel):
    #TODO link photos
    """
    Ad schema
    :param room_count: int
    :param cost: int
    :param address: str
    """
    room_count: int
    cost: int
    address: str | None = None

class AdShow(AdCreate):
    """
    Ad show schema if you need only snow that
    """
    ...
class Ad(AdCreate):
    """
    Main Ad schema
    """
    user_id: uuid.UUID
