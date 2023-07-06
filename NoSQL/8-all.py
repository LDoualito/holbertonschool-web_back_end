#!/usr/bin/env python3
""" Dipslays all the document in the collection """


def list_all(mongo_collection):
    """ return a list of all document in mongo_collection """
    return mongo_collection.find()
