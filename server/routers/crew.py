from fastapi import APIRouter
from server.collection_validator import CrewInsert, CrewUpdate
from database import select_collection, insert_doc_in_collection, update_doc_in_collection, delete_doc_in_collection
from server.convertor import convert_docs_to_JSON, convert_JSON_to_doc
from types_collection import TypesCollection

crew_route = APIRouter()

@crew_route.get("/crew")
async def select_crew_collection():
    docs = select_collection("crew")
    converted_docs = convert_docs_to_JSON(docs, TypesCollection.crew)
    return converted_docs

@crew_route.post("/crew")
async def insert_crew_doc(crew_doc:CrewInsert):
    new_doc = convert_JSON_to_doc(crew_doc, TypesCollection.crew)
    insert_doc_in_collection("crew", new_doc)

@crew_route.put("/crew")
async def update_crew_doc(crew_doc:CrewUpdate):
    new_doc = convert_JSON_to_doc(crew_doc, TypesCollection.crew)
    update_doc_in_collection("crew", new_doc)

@crew_route.delete("/crew")
async def delete_crew_doc(id_doc:int):
    delete_doc_in_collection("crew", id_doc)