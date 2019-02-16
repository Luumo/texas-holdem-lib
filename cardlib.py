from enum import Enum
import random
from abc import *


class Suit(Enum):
    # enumerates all 4 suits
    spades = 1
    hearts = 2
    diamonds = 3
    clubs = 4

    def get_unicode(self):
        if self.spades:
            return u"\u2660"


class PlayingCard(metaclass=ABCMeta):
    def __init__(self, suit):
        self.suit = suit

    @abstractmethod
    def get_value(self):
        pass

    def __lt__(self, other):
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
        s = "Deck("
        for c in self.deck:
            s += ', '.join([str(c.get_value()), str(c.get_suit())]) + ')\n'
        return s
        # return 'Deck(' + ', '.join([str(c.get_suit()) for c in self.deck]) + ')'

    def print_deck(self):
        for card in self.deck:
            print(card.get_value(), card.suit.name)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def pop_card(self):
        popped_card = self.deck.pop()
        return popped_card


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def print_hand(self):
        for card in self.cards:
            print(card)


d = StandardDeck()
print(d)
# d.print_deck()
d.shuffle_deck()
# d.print_deck()

# h = Hand()
# h.add_card(d.pop_card())
# print('\n')
# h.print_hand()


