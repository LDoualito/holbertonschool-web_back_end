#!/usr/bin/env python3
""" Average module """
import pymongo


def top_students(mongo_collection):
    """ calculate the average of score
    for all students and returns it by order """
    students = mongo_collection.find()

    for student in students:
        projects = student.get("topics")
        total = 0
        count = 0
        avg = 0
        for project in projects:
            total += project.get("score")
            count += 1
        avg = total / count
        mongo_collection.update_one(
            {"name": student.get("name")},
            {"$set": {"averageScore": avg}}
        )

    return mongo_collection.find().sort('averageScore', pymongo.DESCENDING)
