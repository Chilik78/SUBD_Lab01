from pymongo.database import Database
from types_technic import TypesTechnic
from .support_functions import get_generate_tech_docs, get_generate_crew_docs, get_tech_collection_name

def generate_crew_documents(db:Database, count_documents:int)->None:
   ''' Функция генерации документов для коллекций экипажа '''
   crew_collection = db.get_collection("crew")
   docs = get_generate_crew_docs(crew_collection, count_documents)
   crew_collection.insert_many(docs)

def generate_tech_documents(db:Database, count_documents:int, type_tech:TypesTechnic)->None:
   ''' Функция генерации документов для коллекций техники '''
   tech_coll_name = get_tech_collection_name(type_tech)
   tech_collection = db.get_collection(tech_coll_name)
   crew_collection = db.get_collection("crew")
   docs = get_generate_tech_docs(crew_collection, tech_collection, count_documents, type_tech)
   tech_collection.insert_many(docs)

def generate_documents(db:Database, count_documents:int)->None:
   generate_crew_documents(db, count_documents)
   generate_tech_documents(db, count_documents, TypesTechnic.ground)
   generate_tech_documents(db, count_documents, TypesTechnic.marine)
   generate_tech_documents(db, count_documents, TypesTechnic.air)