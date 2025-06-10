from utils.card import Card
from random import random
from random import shuffle


class Player:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.cards = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history = []


    def play(self) -> Card:
        card = random(self.cards)                               
        self.history.append(card)
        print(f"{self.name} {self.turn_count} played: {card.value} {card.icon}")
        return card
    
    
class Deck:                                                    

    def __init__(self): 
        self.cards = []                                         
      

    def fill_deck(self):                                       
        for icon in range(4):
            for value in range(13):
                self.cards.append(Card(icon, value))
                

    def shuffle(self):             
        shuffle(self.cards)


    def distribute(self, players):
        self.players = []