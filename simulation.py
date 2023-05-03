# simulation.py
import random
from game import Game
from player import Player
from card_database import cards

deck = cards
deck.extend(deck)
deck.extend(deck)
deck.extend(deck)


random.shuffle(deck)

# Create a new game with 4 players
game = Game([Player() for _ in range(4)], deck)

# Start the game
game.setup()
game.play()

print("END")