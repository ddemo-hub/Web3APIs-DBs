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

def deleteFromPayable_Check(contractHash):
    collectionPC.delete_one({'Contract_Hash': contractHash})

def deleteFromBNB_by_Block(blockID):
    collectionBNB.delete_one({'Block_ID': blockID})

def deleteAll():
    collectionPC.delete_many({})
    collectionBNB.delete_many({})

def findInPayable_Check(contractHash):
    collectionPC.find({'Contract_Hash': contractHash})

def findInBNB_by_Block(blockID):
    collectionBNB.find({'Block_ID': blockID})
