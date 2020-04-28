

f=open("file.csv","r")
#f.write("traing time")
x=f.readline(2)
print(x)
y=f.readlines()
for i in y:
    print(i+"\n")


