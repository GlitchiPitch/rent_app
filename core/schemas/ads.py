from pydantic import BaseModel

class AdAdd(BaseModel):
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

class AdShow(AdAdd):
    """
    Ad show schema if you need only snow that
    """
    ...

class Ad(AdAdd):
    """
    Main Ad schema
    """
    id: int