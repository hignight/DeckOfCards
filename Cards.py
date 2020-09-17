'''
Class that reresents a single card in a standard 52 card French-suited Deck
'''

class _Cards:

    # Define the ranks and suits that are in a standard deck.
    RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", \
             "10", "Jack", "Queen", "King")
    SUITS = ("Spades", "Diamonds", "Clubs", "Hearts")

    # Initialize card to assigned rank and suit.
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # Override string to print Card in simple English. 
    def __str__(self):
        return "{} of {}".format(self.RANKS[self.rank], self.SUITS[self.suit])
  
