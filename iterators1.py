class Employee:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
e=Employee()
ite=iter(e)

print(next(ite))
print(next(ite))

