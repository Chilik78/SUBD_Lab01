from server.collection_validator import CrewInsert, CrewUpdate
from database import get_last_id_collection

def crew_doc_in_JSON(doc:dict)->dict:
    return {
            "id_doc": str(doc['_id']),
            "count_people": int(doc['count_people']),
            "experience": int(doc["experience"]),
            "id_crew": int(doc["id"])
    }

def crew_doc(doc:CrewInsert | CrewUpdate)->dict:
    id_crew = 0
    if(type(doc) == CrewInsert):
        id_crew = get_last_id_collection("crew") + 1
    elif(type(doc) == CrewUpdate):
        id_crew = doc.id

    return {
            "count_people": doc.count_people,
            "experience": doc.experience,
            "id": id_crew
    }