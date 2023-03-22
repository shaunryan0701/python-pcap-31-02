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

obj = Classy()
obj.var = 3
obj.method()