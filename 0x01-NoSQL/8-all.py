#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    return [i for i in mongo_collection.find()]
