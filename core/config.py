from pydantic import BaseModel
from pydantic_settings import BaseSettings

class Run(BaseModel):
    host: str = 'localhost',
    port: int = 8000

class Database(BaseModel):
    url: str = ''

class ApiV1(BaseModel):
    prefix: str = '/v1'
    get_all_ads: str = '/all_ads'
    new_ad: str = '/new_ad'
    delete_ad: str = '/delete_ad'
    update_ad: str = '/update_ad'
    get_one: str = '/get_one/{id}'

class Api(BaseModel):
    prefix: str = '/home'
    auth: str = '/auth'
    user: str = '/user'
    v1: ApiV1 = ApiV1()

class Settings(BaseSettings):
    run: Run = Run()
    db: Database = Database()
    api: Api = Api()

settings = Settings()
