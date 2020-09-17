# Deck of Cards
Simple Deck of Cards implemented in Python

There are two classes connected to this project: Cards and Deck.

## Cards.py 
Cards is a "private" class that only holds the suit and rank of a card and a method for printing what the card is.  It is private as the class can easily be broken at the moment. There is no error handling if you create a card that is not in the standard French suited 52 card deck. 

## Deck.py
Deck is a class that holds Cards.  It is set up to make a 52 card deck with the standard French suits.  You can initialize Deck with no options to get a single 52 card deck or initialize it with an int to get a "shoe" with that many decks in it.  So far it is a very simple class with limited error handling and limited capabilities.  The methods you can call from Deck are:

### AddDecks(num_of_decks = 1)
Adds N decks to the shoe.  The default is 1.

### Shuffle()
Shuffles the cards

### DealOneCard()
Pops the top card off the deck.  Returns None if the deck has no more cards in it

`len` and `str` are overridden so you can see how many cards are left and print the entire deck in a more natural Pythonic way.  

## TestDeck.py
Unit tests for the Deck class.

## TestDeckOfCards.ipynb
Jupyter notebook showing the basics of the Deck class.  
