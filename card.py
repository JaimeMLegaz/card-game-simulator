class Card:
    def __init__(self, name, hp, attack, speed, charisma, ability=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.charisma = charisma
        self.ability = ability
        self.tapped = False
        self.counter = speed  # Counter for scoring
        self.owner = None

    def __str__(self):
        return f"{self.name}: ({self.attack}, {self.hp}, {self.speed}, {self.charisma})"

    def __repr__(self):
        return str(self)

    def destroy(self, game):
        # Remove the creature from play
        self.owner.creatures.remove(self)
        # Add the creature to the owner's graveyard
        self.owner.graveyard.append(self)
        # Check for "on death" abilities
        if "On death:" in self.ability:
            # For now, we'll just print the ability
            print(self.ability)