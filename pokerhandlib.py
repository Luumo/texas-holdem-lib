from collections import Counter     # Counter is convenient for counting objects (a specialized dictionary)
from enum import Enum


class Rank(Enum):
    """
    Rank of poker hands, ascending order
    """
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
    # returns the highest valued card
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
            else the card value of the threee of a kind
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
