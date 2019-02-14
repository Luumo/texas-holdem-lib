from enum import Enum
import random


class Suit(Enum):
    # enumerates all 4 suits

    spades = 1
    hearts = 2
    diamonds = 3
    clubs = 4

    def __str__(self):
        return self.name


class CardValue(Enum):
    # Enumerates all 13 card values

    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

    def __str__(self):
        if 1 < self.value <= 10:
            return str(self.value)
        return self.name


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    # init 52 card deck
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for card_value in CardValue:
                self.cards.append(Card(card_value, suit))

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

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return "{}".format(self.cards)


d = Deck()
d.print_deck()

h = Hand()
h.add_card(d.pop_card())
d.print_deck()
print(h)
