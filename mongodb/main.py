from pymongo import MongoClient
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set up connection to MongoDB Atlas
client = MongoClient(os.environ.get("MONGODB_URI"))
db = client.test
# dbs = client.list_database_names()
# test_db = client.test 
# # list all of the collections inside of this database
# collections = test_db.list_collection_names
# print(collections)

# def insert_test_doc():
#     collection = test_db.test
#     test_document = {
#         "name": "Tim",
#         "type": "Test"
#     }
#     inserted_id = collection.insert_one(test_document).inserted_id # the id of the document
#     print(inserted_id)

# production = client.production
# person_collection = production.person_collection
# insert_test_doc()

# def create_document():
#     first_name = ["Tim", "Sarah", "Jennifer", "Jose", "Brad", "Allen"]
#     last_name = ["Ruscica", "Smith", "Bart", "Cater", "Pit", "Geral"]
#     age = [21, 40, 23, 19, 34, 67,]
#     docs = []
#     # when you zip it just going to give us all of these items of the corresponding indices in tuple
#     for first_name, last_name, age in zip(first_name, last_name, age):
#         doc = {"first+name": first_name, "last_name": last_name, "age": age}
#         docs.append(doc)
#         person_collection.insert_one(doc)

#     person_collection.insert_many(docs)

# # reading documents
# printer = pprint.PrettyPrinter()

# def find_all_people():
#     people = person_collection.find() # allows you to insert a query object wich is different properties that you're trying to match with when your looking for elements or looking for documents
#     # in this case if you leave this empty it's just going to find all of the people or all of the documents in the collection

#     for person in people:
#         printer.pprint(person)

# find_all_people()

# def find_tim():
#     tim = person_collection.find_one({"first_name": "Tim"})
#     printer.pprint(tim)

# def count_all_people():
#     count = person_collection.count_documents(filter={})
#     # count = person_collection.find().count()
#     print("Number of people", count)

# count_all_people()

# def get_person_by_id(person_id):
#     from bson.objectid import ObjectId

#     _id = ObjectId(person_id)
#     person = person_collection.find_one(_id)
#     printer.pprint(person)

# #get_person_by_id("")

# def get_age_range(min_age, max_age):
#     # SELECT * FROM person WHERE age >= min_age AND age <= max_age
#     query = {
#         {"$and": [
#             {"age": {"$gte": min_age}},
#             {"age": {"$lte": max_age}}
#         ]}
#     }
#     people = person_collection.find(query).sort("age")
#     for person in people:
#         printer.print(person)

# #get_age_range(20, 35)

# def project_columns():
#     # id: 0 indicates I don't want to have the id's in my result
#     columns = {"_id": 0, "first_name": 1, "last_name": 1}
#     people = person_collection.find({}, columns) # it's going to do a projection, it's only going to give thw columns I specified.
#     for person in people:
#         printer.pprint(person)

# def update_person_by_id(person_id):
#     from bson.objectid import ObjectId

#     _id = ObjectId(person_id)

#     all_updates = {   # this is going to set a new field to a value of our choice.
#          "$set": {"new_field": True},  # if this field was something that currently existed, we would override that field.
#          "$inc": {"age": 1},
#          "$rename": {"first_name": "first", "last_name": "last"}
#     }
#     person_collection.update_one({"_id": _id}, all_updates)

#     # remove
#     person_collection.update_one({"_id": _id}, {"$unset": {"new_field": ""}})

# #update_person_by_id()

# def replace_one(person_id):
#     from bson.objectid import ObjectId
#     _id = ObjectId(person_id)

#     new_doc = {
#         "first_name": "new first name",
#         "last_name": "new last name",
#         "age": 100
#     }

#     person_collection.replace_one({"_id": _id}, new_doc)

# def delete_doc_by_id(person_id):
#     from bson.objectid import ObjectId
#     _id = ObjectId(person_id)
#     person_collection.delete_one({"_id": _id})
#     person_collection.delete_many({"_id": _id})

# address = {
#     "_id": "6232322424a4284e24",
#     "street": "Bay Street",
#     "number": 2706,
#     "city": "San Francisco",
#     "country": "United States",
#     "zip": "94107"
# }

# def add_address_embed(person_id, address):
#     from bson.objectid import ObjectId
#     _id = ObjectId(person_id)

#     person_collection.update_one({"_id": _id}, {"$addToSet": {"addresses": address}})

# def add_address_relationship(person_id, address):
#     from bson.objectid import ObjectId
#     _id = ObjectId(person_id)

#     address = address.copy()
#     address["owner_id"] = person_id
#     address_collection = production.address
#     address_collection.insert_one()