import random
from enum import Enum
from abc import *
from collections import Counter


class Suit(Enum):
    # enumerates all 4 suits
    spades = 1
    hearts = 2
    diamonds = 3
    clubs = 4

    def get_unicode(self):
        # printable nicode for each suit
        if self == Suit.spades:
            return u"\u2660"
        elif self == Suit.hearts:
            return u"\u2665"
        elif self == Suit.diamonds:
            return u"\u2666"
        else:
            return u"\u2663"


class PlayingCard(metaclass=ABCMeta):
    """ Represents playing card"""
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
    """ represents numbered cards"""
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
    """ Represents jack card"""
    def get_value(self):
        return 11

    def get_suit(self):
        return self.suit

    def __str__(self):
        return 'J' + self.suit.get_unicode()


class QueenCard(PlayingCard):
    """ represents queen card"""
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 12

    def get_suit(self):
        return self.suit

    def __str__(self):
        return 'Q' + self.suit.get_unicode()


class KingCard(PlayingCard):
    """Represents king card"""
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 13

    def get_suit(self):
        return self.suit

    def __str__(self):
        return 'K' + self.suit.get_unicode()


class AceCard(PlayingCard):
    """Represents the Ace cards"""
    def __init__(self, suit):
        super().__init__(suit)

    def get_value(self):
        return 14

    def get_suit(self):
        return self.suit

    def __str__(self):
        return 'A' + self.suit.get_unicode()


class StandardDeck:
    """StandardDeck represents deck of cards """
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
        """ randomly shuffles the deck of cards"""
        random.shuffle(self.deck)

    def pop_card(self):
        """ Returns the card on top of the deck, and removes it from deck"""
        return self.deck.pop()


class Hand:
    """ Hand represents the players hand"""
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
    """ PokerHand checks what poker hand rank of the cards """

    def __init__(self, cards: list):
        self.pokertype = None
        self.high_values = None

        # list of poker hand functions
        checks = (straight_flush,  four_of_a_kind, full_house, flush, straight,
                  three_of_a_kind, two_pair, one_pair, high_card)

        # Loops through best hand -> worst hand.
        # for f, pt in reversed(zip(checks, Rank)):
        for f, pt in zip(checks, reversed(Rank)):
            found = f(cards)
            # if poker hand found, add high value and the pokerhand type to self
            if found is not None:
                self.high_values = found
                self.pokertype = pt
                break

    def __lt__(self, other):
        return self.pokertype.value < other.pokertype.value


class Rank(Enum):
    """Rank of poker hands, ascending order"""
    high_card = 1
    pair = 2
    two_pair = 3
    three_of_a_kind = 4
    straight = 5
    flush = 6
    full_house = 7
    four_of_a_kind = 8
    straight_flush = 9


def high_card(cards):
    """
    Checks for highest card in list of cards

    :param cards: A list of playing cards
    :return: The value of highest valued card
    """
    vals = []
    for c in cards:
        vals.append(c.get_value())
    vals.sort()
    return vals[-1]


def one_pair(cards):
    """
    Checks for one pair in list of cards
    :param cards: A list of playing cards
    :return: None if no pair is found, else the card value of the pair
    """
    value_count = Counter()
    # finds the card ranks which are in one pair
    # only returns pairs if 1 pair. else none
    for c in cards:
        value_count[c.get_value()] += 1
    pairs = [v[0] for v in value_count.items() if v[1] == 2]
    if len(pairs) == 1:
        return pairs[0]


def two_pair(cards):
    """
    Checks for two pairs in a list of cards

    :param cards: A list of playing cards
    :return: None if no two pair can be found, else a tuple of the values of the two card pairs
    """
    value_count = Counter()
    for c in cards:
        value_count[c.get_value()] += 1
    pairs = [v[0] for v in value_count.items() if v[1] == 2]
    if len(pairs) == 2:
        return pairs[0], pairs[1]


def three_of_a_kind(cards):
    """
    Checks for three of a kind in a list of cards.

    :param cards: A list of playing cards
    :return: None if no three of a kind is found,
            else the card value of the three of a kind
    """
    value_count = Counter()
    for c in cards:
        value_count[c.get_value()] += 1
    threes = [v[0] for v in value_count.items() if v[1] == 3]
    if len(threes) == 1:
        return threes[0]


def straight(cards):
    """
    Checks for straight in a list of cards.

    :param cards: A list of playing cards
    :return: None if no straight was found, else the value of the highest valued card in the straight
    """
    vals = [c.get_value() for c in cards] \
        + [(1, c.suit) for c in cards if c.get_value() == 14]  # Add the aces!
    for c in reversed(cards):    # Starting point (high card)
        # Check if we have the value - k in the set of cards:
        found_straight = True
        for k in range(1, 5):
            if (c.get_value() - k) not in vals:
                found_straight = False
                break
        if found_straight:
            return c.get_value()


def flush(cards):
    """
    Checks for flush in a list of cards. Doesn't care about value, only suit.


    :param cards: A list of playing cards
    :return: None if no flush is found, else the suit of the flush
    """
    suits = []
    for c in cards:
        suits.append(c.suit)
    # Only suits matter in flush, checks if all suits are the same
    if all(s == suits[0] for s in suits):
        return suits[0].get_unicode()


def full_house(cards):
    """
    Checks for the best full house in a list of cards (may be more than just 5)

    :param cards: A list of playing cards
    :return: None if no full house is found, else a tuple of the values of the triple and pair.
    """
    value_count = Counter()
    for c in cards:
        value_count[c.get_value()] += 1
    # Find the card ranks that have at least three of a kind
    threes = [v[0] for v in value_count.items() if v[1] >= 3]
    threes.sort()
    # Find the card ranks that have at least a pair
    twos = [v[0] for v in value_count.items() if v[1] >= 2]
    twos.sort()

    # Threes are dominant in full house, lets check that value first:
    for three in reversed(threes):
        for two in reversed(twos):
            if two != three:
                return three, two


def four_of_a_kind(cards):
    """
    :param cards: A list of playing cards
    :return: None if no four of a kind is found, else the value of the four of a kind
    """
    value_count = Counter()
    for c in cards:
        value_count[c.get_value()] += 1
        # Find the card ranks that have at least a four of a kind
    fours = [v[0] for v in value_count.items() if v[1] == 4]
    if len(fours) == 1:
        return fours[0]


def straight_flush(cards):
    """
    Checks for the best straight flush in a list of cards (may be more than just 5)

    :param cards: A list of playing cards.
    :return: None if no straight flush is found, else the value of the top card.
    """
    vals = [(c.get_value(), c.suit) for c in cards] \
        + [(1, c.suit) for c in cards if c.get_value() == 14]  # Add the aces!
    for c in reversed(cards):    # Starting point (high card)
        # Check if we have the value - k in the set of cards:
        found_straight = True
        for k in range(1, 5):
            if (c.get_value() - k, c.suit) not in vals:
                found_straight = False
                break
        if found_straight:
            return c.get_value()
