#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    if not kwargs:
        return ''
    doc = mongo_collection.insert_one(kwargs)
    return str(doc.inserted_id)


if __name__ == '__main__':
    pass