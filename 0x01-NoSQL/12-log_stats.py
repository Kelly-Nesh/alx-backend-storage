#!/usr/bin/env python3
"""Log nginx stats"""
from pymongo import MongoClient


client = MongoClient()
db = client.logs
coll = db['nginx']


print("{} logs".format(coll.count_documents({})))
print("Methods:")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for m in methods:
    print("\tmethod {}: {}".format(m, coll.count_documents({'method': m})))
print("{} status check".format(coll.count_documents({'path': '/status'})))