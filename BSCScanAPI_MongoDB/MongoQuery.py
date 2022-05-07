import Constants as keys

import pymongo
from pymongo import MongoClient

cluster = MongoClient(keys.MongoCluster)
db = cluster["BSCScan"]
collectionSC = db["Payable_Check"]
collectionBNB = db["BNB_by_Block"]

def insertToPayable_Check(post):
    collectionSC.insert_one(post)

def insertToBNB_by_Block(post):
    collectionBNB.insert_one(post)
