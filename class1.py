class Employee:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        self.place="cochin"


    def myfunction(self):
        print("Hello ! , My name is"+self.name)
    def empdet(self):
        print("Employee Name : "+self.name)
        print("Employye Id : "+ str(self.id))
        print("Employee city : " + self.place)


e1=Employee('Max',123,30)
e2=Employee("John", 1234, 40)
print(e1.name)
e1.myfunction()
e2.empdet()


