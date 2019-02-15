from enum import Enum
import random
from abc import *


class Suit(Enum):
    # enumerates all 4 suits

    spades = 1
    hearts = 2
    diamonds = 3
    clubs = 4


class PlayingCard:
    def __init__(self, suit):
        self.suit = suit

    @abstractmethod
    def get_value(self):
        pass


class NumberedCard(PlayingCard):

    def __init__(self, value, suit):
        super().__init__(suit)
        self.value = value

    def get_value(self):
        return self.value


class JackCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 11


class QueenCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 12


class KingCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 13


class AceCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 14


class Deck:
    # init 52 card deck
    def __init__(self, numbered, jack, queen, king, ace):


    def __str__(self):
        return "{}".format(self.cards)

    def print_deck(self):
        for card in self.cards:
            print(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def pop_card(self):
        popped_card = self.cards.pop()
        return popped_card


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return "{}".format(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def print_hand(self):
        for card in self.cards:
            print(card)


d = Deck(NumberedCard, JackCard, QueenCard, KingCard, AceCard)
# n = NumberedCard
J = JackCard(Suit.spades)
N = NumberedCard(4, Suit.spades)
print(N.get_value())

