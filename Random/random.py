from enum import Enum

class Hand:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def __add__(self):


class Suits(Enum):


class PlayingCard:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def __NumberedCard__(self, value, suit):
        self.value = value
        self.suit = suit

    def __JackCard__(self, suit):
        self.suit = suit

    def __QueenCard__(self, suit):
        self.suit = suit

    def __KindCard__(self, suit):
        self.suit = suit

    def __AceCard__(self, suit):
        self.suit = suit



class PokerHands:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value


class Deck:
    def __init__(self):
        self.cards = []

    def __add__(self, ):






