from pymongo.collection import Collection
from types_technic import TypesTechnic
import random
from .generator_constants.export_constatnts import *

def get_last_id_collection(collection:Collection, field_name_with_id:str)->int:
   '''Функция получения последнего id документа в коллекции'''

   documents = list(collection.find({}))
   id_last_document = 0
   if(len(documents) != 0):
    id_last_document = documents[-1][field_name_with_id]

   return id_last_document

def get_all_id_crew_collection(crew_collection:Collection,)->list[int]:
  '''Функция получения всех id коллекции crew'''
  documents = list(crew_collection.find({}))
  crew_ids = list(set([doc["id"] for doc in documents]))
  return crew_ids

def get_constants_tech(type_tech:TypesTechnic)->tuple:
   constants = tuple
   if(type_tech == TypesTechnic.ground):
     constants = (NAMES_GROUND_TECH, BATTLE_RATING_GROUND_TECH, RANKS_GROUND_TECH)
   elif(type_tech == TypesTechnic.marine):
     constants = (NAMES_MARINE_TECH, BATTLE_RATING_MARINE_TECH, RANKS_MARINE_TECH)
   elif(type_tech == TypesTechnic.air):
     constants = (NAMES_AIR_TECH, BATTLE_RATING_AIR_TECH, RANKS_AIR_TECH)

   return constants

def get_tech_collection_name(type_tech:TypesTechnic)->str:
   collection_name = ''
   if(type_tech == TypesTechnic.ground):
      collection_name = "ground_tech"
   elif(type_tech == TypesTechnic.marine):
      collection_name = "marine_tech"
   elif(type_tech == TypesTechnic.air):
      collection_name = "air_tech"
   
   return collection_name

def get_generate_tech_docs(crew_collection:Collection, tech_coll:Collection, count_documents:int, type_tech:TypesTechnic)->list:

   id_last_document = get_last_id_collection(tech_coll, 'id')
   crew_ids = get_all_id_crew_collection(crew_collection)
   names, battle_rating, ranks = get_constants_tech(type_tech)
   tech_docs = [{
      "name" : names[random.randint(0, len(names) - 1)],
      "battle_rating" : battle_rating[random.randint(0, len(battle_rating) - 1)],
      "rank" : ranks[random.randint(0, len(ranks) - 1)],
      "id_crew" : crew_ids[random.randint(0, len(crew_ids) - 1)],
      "id" : id_last_document + i + 1
   } for i in range(count_documents)]
  
   return tech_docs

def get_generate_crew_docs(crew_collection:Collection, count_documents:int)->list:
   id_last_document = get_last_id_collection(crew_collection, 'id_crew')
   crew_docs = [{
      "count_people" : COUNT_PEOPLE[random.randint(0, len(COUNT_PEOPLE) - 1)],
      "experience" : EXPERIENCE[random.randint(0, len(EXPERIENCE) - 1)],
      "id" : id_last_document + i + 1
   } for i in range(count_documents)]

   return crew_docs