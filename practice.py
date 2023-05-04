
###TEST***

# if __name__ == "__main__":

class Pokemon():
    generation = "base"

    def __init__ (self, name, start_hp, energy_type, weakness, moves):
        self.name = name
        self.hp = start_hp
        self.energy_type = energy_type
        self.weakness = weakness
        self.moves = moves

    def take_damage(self, damage_amount):
        self.hp = self.hp - damage_amount

    # def take_damage(self, damage_amount, energy_type, resist_amount):
    #         if self.weakness[0] == poke(energy_type):
    #              self.hp = self.hp - (damage_amount*2)

#     #         elif self.resistence[0] == insert(energy_type):
#     #             self.hp = (self.hp + resist_amount) - damage_amount

#             elif self.hp : self.hp - damage_amount
                                 
    def __str__(self):
        if self.hp > 0:
             return f"Pokemon: {self.name} with {self.hp} HP left"
        elif self.hp <= 0:
             return f"Pokemon: {self.name} has fainted"     

poliwag = Pokemon('Poliwag', 60, 'water', 'grass', ('Water Gun', 30))
bulbasaur = Pokemon('Bulbasaur', 90, 'grass', 'fire', ('Vine Whip', 40))

# deck1 = [
#      'Poliwag' = ('Poliwag', 60, 'water', 'grass', ('none', 0), ('Water Gun', 30)),
#      'Bulbasaur' = ('Bulbasaur', 90, 'grass', 'fire', ('water', 10), ('Vine Whip', 40))
# ]

# deck2(Pokemon) = [
#     ('Mareep', 40, 'electric', 'fighting', ('none', 0), ('Thunder Shock', 10)),
#     ('Abra', 30, 'psychic', 'psychic', ('none', 0), ('Psyshock', 10))
# ]

def battle (poke1, poke2):
     while poke1.hp > 0 and poke2.hp > 0:
        poke1.take_damage(poke2.moves[1])
        poke2.take_damage(poke1.moves[1])
#         #break#

     print(poke1)
     print(poke2)

battle(poliwag, bulbasaur)