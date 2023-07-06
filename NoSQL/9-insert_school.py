#!/usr/bin/env python3
""" Insert module """


def insert_school(mongo_collection, **kwargs):
    """ insert a new document in mongo_collection """
    return mongo_collection.insert_one(kwargs).inserted_id
