import pymongo
import pprint
import datetime
from bson.son import SON
from pymongo import MongoClient


def insertUsers(userCollection):
    user1 = {
        "name": "Hannelore Schmidt",
        "hobbies": ["stricken", "häkeln", "kickboxen"],
        "birth": datetime.datetime(2001, 3, 2)
    }
    userCollection.insert_one(user1)

    userCollection.insert_many([
        {
            "name": "Jochen von der Lippe",
            "hobbies": ["Witze erzählen", "stricken", "Rollschuh fahren"],
            "birth": datetime.datetime(2000, 6, 2)
        },
        {
            "name": "Schill QiGong",
            "hobbies": ["chillen", "Qigong", "kickboxen"],
            "birth": datetime.datetime(1999, 7, 6)
        },
        {
            "name": "Joachim Frühlingsbäcker",
            "alter": "34",
            "hobbies": [],
            "lieblingsobst": "Birne",
            "birth": datetime.datetime(2001, 3, 2)
        },
        {
            "name": "Joe",
            "hobbies": ["essen", "trinken", "schlafen"],
            "lieblingsobst": "Kirsche",
            "straße": "Kirchstraße",
            "hausnummer": "2",
            "plz": "12345",
            "ort": "Bremen",
            "lieblingsmahlzeit": "Mittagessen",
            "birth": datetime.datetime(1998, 4, 4)
        }
    ])


def aggregation():
    pipeline = [
        {"$unwind": "$hobbies"},
        {"$group": {"_id": "$hobbies", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("_id", -1)])}
    ]

    hobbyCounts = userCollection.aggregate(pipeline)
    pprint.pprint(list(hobbyCounts))


client = MongoClient('localhost', 27017)

db = client.PysHbDb

userCollection = db.users
insertUsers(userCollection)

queriedUser = userCollection.find_one({"lieblingsobst": "Kirsche"})
print(queriedUser)



queriedUsers = userCollection.find({"birth": {"$lt": datetime.datetime(2000, 1, 1)}}).sort("name").limit(3)
for user in queriedUsers:
    pprint.pprint(user)

# aggregation()

