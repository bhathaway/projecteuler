# This is a fun problem. We get to characterize a five card hand in the game of Poker.
# Begin by modeling the rank system.

HIGH_CARD = 0
PAIR = 1
TWO_PAIR = 2
THREEE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8

# Realistically, a royal flush is just the highest possible straight flush, so I don't see the point, really.

# The weird card is the ace, whose value is hand dependent. Sometimes an ace is high, sometimes low, but
# never both at the same time. It really only matters in hands that are potentially straights.

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

    def __repr__(self):
        return Card.rank_repr_map[self.rank] + ' of ' + Card.suit_repr_map[self.suit]

class Hand:
    def __init__(self, cards):
        card_list = cards.split()
        assert(len(card_list) == 5)
        self.cards = []
        for card in card_list:
            self.cards.append(Card(card))

    def getHandClass(self):
        consecutive_head = ''
        same_head = ''
        starting_suit = ''

        pair_count = 0
        three_count = 0
        four_count = 0
        same_suit_count = 0

        sorted_cards = self.cards
        sorted_cards.sort()
        for card in sorted_cards
            if consecutive_head = '':
                consecutive_head = 
