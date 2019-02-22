from cardlib import *
import pytest

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
    cmp = JackCard(Suit.clubs) < QueenCard(Suit.spades)
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


def test_compare_two_poker_hands():
    h1 = [NumberedCard(9, Suit.clubs), NumberedCard(9, Suit.hearts), NumberedCard(9, Suit.spades),
          NumberedCard(9, Suit.diamonds)]
    ph1 = PokerHand(h1)

    h2 = [QueenCard(Suit.clubs), QueenCard(Suit.clubs), NumberedCard(6, Suit.clubs),
          NumberedCard(6, Suit.clubs), NumberedCard(6, Suit.clubs)]
    ph2 = PokerHand(h2)

    assert(ph2 < ph1)


def test_best_poker_hand():
    h = Hand()
    h.add_card(NumberedCard(9, Suit.hearts))
    h.add_card(NumberedCard(9, Suit.clubs))
    other = [NumberedCard(9, Suit.spades), NumberedCard(9, Suit.diamonds)]

    best = Hand.best_poker_hand(h, other)

    assert (best.pokertype == Rank.four_of_a_kind)

def test_cmp_two_best_hands():
    # ---- other cards --- #
    other = [NumberedCard(2, Suit.spades), JackCard(Suit.diamonds)]
    # ---- Hand 1 ----- #
    h = Hand()
    h.add_card(NumberedCard(2, Suit.hearts))
    h.add_card(NumberedCard(2, Suit.clubs))

    ph1 = Hand.best_poker_hand(h, other)
    # --- Hand 2 ---- #
    h = Hand()
    h.add_card(NumberedCard(9, Suit.hearts))
    h.add_card(NumberedCard(9, Suit.clubs))

    ph2 = Hand.best_poker_hand(h, other)
    print('Hand 1 rank: {}, Hand 2 rank: {}, Ph1 wins over Ph2: {}'.format(
        ph1.pokertype.name, ph2.pokertype.name, ph1 > ph2))

    assert(ph1 > ph2)
