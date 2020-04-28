import platform
import datetime
import json
print(platform.system())
x=dir(platform) #list all the functions
#print(x)

dt=datetime.datetime.now()
print(dt)
print(dt.strftime("%B"))




# some JSON:
js = '{ "name":"John", "age":30, "city":"New York"}'
print(type(js))

# parse x:
y = json.loads(js)
print(y)
print(type(y))

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
