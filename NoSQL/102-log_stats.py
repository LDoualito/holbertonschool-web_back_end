#!/usr/bin/env python3
""" Logs module """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    count = collection.count_documents({})
    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})
    status = collection.count_documents({"method": "GET", "path": "/status"})
    ips = {}
    result = collection.find()
    for res in result:
        ip = res.get('ip')
        if ip and ip not in ips:
            ips[ip] = 1
        elif ip:
            ips[ip] += 1

    print(f"{count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")
    print("IPs:")
    for ip in sorted(ips, key=ips.get, reverse=True)[:10]:
        print("\t{}: {}".format(ip, ips[ip]))
    client.close()
    