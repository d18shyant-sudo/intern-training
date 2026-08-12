from pydantic import BaseModel
from datetime import datetime
class Cat_Fact(BaseModel):
    fact: str
    length: int
class Joke(BaseModel):
    type: str
    setup: str
    punchline: str
    id: int
class current_units(BaseModel):
    time:str
    interval:str
    temperature_2m:str
class current(BaseModel):
    time:datetime
    interval:int
    temperature_2m:float
class Weather(BaseModel):
    latitude:float
    longitude:float
    generationtime_ms:float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation:str
    elevation: float
    current_units:current_units
    current:current