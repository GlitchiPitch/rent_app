from pydantic import BaseModel
from pydantic.v1 import PostgresDsn
from pydantic_settings import BaseSettings

class Run(BaseModel):
    host: str = 'localhost',
    port: int = 8000

class Database(BaseModel):
    url: PostgresDsn = ''

class ApiV1(BaseModel):
    prefix: str = '/v1'
    get_all_ads: str = '/all_ads'
    new_ads: str = '/new_ads'

class Api(BaseModel):
    prefix: str = '/home'
    v1: ApiV1 = ApiV1()

class Settings(BaseSettings):
    run: Run = Run()
    db: Database = Database()
    api: Api = Api()

settings = Settings()
