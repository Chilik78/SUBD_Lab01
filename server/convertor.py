from types_collection import TypesCollection
from server.documents.crew_doc import crew_doc_in_JSON, crew_doc
from server.documents.technic_doc import technic_doc_in_JSON, technic_doc
from types_technic import TypesTechnic

def convert_docs_to_JSON(docs:list, type_coll:TypesCollection)->list[dict]:
    if(type_coll == TypesCollection.crew):
        return [crew_doc_in_JSON(doc) for doc in docs]
    elif(type_coll == TypesCollection.technic):
        return [technic_doc_in_JSON(doc) for doc in docs]
    
def convert_JSON_to_doc(json_doc, type_coll:TypesCollection, type_tech:TypesTechnic=None)->dict:
    if(type_coll == TypesCollection.crew):
        return crew_doc(json_doc)
    elif(type_coll == TypesCollection.technic):
        return technic_doc(json_doc, type_tech)