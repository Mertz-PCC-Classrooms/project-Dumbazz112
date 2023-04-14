
##"Class" Function ###
# class Pokemon():
#     generation = 1

#     def __init__ (self, name, level):
#         self.name = name
#         self.level = level

#     def print_choice(self):
#         print(f"I choose you {self.name}!")

#     def __str__(self):
#         return f"Pokemon: {self.name}"

# pikachu = Pokemon('pikachu', 10)
# bulbasaur = Pokemon('bulbasaur', 12)

# pikachu.print_choice()
# print(bulbasaur)

###"instance" class ### ***BATTLE NOTES***

class Pokemon():
    generation = "base"

    def __init__ (self, name, level, start_hp, energy_types, weakness, resistence, moves):
        self.name = name
        self.level = level
        self.hp = start_hp
        self.energy_types = energy_types
        self.resistence = resistence
        self.weakness = weakness
        self.moves = moves

    def take_damage(self, damage_amount):
        self.hp = self.hp - damage_amount

                                 
    def __str__(self):
        return f"Pokemon: {self.name} with {self.hp} HP left"

poliwag = Pokemon('Poliwag', 13, 60, 'water', None, None, ('Water Gun', 30))
starmie = Pokemon('Starmie', 28, 90, 'psychic', None, None, ('Star Freeze', 40))

def battle (poke1, poke2):
     while poke1.hp > 0 and poke2.hp > 0:
        poke1.take_damage(poke2.moves[1])
        poke2.take_damage(poke1.moves[1])

     print(poke1)
     print(poke2)

battle(poliwag, starmie)