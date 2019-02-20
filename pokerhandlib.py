from collections import Counter     # Counter is convenient for counting objects (a specialized dictionary)


class PokerHand:
    def __init__(self, cards):
        self.cards = cards

    def __lt__(self, other):
        pass


    def high_card(self):
        # returns the highest valued card
        vals = []
        for c in self.cards:
            vals.append(c.get_value())
        vals.sort()
        return vals[-1]

    def one_pair(self):
        value_count = Counter()
        # finds the card ranks which are in one pair
        # only returns pairs if 1 pair. else none
        for c in self.cards:
            value_count[c.get_value()] += 1
        pairs = [v[0] for v in value_count.items() if v[1] == 2]
        if len(pairs) == 1:
            return pairs

    def two_pair(self):
        value_count = Counter()
        for c in self.cards:
            value_count[c.get_value()] += 1
        pairs = [v[0] for v in value_count.items() if v[1] == 2]
        if len(pairs) == 2:
            return pairs

    def three_of_a_kind(self):
        value_count = Counter()
        for c in self.cards:
            value_count[c.get_value()] += 1
        threes = [v[0] for v in value_count.items() if v[1] == 3]
        if len(threes) == 1:
            return threes

    def straight(self):
        vals = [c.get_value() for c in self.cards] \
            + [(1, c.suit) for c in self.cards if c.get_value() == 14]  # Add the aces!
        for c in reversed(self.cards):    # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.get_value() - k) not in vals:
                    found_straight = False
                    break
            if found_straight:
                return c.get_value()

    def flush(self):
        # Doesn't care about value, so it might be a straight flush
        # However, in the comparison of best_pokerhand(),
        # the straight_flush will be compared before flush
        suits = []
        for c in self.cards:
            suits.append(c.suit)
        # Only suits matter in flush, checks if all suits are the same
        if all(s == suits[0] for s in suits):
            return suits[0].get_unicode()


    def full_house(self):
        """
        Checks for the best full house in a list of cards (may be more than just 5)

        :param self: A list of playing cards
        :return: None if no full house is found, else a tuple of the values of the triple and pair.
        """
        value_count = Counter()
        for c in self.cards:
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

    def four_of_a_kind(self):
        value_count = Counter()
        for c in self.cards:
            value_count[c.get_value()] += 1
        fours = [v[0] for v in value_count.items() if v[1] == 4]
        if len(fours) == 1:
            return fours

    def straight_flush(self):
        """
        Checks for the best straight flush in a list of cards (may be more than just 5)

        :param self: A list of playing cards.
        :return: None if no straight flush is found, else the value of the top card.
        """
        vals = [(c.get_value(), c.suit) for c in self.cards] \
            + [(1, c.suit) for c in self.cards if c.get_value() == 14]  # Add the aces!
        for c in reversed(self.cards):    # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.get_value() - k, c.suit) not in vals:
                    found_straight = False
                    break
            if found_straight:
                return c.get_value()

    def hand_ranks(self):
        if self.straight_flush():
            return 9
        if self.four_of_a_kind():
            return 8
        if self.full_house():
            return 7
        if self.flush():
            return 6
        if self.straight():
            return 5
        if self.three_of_a_kind():
            return 4
        if self.two_pair():
            return 3
        if self.one_pair():
            return 2
        if self.high_card():
            return 1


# -------Poker Hand Ranks -------- #
    # Straight Flush    9
    # Four of a kind    8
    # Full House        7
    # Flush             6
    # Straight          5
    # Three of a kind   4
    # Two pair          3
    # Pair              2
    # High card         1


