'''
Class that reresents a collection of Cards 
in a standard 52 card French-suited Deck
'''

import Cards

import random

class Deck:

    # Define a Deck of cards which holds num of decks
    def __init__(self, num_of_decks=1):
        self.deck = []
        self.AddDecks(num_of_decks)
        
    # Add num of decks to total Deck
    def AddDecks(self, num_of_decks=1):
        for deck_count in range(num_of_decks):
            for suit in range(4):    
                for rank in range(13):
                    self.deck.append(Cards._Cards(rank, suit))
    
    # Shuffle Deck by switching card i with random card j
    def Shuffle(self):
        for i in range(len(self.deck)):
            j = random.randrange(len(self.deck))
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
            
    # Deal single card from Deck.
    # Prints warning if there are no cards left
    def DealOneCard(self):
        try: 
            return self.deck.pop(0)
        except:
            print("There are no more cards left in the deck!")

    # Override length so you can see how many cards are left in the Deck
    def __len__(self):
        return len(self.deck)
    
    # Override string to print cards left in Deck 
    def __str__(self):
        deck_text = ""
        for card in self.deck:
            deck_text += str(card) + "\n"
        return deck_text
