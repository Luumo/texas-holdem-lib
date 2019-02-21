from enum import Enum
import random
from abc import *
from pokerhandlib import *


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
        return self.get_value() < other.get_value()

    def __eq__(self, other):
        return (self.get_value(), self.suit) == (other.get_value(), other.suit)


class NumberedCard(PlayingCard):

    def __init__(self, value, suit):
        super().__init__(suit)
        self.value = value

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def __str__(self):
        return '{}'.format(self.value) + self.suit.get_unicode()


class JackCard(PlayingCard):
    def get_value(self):
        return 11

    def get_suit(self):
        return self.suit

    def __str__(self):
        return 'J' + self.suit.get_unicode()


class QueenCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 12

    def get_suit(self):
        return self.suit

    def __str__(self):
        return 'Q' + self.suit.get_unicode()


class KingCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 13

    def get_suit(self):
        return self.suit

    def __str__(self):
        return 'K' + self.suit.get_unicode()


class AceCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 14

    def get_suit(self):
        return self.suit

    def __str__(self):
        return 'A' + self.suit.get_unicode()


class StandardDeck:
    def __init__(self):
        self.deck = []
        # create all 52 cards
        for suit in Suit:
            for value in range(2, 11):
                self.deck.append(NumberedCard(value, suit))
            self.deck.append(JackCard(suit))
            self.deck.append(QueenCard(suit))
            self.deck.append(KingCard(suit))
            self.deck.append(AceCard(suit))

    def __str__(self):
        return 'Deck: ' + '(' + ', '.join([str(c) for c in self.deck]) + ')'

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def pop_card(self):
        return self.deck.pop()


class Hand:
    '''fgfh'''
    def __init__(self):
        self.cards = []

    def __str__(self):
        return 'Hand:' + '(' + ', '.join([str(c) for c in self.cards]) + ')'

    def best_poker_hand(self, table_cards=[]):
        return PokerHand(self.cards + table_cards)

    def add_card(self, card: PlayingCard):
        self.cards.append(card)

    def drop_cards(self):
        self.cards.clear()

    def sort_cards(self):
        self.cards.sort()


class PokerHand:
    def __init__(self, cards: list):
        self.pokertype = None
        self.high_values = None

        # list of poker hand functions
        checks = (high_card, one_pair, two_pair, three_of_a_kind, straight, flush,
                  full_house, four_of_a_kind, straight_flush)

        # Loops through best hand -> worst hand.
        for f, pt in reversed(zip(checks, Rank)):
            found = f(cards)
            # if poker hand found, add high value and the pokerhand type to self
            if found is not None:
                self.high_values = found
                self.pokertype = pt
                break

    def __lt__(self, other):
        pass




