import pytest
from cardlib import *
from pokerhandlib import *


def test_jackcard_get_value():
    card = JackCard(Suit.hearts)
    assert card.get_value() == 11


def test_full_house():

    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = PokerHand.full_house(he)
    print('full house: {}'.format(a))


def test_high_card():
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
    a = PokerHand.one_pair(he)
    print('One Pair: {} '.format(a))


def test_two_pair():
    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = PokerHand.two_pair(he)
    print('Two Pair: {} '.format(a))


def test_three_of_a_kind():
    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = PokerHand.three_of_a_kind(he)
    print('Three of a kind: {} '.format(a))


def test_flush():
    he = Hand()
    he.add_card(NumberedCard(9, Suit.clubs))
    he.add_card(NumberedCard(8, Suit.clubs))
    he.add_card(NumberedCard(7, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(5, Suit.clubs))
    a = PokerHand.straight(he)
    print('Flush: {} '.format(a))


