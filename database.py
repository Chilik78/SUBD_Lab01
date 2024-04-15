from pymongo import MongoClient
from pymongo.database import Database
from termcolor import colored

def get_database(conn_string:str="mongodb://localhost:27017/war_thunder")->Database:
      try:
         client = MongoClient(conn_string)
         client.is_mongos
         return client['war_thunder']
      except Exception as e:
         print(colored("Отсутвует подключение к базе данных из-за интернета", color="red", attrs=['bold']))

def clear_all_collections()->None:
      '''Функция очищения всех коллекций'''

      db = get_database()
      names_collections = db.list_collection_names()
      for name in names_collections:
         db.get_collection(name).delete_many({})

def select_collection(coll_name:str)->list:
   db = get_database()
   return list(db.get_collection(coll_name).find({}))

def get_last_id_collection(coll_name:str)->int:
   '''Функция получения последнего id документа в коллекции'''

   db = get_database()
   collection = db.get_collection(coll_name)
   documents = list(collection.find({}))

   id_last_document = 0
   if(len(documents) != 0):
      id_last_document = documents[-1]["id"]

   return id_last_document

def insert_doc_in_collection(coll_name:str, doc:dict)->None:
   db = get_database()
   collection = db.get_collection(coll_name)
   collection.insert_one(doc)

def update_doc_in_collection(coll_name:str, doc:dict):
   db = get_database()
   collection = db.get_collection(coll_name)
   collection.find_one_and_update({"id":doc['id']}, {"$set": dict(doc)})

def delete_doc_in_collection(coll_name:str, id:int):
   db = get_database()
   collection = db.get_collection(coll_name)
   collection.find_one_and_delete({"id":id})