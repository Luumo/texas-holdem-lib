import pytest
from cardlib import *


def test_JackCard_get_value():
    card = JackCard(Suit.hearts)
    assert card.get_value() == 11

def test_eq():
    card1