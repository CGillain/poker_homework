import random

suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)

class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_royal_flush(self):
        self.card_rank = []
        for k in range(5):
            current_rank = self.cards[k].get_rank()
            self.card_rank.append(current_rank)
        self.card_rank = [int(i) for i in self.card_rank]
        self.card_rank.sort()
        if (self.card_rank[4] - self.card_rank[3] == 1) and (self.card_rank[3] - self.card_rank[2] == 1) and (
                self.card_rank[2] - self.card_rank[1] == 1) and (self.card_rank[1] - self.card_rank[0] == 1) and (
                min(self.card_rank) == 10):
            for k in range(5):
                for l in range(k + 1, 5):
                    for m in range(l + 1, 5):
                        for i in range(m + 1, 5):
                            for j in range(i + 1, 5):
                                if self.cards[k].get_suit() == self.cards[l].get_suit() == self.cards[m].get_suit() == \
                                        self.cards[i].get_suit() == self.cards[j].get_suit():
                                    return True
        else:
            return False

    def is_straight_flush(self):
        self.card_rank = []
        for k in range(5):
            current_rank = self.cards[k].get_rank()
            self.card_rank.append(current_rank)
        self.card_rank = [int(i) for i in self.card_rank]
        self.card_rank.sort()
        if ((self.card_rank[4] - self.card_rank[3] == 1) and (self.card_rank[3] - self.card_rank[2] == 1) and (
                self.card_rank[2] - self.card_rank[1] == 1) and (self.card_rank[1] - self.card_rank[0] == 1) and (
                    min(self.card_rank) != 10)) or (
                self.card_rank[4] == 14 and self.card_rank[3] == 5 and self.card_rank[2] == 4 and self.card_rank[1] == 3 and self.card_rank[0] == 2):
            for k in range(5):
                for l in range(k + 1, 5):
                    for m in range(l + 1, 5):
                        for i in range(m + 1, 5):
                            for j in range(i + 1, 5):
                                if self.cards[k].get_suit() == self.cards[l].get_suit() == self.cards[m].get_suit() == \
                                        self.cards[i].get_suit() == self.cards[j].get_suit():
                                    return True
        else:
            return False

    def is_flush(self):
        for k in range(5):
            for l in range(k + 1, 5):
                for m in range(l + 1, 5):
                    for i in range(m + 1, 5):
                        for j in range(i + 1, 5):
                            if self.cards[k].get_suit() == self.cards[l].get_suit() == self.cards[m].get_suit() == \
                                    self.cards[i].get_suit() == self.cards[j].get_suit():
                                return True
                            else:
                                return False

    def is_straight(self):
        self.card_rank = []
        for k in range(5):
            current_rank = self.cards[k].get_rank()
            self.card_rank.append(current_rank)
        self.card_rank = [int(i) for i in self.card_rank]
        self.card_rank.sort()
        if ((self.card_rank[4] - self.card_rank[3] == 1) and (self.card_rank[3] - self.card_rank[2] == 1) and (
                self.card_rank[2] - self.card_rank[1] == 1) and (self.card_rank[1] - self.card_rank[0] == 1) and (
                min(self.card_rank) != 10)) or (self.card_rank[4] == 14 and self.card_rank[3] == 5 and self.card_rank[2] == 4 and self.card_rank[1] == 3 and self.card_rank[0] == 2):
            return True
        else:
            return False

    def is_four_same(self):
        for k in range(5):
            for l in range(k + 1, 5):
                for m in range(k + 2, 5):
                    for n in range(k + 3, 5):
                        if self.cards[k].get_rank() == self.cards[l].get_rank() == self.cards[m].get_rank() == \
                                self.cards[n].get_rank():
                            return True
                        else:
                            return False

    def is_full_house(self):
        for k in range(5):
            for l in range(k + 1, 5):
                for m in range(l + 1, 5):
                    for i in range(m + 1, 5):
                        for j in range(i + 1, 5):
                            if self.cards[k].get_rank() == self.cards[l].get_rank() == self.cards[m].get_rank() and \
                                    self.cards[i].get_rank() == self.cards[j].get_rank():
                                return True
                            else:
                                return False

    def is_three_same(self):
        for k in range(5):
            for l in range(k + 1, 5):
                for m in range(l + 1, 5):
                    for i in range(m + 1, 5):
                        for j in range(i + 1, 5):
                            if self.cards[k].get_rank() == self.cards[l].get_rank() == self.cards[m].get_rank() and (
                                    self.cards[i].get_rank() != self.cards[j].get_rank()) and (
                                    self.cards[i].get_rank() != self.cards[k].get_rank()):
                                return True
                            else:
                                return False

    def is_two_pairs(self):
        nbr_pairs = 0
        for k in range(5):
            for l in range(k + 1, 5):
                if self.cards[k].get_rank() == self.cards[l].get_rank():
                    nbr_pairs += 1

        if nbr_pairs == 2:
            return True
        else:
            return False

    def is_one_pair(self):
        nbr_pairs = 0
        for k in range(5):
            for l in range(k + 1, 5):
                if self.cards[k].get_rank() == self.cards[l].get_rank():
                    nbr_pairs += 1

        if nbr_pairs == 1:
            return True
        else:
            return False


def check_hand():
    n = 10000  # Number of times we want to run poker hands
    nothing = 0
    one_pair = 0
    two_pairs = 0
    three_same = 0
    full_house = 0
    four_same = 0
    straight = 0
    straight_flush = 0
    flush = 0
    royal_flush = 0

    for i in range(n):
        new_deck = Deck()
        new_deck.shuffle()
        hand = Hand(new_deck)
        # print(hand)

        if hand.is_one_pair():
            one_pair += 1

        elif hand.is_two_pairs():
            two_pairs += 1

        elif hand.is_three_same():
            three_same += 1

        elif hand.is_straight():
            straight += 1

        elif hand.is_flush():
            flush += 1

        elif hand.is_full_house():
            full_house += 1

        elif hand.is_four_same():
            four_same += 1

        elif hand.is_straight_flush():
            straight_flush += 1

        elif hand.is_royal_flush():
            royal_flush += 1

        else:
            nothing += 1

    total = one_pair + two_pairs + three_same + straight + flush + full_house + four_same + straight_flush + royal_flush + nothing

    print("Got Nothing", nothing, "times.")
    print("Got one pair", one_pair, "times.")
    print("Got two pairs", two_pairs, "times.")
    print("Got three cards of the same kind", three_same, "times.")
    print("Got full house", full_house, "times.")
    print("Got four of the same kind", four_same, "times.")
    print("Got straight", straight, "times.")
    print("Got straight flush", straight_flush, "times.")
    print("Got flush", flush, "times.")
    print("Got royal flush", royal_flush, "times.")
    # print("Total", total)

    print("Probability of getting nothing is", ((nothing*100)/n))
    print("Probability of getting 1 pair is", ((one_pair*100)/n))
    print("Probability of getting 2 pairs is", ((two_pairs * 100) / n))
    print("Probability of getting 3 cards of the same kind is", ((three_same*100)/n))
    print("Probability of getting a full house is", ((full_house * 100) / n))
    print("Probability of getting a four of the same kind is", ((four_same * 100) / n))
    print("Probability of getting a straight is", ((straight * 100) / n))
    print("Probability of getting a straight flush is", ((straight_flush * 100) / n))
    print("Probability of getting a flush is", ((flush * 100) / n))
    print("Probability of getting a royal flush is", ((royal_flush * 100) / n))


check_hand()