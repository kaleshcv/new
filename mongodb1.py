import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["secondmongodb"] # create a db named secondmongodb
mycol=mydb["EmployeeTable"] # create a collection named EmployeeTable
dict={'name':'Kalesh', 'mobile':9744218219}
mycol.insert_one(dict)


#print(type(myclient))
#print(type(mydb))
dblist=myclient.list_database_names() # to list all db names
#print(dblist)