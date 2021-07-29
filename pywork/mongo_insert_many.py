# mongo_insert_many.py

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["customers"]

mylist = [
    { "name": "Amy" , "address": "Apple st 652"},
    { "name": "Hannah" , "address": "Mountain 21"},
    { "name": "Michael" , "address": "Valley 345"},
    { "name": "Sandy" , "address": "Ocean blvd 2"},
    { "name": "Betty" , "address": "Green Grass 1"},
    { "name": "Richard" , "address": "Sky st 331"},
    { "name": "Susan" , "address": "One way 98"},
    { "name": "Vicky" , "address": "Yellow Garden 2"},
    { "name": "Ben" , "address": "Park Lane 38"},
    { "name": "William" , "address": "Central st 954"},
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)