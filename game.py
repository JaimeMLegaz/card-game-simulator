import random


class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.discard_pile = []
        self.shop = []
        self.turn = 0

    def setup(self):
        print(len(self.deck))
        # Each player draws 4 cards
        for player in self.players:
            for _ in range(4):
                player.hand.append(self.deck.pop())
        # Reveal the top 8 cards of the deck to form the Shop
        self.refresh_shop()
        print(len(self.deck))

    def refresh_shop(self):
        for _ in range(8):
            if self.deck:
                self.shop.append(self.deck.pop())
            else:
                if self.discard_pile:
                    self.deck = self.discard_pile
                    self.shop.append(self.deck.pop())
                else:
                    break

    def player_choice(self, player):
        actions = ['reroll']
        # Check conditions for each action
        if self.shop:
            actions.append('draw')
        if player.hand:
            actions.append('play')
        if [creature for creature in player.creatures if not creature.tapped] and any([opponent.creatures for opponent in self.players if opponent != player]):
            actions.append('attack')

        if actions:
            # Randomly choose an action
            action = random.choice(actions)
            if action == 'draw':
                print("DRAW -- ", len(self.shop))
                player.draw_card(self)
            elif action == 'play':
                print("PLAY -- ", len(player.hand))
                player.play_card()
            elif action == 'attack':
                print("ATTACK")
                # Randomly choose an untapped creature to attack with
                attacker = random.choice([creature for creature in player.creatures if not creature.tapped])
                attacker.tapped = True
                # Randomly choose an opponent's creature to attack
                opponent = random.choice([opponent for opponent in self.players if opponent != player and opponent.creatures])
                target = random.choice(opponent.creatures)
                # Perform the attack
                target.hp -= attacker.attack
                if target.hp <= 0:
                    opponent.graveyard.append(target)
                    opponent.creatures.remove(target)
            elif action == 'reroll':
                print("REROLL")
                # Move the current Shop cards to the discard pile and refresh the Shop
                self.discard_pile.extend(self.shop)
                self.shop.clear()
                self.refresh_shop()

    def play(self):
        while not self.check_end():
            current_player = self.players[self.turn % len(self.players)]
            current_player.score()  # Score points at the start of the turn
            for _ in range(2):
                print("\n\n\nTurn of player ", current_player)
                self.player_choice(current_player)
            self.turn += 1

        for player in self.players:
            print(player)


    def check_end(self):
        for player in self.players:
            if player.points >= 25:
                return True
        return False


