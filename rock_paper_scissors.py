from random import choice

class Player():
    def __init__(self):
        self.score = 0

class HumanPlayer(Player):
    def choose(self):
        while True:
            user_choice = input('Rock, paper or scissors [r/p/s]? ')
            if user_choice in ['r', 'p', 's']:
                return user_choice

class ComputerPlayer(Player):
    def choose(self):
        return choice(['r', 'p', 's'])

class Game:
    round_result = {
        ('r', 'r'): 'tied',
        ('p', 'p'): 'tied',
        ('s', 's'): 'tied',
        ('r', 'p'): 'lost',
        ('r', 's'): 'won',
        ('p', 'r'): 'won',
        ('p', 's'): 'lost',
        ('s', 'p'): 'won',
        ('s', 'r'): 'lost'
    }


    def __init__(self, rounds):
        self.rounds = rounds
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()


    def play(self):

        for _ in range(self.rounds):
          human_choice = self.human_player.choose()
          computer_choice = self.computer_player.choose()
          print('You:', human_choice, ' | Computer:', computer_choice)
          round = (human_choice, computer_choice)
          print('You', self.round_result[round], 'this round!')


print('--- Rock Paper Scissors Game ---')
while True:
    round_count = input('How many rounds would you like to play? ')
    if round_count.isnumeric():
        Game(int(round_count)).play()
        break
