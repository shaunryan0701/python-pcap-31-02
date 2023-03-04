import random

class Deck:
    suits = ['hearts', 'diamonds', 'clubs','spades']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self):
        self.cards = []   
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) == 0:
            return None
        
        last_card = self.cards[-1]
        self.cards.pop()
        return last_card

    def count_remaining(self):
        return len(self.deck)   

    def get_remaining(self):
        for card in self.cards:
            print(card.present())

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def present(self):
        return(f'{self.value} of {self.suit}')
        

new_deck = Deck()
new_deck.shuffle()
print('    ***** Shuffled ******')
new_deck.get_remaining()
print("    ***** Dealing ******")
my_card = new_deck.deal()
print(my_card.present())
my_card = new_deck.deal()
print(my_card.present())
my_card = new_deck.deal()
print(my_card.present())
my_card = new_deck.deal()
print(my_card.present())
print(len(new_deck.cards))