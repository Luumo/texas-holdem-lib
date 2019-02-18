import pytest
from cardlib import *
from full_house_straight_flush import *


def test_jackcard_get_value():
    card = JackCard(Suit.hearts)
    assert card.get_value() == 11


def test_full_house():  ## Pre-

    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(5, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = PokerHand.check_full_house(he)
    print(a)



