class User:
    def __init__(self):
      self.nickname = 'sampleNickname'
      self.city = 'sampleCity'

    def introduce(self):
      print('Hello I am', self.nickname, 'and I live in', self.city)   

sample_user = User()
sample_user.introduce()

class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
        self.other()

    def other(self):
        print("other")

    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")

obj = Classy()
obj.var = 3
obj.method()

obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()

print(Classy.__name__)
print(type(obj).__name__)

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)