import pytest
from cardlib import *
from pokerhandlib import *


def test_jackcard_get_value():
    card = JackCard(Suit.hearts)
    assert card.get_value() == 11


def test_full_house():  ## Creates a hand

    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = PokerHand.full_house(he)
    print('full house: {}'.format(a))


def test_high_Card():

    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = PokerHand.high_card(he)
    print('high card: {} '.format(a))

def test_one_pair():

    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = PokerHand.one_pair(he)
    print('One Pair: {} '.format(a))


