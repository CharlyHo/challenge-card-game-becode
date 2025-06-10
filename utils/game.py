from player import Player, Deck
from card import Card
from random import shuffle, random


class Board:
    
    def __init__ (self, players):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_card = []


    def start_game(self):
            deck = Deck()
            deck.fill_deck()
            deck.shuffle()
            deck.distribute_cards(self.players)