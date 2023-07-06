#!/usr/bin/env python3
""" Find module """


def schools_by_topic(mongo_collection, topic):
    """ Find document filtered by topic """
    return mongo_collection.find(
        {"topics": {"$in": [topic]}}
    )
