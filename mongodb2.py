import pymongo
from mongodb1 import mycol

myclient=pymongo.MongoClient("mongodb://localhost:27017/")


list1=[{'name':'Megha','mobile':9744217928},
        {'name':'Ritvik','mobile':9744218219},
       ]
x=mycol.insert_many(list1)

print(x.inserted_ids)
for y in mycol.find():
    print(y)
    