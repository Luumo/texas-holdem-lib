import pytest
from cardlib import *


def test_deck():
    d = StandardDeck()
    print(d)
    d.shuffle_deck()
    print('Shuffled deck: {}:'.format(d))


def test_pop_card_from_deck_to_hand():
    d = StandardDeck()
    h = Hand()
    h.add_card(d.pop_card())
    h.add_card(d.pop_card())
    print('Hand with two cards from unshuffled deck: {}'.format(h))


def test_compare_cards():
    cmp = QueenCard(Suit.clubs) < QueenCard(Suit.spades)
    print(cmp)


def test_full_house():

    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = full_house(he.cards)
    print('full house: {}'.format(a))


def test_high_card():
    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = high_card(he.cards)
    print('high card: {} '.format(a))


def test_one_pair():
    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = one_pair(he.cards)
    print('One Pair: {} '.format(a))


def test_two_pair():
    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = two_pair(he.cards)
    print('Two Pair: {} '.format(a))


def test_three_of_a_kind():
    he = Hand()
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(QueenCard(Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    a = three_of_a_kind(he.cards)
    print('Three of a kind: {} '.format(a))


def test_straight_flush():
    he = Hand()
    he.add_card(NumberedCard(9, Suit.clubs))
    he.add_card(NumberedCard(8, Suit.clubs))
    he.add_card(NumberedCard(7, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(5, Suit.clubs))
    a = straight_flush(he.cards)
    print('Straight Flush: {} '.format(a))


def test_flush():
    he = Hand()
    he.add_card(NumberedCard(9, Suit.clubs))
    he.add_card(NumberedCard(8, Suit.clubs))
    he.add_card(NumberedCard(7, Suit.clubs))
    he.add_card(NumberedCard(6, Suit.clubs))
    he.add_card(NumberedCard(5, Suit.clubs))
    a = flush(he.cards)
    print('Flush: {} '.format(a))


def test_four_of_a_kind():
    he = (NumberedCard(9, Suit.hearts), NumberedCard(9, Suit.hearts),
          NumberedCard(9, Suit.hearts), NumberedCard(9, Suit.hearts))
    a = four_of_a_kind(he)
    print('Four of a kind: {} '.format(a))


def test_poker_hand():


def test_poker_hand_real():
    he = (NumberedCard(9, Suit.hearts), NumberedCard(9, Suit.hearts),
          NumberedCard(9, Suit.hearts), NumberedCard(9, Suit.hearts))
    ph = PokerHand(he)
    print(ph.pokertype, ph.high_values)
    assert(ph.pokertype == Rank.four_of_a_kind)


