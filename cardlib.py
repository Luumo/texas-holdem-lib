from enum import Enum

# 52 cards consists of:
# Spade x 13
# Heart x 13
# Diamond x 13
# Club x 13


class Suit(Enum):
    # enumerates all 4 suits

    spade = 1
    heart = 2
    diamond = 3
    clubs = 4


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


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "Card is {} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit.__members__.values():
            self.cards.append(suit)

    def __str__(self):
        return "{}".format(self.cards)


d = Deck()
print(d)
