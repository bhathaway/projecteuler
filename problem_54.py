# This is a fun problem. We get to characterize a five card hand in the game of Poker.
# Begin by modeling the rank system.

HIGH_CARD = 0
PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8

class PokerHandCategory:
    enum_to_string =\
      { HIGH_CARD : "high card", PAIR : "pair", TWO_PAIR : "two pair",\
        THREE_OF_A_KIND : "three of a kind", STRAIGHT : "straight", \
        FLUSH : "flush", FULL_HOUSE : "full house", FOUR_OF_A_KIND : "four of a kind",\
        STRAIGHT_FLUSH : "straight flush" }

    def __init__(self, e):
        self.category = e

    def __repr__(self):
        return PokerHandCategory.enum_to_string[self.category]

# Realistically, a royal flush is just the highest possible straight flush, so I don't see the point, really.

# Here is the encoding of the cards. Rank = 2, 3, ... J, Q, K, A.
# Suit = S, C, D, H

# Maybe an easy first step would be to correctly identify a hand.

class Card:
    rank_repr_map = {'2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight',
                     '9':'nine', 'T':'ten', 'J':'jack', 'Q':'queen', 'K':'king', 'A':'ace'}
    suit_repr_map = {'S':'spades', 'C':'clubs', 'D':'diamonds', 'H':'hearts'}

    def __init__(self, card):
        self.rank = card[0]
        self.suit = card[1]
        assert self.rank in Card.rank_repr_map
        assert self.suit in Card.suit_repr_map
        if self.rank <= '9' and self.rank >= '2':
            self.functional_rank = ord(self.rank) - ord('2')
        elif self.rank == 'T':
            self.functional_rank = 8
        elif self.rank == 'J':
            self.functional_rank = 9
        elif self.rank == 'Q':
            self.functional_rank = 10
        elif self.rank == 'K':
            self.functional_rank = 11
        elif self.rank == 'A':
            self.functional_rank = 12
        else:
            assert false

    def __lt__(self, other_card):
        return self.functional_rank < other_card.functional_rank

    def __eq__(self, other_card):
        return self.functional_rank == other_card.functional_rank

    def __repr__(self):
        return Card.rank_repr_map[self.rank] + ' of ' + Card.suit_repr_map[self.suit]

class Hand:
    def __init__(self, cards):
        card_list = cards.split()
        assert(len(card_list) == 5)
        self.cards = []
        for card in card_list:
            self.cards.append(Card(card))
        self.cards.sort()

        # Depends on sorted cards
        self.groups = self.sameValueLists()

        # Depends on groups being determined and cards sorted
        self.category = self.findCategory()

    def sameValueLists(self):
        return_list = []
        same_card_list = []
        for card in self.cards:
            if len(same_card_list) == 0:
                same_card_list.append(card)
            elif same_card_list[-1].functional_rank == card.functional_rank:
                same_card_list.append(card)
            else:
                return_list.append(same_card_list)
                same_card_list = [card]
        return_list.append(same_card_list)

        # As a last step and courtesy to downstream algorthims, sort by list size,
        # then by rank.
        return_list.sort(lambda x,y: cmp(len(x), len(y)), reverse=True)

        # Get the pivots.
        pivots = []
        current_length = len(return_list[0])
        for i in range(len(return_list)):
            length = len(return_list[i])
            if length != current_length:
                pivots.append(i)
                current_length = length

        final_list = []
        p = 0
        for k in pivots:
            tmp_list = return_list[p:k]
            tmp_list.sort(lambda x, y: cmp(x[0], y[0]), reverse=True)
            final_list += tmp_list
            p = k
        tmp_list = return_list[p:len(return_list)]
        tmp_list.sort(lambda x, y: cmp(x[0], y[0]), reverse=True)
        final_list += tmp_list
        return final_list

    def haveStraight(self):
        return self.cards[4].functional_rank == self.cards[3].functional_rank + 1 and\
               self.cards[3].functional_rank == self.cards[2].functional_rank + 1 and\
               self.cards[2].functional_rank == self.cards[1].functional_rank + 1 and\
               self.cards[1].functional_rank == self.cards[0].functional_rank + 1
    def haveFlush(self):
        return self.cards[0].suit == self.cards[1].suit and\
               self.cards[1].suit == self.cards[2].suit and\
               self.cards[2].suit == self.cards[3].suit and\
               self.cards[3].suit == self.cards[4].suit

    def findCategory(self):
        if len(self.groups[0]) == 4:
            return PokerHandCategory(FOUR_OF_A_KIND)
        elif len(self.groups[0]) == 3:
            if len(self.groups) == 2:
                return PokerHandCategory(FULL_HOUSE)
            else:
                return PokerHandCategory(THREE_OF_A_KIND)
        elif len(self.groups[0]) == 2:
            if len(self.groups) == 3:
                return PokerHandCategory(TWO_PAIR)
            else:
                return PokerHandCategory(PAIR)
        else:
            if self.haveFlush():
                if self.haveStraight():
                    return PokerHandCategory(STRAIGHT_FLUSH)
                else:
                    return PokerHandCategory(FLUSH)
            elif self.haveStraight():
                return PokerHandCategory(STRAIGHT)
            else:
                return PokerHandCategory(HIGH_CARD)

    def wins(self, contending_hand):
        if self.category.category > contending_hand.category.category:
            return True
        elif self.category.category < contending_hand.category.category:
            return False
        else:
            # Now the tricky part..
            if self.category.category == HIGH_CARD or self.category.category == FLUSH or\
               self.category.category == STRAIGHT or self.category.category == STRAIGHT_FLUSH:
                return self.cards[4].functional_rank > contending_hand.cards[4].functional_rank
            # The rest of the cases should be treated the same.
            else:
                for i in range( min(len(self.groups), len(contending_hand.groups)) ):
                    if len(self.groups[i]) > len(contending_hand.groups[i]):
                        return True
                    elif len(self.groups[i]) < len(contending_hand.groups[i]):
                        return False
                    elif self.groups[i][0] > contending_hand.groups[i][0]:
                        return True
                    elif self.groups[i][0] < contending_hand.groups[i][0]:
                        return False
                return False

test_file = open('p054_poker.txt', 'r')
player_one_wins = 0
for raw_line in test_file:
    line = raw_line.rstrip('\n')
    p1_hand = Hand(line[0:15])
    p2_hand = Hand(line[15:])
    if p1_hand.wins(p2_hand):
        player_one_wins += 1

print(player_one_wins)

