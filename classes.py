class User:
    def __init__(self):
      self.nickname = 'sampleNickname'
      self.city = 'sampleCity'

    def introduce(self):
      print('Hello I am', self.nickname, 'and I live in', self.city)   

sample_user = User()
sample_user.introduce()