#!/usr/bin/env python3
""" Update module """


def update_topics(mongo_collection, name, topics):
    """update the topics of a document in mongo_collection"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )