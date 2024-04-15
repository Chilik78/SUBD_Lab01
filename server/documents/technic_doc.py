from server.collection_validator import TechnicInsert, TechnicUpdate
from database import get_last_id_collection
from types_technic import TypesTechnic

def get_tech_collection_name(type_tech:TypesTechnic)->str:
   collection_name = ''
   if(type_tech == TypesTechnic.ground):
      collection_name = "ground_tech"
   elif(type_tech == TypesTechnic.marine):
      collection_name = "marine_tech"
   elif(type_tech == TypesTechnic.air):
      collection_name = "air_tech"
   
   return collection_name

def technic_doc_in_JSON(doc:dict)->dict:
    return {
            "id_doc":str(doc['_id']),
            "name":str(doc['name']),
            "battle_rating":float(doc["battle_rating"]),
            "rank":int(doc["rank"]),
            "id_crew":int(doc["id_crew"]),
            "id_tech":int(doc["id"])
    }

def technic_doc(doc:TechnicInsert | TechnicUpdate, type_tech:TypesTechnic)->dict:
    id_tech = 0
    collection_name = get_tech_collection_name(type_tech)

    if(type(doc) == TechnicInsert):
        id_tech = get_last_id_collection(collection_name) + 1
    elif(type(doc) == TechnicUpdate):
        id_tech = doc.id

    return {
            "name": doc.name,
            "battle_rating": doc.battle_rating,
            "rank": doc.rank,
            "id_crew": doc.id_crew,
            "id": id_tech
    }