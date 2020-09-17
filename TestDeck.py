''' Unit test all the methods in the Deck class '''

import unittest

import Deck

class TestDeck(unittest.TestCase):

    # Test default initializer of deck works
    def test_single_deck_size(self):
        deck = Deck.Deck()
        self.assertEqual(len(deck), 52,
                         "Should be 52 cards in a single deck")

    # Test initializer with more than one deck
    def test_four_deck_size(self):
        deck = Deck.Deck(4)
        self.assertEqual(len(deck), 208,
                         "Should be 208 cards in four decks")

    # Extra test of AddDecks
    # Mostly redundant as init calls AddDecks
    def test_add_deck_size(self):
        deck = Deck.Deck()
        deck.AddDecks(3)
        self.assertEqual(len(deck), 208, 
                         "Should be 208 cards in four decks")

    # Test DealOnCard returns a card 
    def test_deal_one_card(self):
        deck = Deck.Deck()
        card = deck.DealOneCard()
        self.assertIsNotNone(card, "Should be a card, not None")

    # Test that if too many cards are dealt, the returned card is None
    def test_deal_too_many_cards(self):
        deck = Deck.Deck()
        for cards_dealt in range(len(deck) + 1):
            card = deck.DealOneCard()
        self.assertIsNone(card, "Should return None is there are no cards left")

    # Test the Shuffle returns different ordering of cards
    def test_shuffle_deck(self):
        deck = Deck.Deck()
        deck_before_shuffle = str(deck)
        deck.Shuffle()
        deck_after_shuffle = str(deck)
        self.assertNotEqual(deck_before_shuffle, deck_after_shuffle)
        
        
if __name__ == "__main__":
    unittest.main()
