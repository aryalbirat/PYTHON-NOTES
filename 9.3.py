varList = [12,34,67,89,0,1,2,3,4]

def normalFunction():
    for var in varList:
        yield var
  

print("MainList: ",varList)

print("Normal Function TEST")
value = normalFunction()
print(type(value))
print(value)



def check():
    yield 10
    yield 20
    yield "PYTHON"
print(list(check()))
