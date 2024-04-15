from pydantic import BaseModel

class CrewInsert(BaseModel):
    count_people:int
    experience:int

class CrewUpdate(CrewInsert):
    id:int

class TechnicInsert(BaseModel):
    name:str
    battle_rating:float
    rank:int
    id_crew:int

class TechnicUpdate(TechnicInsert):
    id:int