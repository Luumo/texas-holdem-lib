from enum import Enum
import random, math
from abc import *


class Suit(Enum):
    # enumerates all 4 suits
    spades = 1
    hearts = 2
    diamonds = 3
    clubs = 4

    def get_unicode(self):
        if self == Suit.spades:
            return u"\u2660"    # Spades unicode
        elif self == Suit.hearts:
            return u"\u2665"    # Hearts unicode
        elif self == Suit.diamonds:
            return u"\u2666"    # Diamonds unicode
        else:
            return u"\u2663"    # Clubs unicode


class PlayingCard(metaclass=ABCMeta):
    def __init__(self, suit):
        self.suit = suit

    @abstractmethod
    def get_value(self):
        pass

    def __lt__(self, other):
        first_card = (self.get_value(), self.suit)
        second_card = (other.get_value(), other.suit)

        if first_card < second_card:
            return True
        elif first_card > second_card:
            return False

    def __eq__(self, other): # Skulle kunna lägga denna i __lt__
        if (self.get_value(), self.suit) == (other.get_value(), other.suit):
            return True


class NumberedCard(PlayingCard):

    def __init__(self, value, suit):
        super().__init__(suit)
        self.value = value

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit


class JackCard(PlayingCard):
    def get_value(self):
        return 11

    def get_suit(self):
        return self.suit


class QueenCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 12

    def get_suit(self):
        return self.suit


class KingCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 13

    def get_suit(self):
        return self.suit


class AceCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 14

    def get_suit(self):
        return self.suit


class StandardDeck:
    # init 52 card deck
    def __init__(self):
        self.deck = []
        # Create Numbered cards
        for suit in Suit:
            for value in range(2, 11):
                self.deck.append(NumberedCard(value, suit))
            # Create jack cards
            self.deck.append(JackCard(suit))
            # create queen cards
            self.deck.append(QueenCard(suit))
            # create king cards
            self.deck.append(KingCard(suit))
            # create ace cards
            self.deck.append(AceCard(suit))

    def __str__(self):
        s = "Deck: \n"
        for c in self.deck:
            s += '(' + ''.join([str(c.get_value()), str(Suit.get_unicode(c.get_suit()))]) + ')\n'
        return s
        # return 'Deck(' + ', '.join([str(c.get_suit()) for c in self.deck]) + ')'

    def print_deck(self):
        for card in self.deck:
            print(card.get_value(), card.suit.name)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def pop_card(self):
        return self.deck.pop(-1)


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):   # __add__ or __addcard__ ?
        self.cards.append(card)

    def drop_cards(self):
        self.cards.clear()

    def sort_cards(self):
        self.cards.sort()

    def __str__(self):
        for card in self.cards:
            return str((card.get_value(), (Suit.get_unicode(card.get_suit()))))


d = StandardDeck()
print(d)
# d.shuffle_deck()

h = Hand()
h.add_card(d.pop_card())
h.add_card(d.pop_card())
print(d)
print('\n')
print(h)

# c = PlayingCard.__eq__(JackCard(Suit.spades), JackCard(Suit.spades))
# print(c)