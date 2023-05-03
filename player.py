import random
import names

class Player:
    def __init__(self):
        self.hand = []
        self.creatures = []
        self.graveyard = []
        self.points = 0
        self.name = names.get_full_name()

    def __str__(self):
        return f"{self.name}: Hand {self.hand}, \n" \
               f"Creatures in play: {self.creatures}, \n" \
               f"Graveyard: {self.graveyard}, \n" \
               f"Points: {self.points}\n"

    def draw_card(self, game):
        # Call a function to decide which card to draw
        card_index = self.choose_card_shop(game.shop)
        self.hand.append(game.shop.pop(card_index))

    def choose_card_shop(self, shop):
        # Select a random card from the shop
        return random.randrange(len(shop))

    def choose_card_hand(self):
        return random.randrange(len(self.hand))

    def play_card(self):
        if self.hand:
            index = self.choose_card_hand()
            creature = self.hand[index]
            creature.owner = self
            self.creatures.append(creature)
            del self.hand[index]

    def score(self):
        for creature in self.creatures:
            creature.counter -= 1
            if creature.counter == 0:
                self.points += creature.charisma
                creature.counter = creature.speed  # Reset the counter
