from fastapi import APIRouter
from server.collection_validator import TechnicInsert, TechnicUpdate
from database import select_collection, insert_doc_in_collection, update_doc_in_collection, delete_doc_in_collection
from server.convertor import convert_docs_to_JSON, convert_JSON_to_doc
from server.documents.technic_doc import get_tech_collection_name
from types_collection import TypesCollection
from types_technic import TypesTechnic

tech_route = APIRouter()

def get_tech_docs(coll_name:str)->list:
    ''' Функция получения сконвертированных документов в JSON для сервера '''
    docs = select_collection(coll_name)
    converted_docs = convert_docs_to_JSON(docs, TypesCollection.technic)
    return converted_docs

def insert_tech_doc(tech_doc:TechnicInsert, type_tech:TypesTechnic)->None:
    new_doc = convert_JSON_to_doc(tech_doc, TypesCollection.technic, type_tech)
    coll_name = get_tech_collection_name(type_tech)
    insert_doc_in_collection(coll_name, new_doc)

def update_tech_doc(tech_doc:TechnicUpdate, type_tech:TypesTechnic)->None:
    new_doc = convert_JSON_to_doc(tech_doc, TypesCollection.technic, type_tech)
    coll_name = get_tech_collection_name(type_tech)
    update_doc_in_collection(coll_name, new_doc)

@tech_route.get("/air_tech")
async def select_air_tech_collection():
    docs = get_tech_docs("air_tech")
    return docs

@tech_route.get("/ground_tech")
async def select_ground_tech_collection():
    docs = get_tech_docs("ground_tech")
    return docs

@tech_route.get("/marine_tech")
async def select_marine_tech_collection():
    docs = get_tech_docs("marine_tech")
    return docs

@tech_route.post("/air_tech")
async def insert_air_tech_doc(tech_doc:TechnicInsert):
    insert_tech_doc(tech_doc, TypesTechnic.air)

@tech_route.post("/ground_tech")
async def insert_ground_tech_doc(tech_doc:TechnicInsert):
    insert_tech_doc(tech_doc, TypesTechnic.ground)

@tech_route.post("/marine_tech")
async def insert_marine_tech_doc(tech_doc:TechnicInsert):
    insert_tech_doc(tech_doc, TypesTechnic.marine)

@tech_route.put("/air_tech")
async def update_air_doc(tech_doc:TechnicUpdate):
    update_tech_doc(tech_doc, TypesTechnic.air)

@tech_route.put("/ground_tech")
async def update_ground_doc(tech_doc:TechnicUpdate):
    update_tech_doc(tech_doc, TypesTechnic.ground)

@tech_route.put("/marine_tech")
async def update_marine_doc(tech_doc:TechnicUpdate):
    update_tech_doc(tech_doc, TypesTechnic.marine)

@tech_route.delete("/air_tech")
async def delete_air_doc(id_doc:int):
    delete_doc_in_collection("air_tech", id_doc)

@tech_route.delete("/ground_tech")
async def delete_ground_doc(id_doc:int):
    delete_doc_in_collection("ground_tech", id_doc)

@tech_route.delete("/marine_tech")
async def delete_marine_doc(id_doc:int):
    delete_doc_in_collection("marine_tech", id_doc)