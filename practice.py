
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

###TEST***

# if __name__ == "__main__":
#      my_dex = (
#          skarmory = Pokemon('Skarmory', 60, 'metal', 'fire', 'grass', ('Steel Beak', 20))
#          mareep = Pokemon('Mareep', 40, 'electric', 'fighting', None, ('Thunder Shock', 10)),
#          chansey = Pokemon('Chansey', 90, 'colorless', 'fighting', None, ('Bind Wound', 15)),
#          machoe = Pokemon('Machoke', 80, 'fighting', 'psyhic', None, ('Punch', 20)),
#          chikorita = Pokemon('Chikorita', 40, 'grass', 'fire', 'water', ('Double Scratch', 20)),
#          doduo = Pokemon('Doduo', 50, 'colorless', 'electric', None, ('Fury Attak', 10)),
#          clefable = Pokemon('Clefable', 70, 'colorless', 'fighting', None, ('Doubleslap', 20)),
#          persian = Pokemon('Persian', 70, 'colorless', 'fighting', 'psyhic', ('Pounce', 30)),
#          weezing = Pokemon('Weezing', 80, 'grass', 'psyhic', None, ('Misfire', 60))
#      )

#      rival_dex = (
#          hitmonchan = Pokemon('Hitmonchan', 70, 'fighting', 'psychic', None, ('Jab', 20)),
#          meganium = Pokemon('Meganium', 100, 'grass', 'fire', 'water', ('Posion Poweder', 40)),
#          abra = Pokemon('Abra', 30, 'psychic', 'psychic', None, ('Psyshock', 10)),
#          zapdos = Pokemon('Zapdos', 90, 'electric', None, 'fighting', ('Thunder', 60)),
#          butterfree = Pokemon('Butterfree', 70, 'grass', 'fire', None, ('Whirlwind', 20)),
#          ekans = Pokemon('Ekans', 50, 'grass', 'psychic', None, ('Poison Sting', 10)),
#          porygon = Pokemon('Porygon', 30, 'colorless', 'fighting', 'psychic', ('Conversion1', 10)),
#          dewgong = Pokemon('Dewgong', 80, 'water', 'electric', None, ('Ice Beam', 30)),
#          feraligator = Pokemon('Feraligator', 120, 'water', 'electric', None, ('Rendering Jaw', 30)),
#          venomoth = Pokemon('Venomoth', 70, 'grass', 'fire', 'fighting', ('Venom Powder', 15))
#      )

class Pokemon():
    generation = "base"

    def __init__ (self, name, level, start_hp, energy_types, weakness, resistence, moves):
        self.name = name
        self.level = level
        self.hp = start_hp
        self.energy_types = energy_types
        self.weakness = weakness
        self.resistence = resistence
        self.moves = moves

    # def take_damage(self, damage_amount):
    #     self.hp = self.hp - damage_amount

    def take_damage(self, damage_amount, resist_amount):
            self.hp = self.hp - damage_amount + resist_amount
                                 
    def __str__(self):
        return f"Pokemon: {self.name} with {self.hp} HP left"

#              self, name, level, start_hp, energy_types, weakness, resistence, moves
poliwag = Pokemon('Poliwag', 13, 60, 'water', 'grass', ('none', 0), ('Water Gun', 30))
bulbasaur = Pokemon('Bulbasaur', 28, 90, 'grass', 'fire', ('water', 10), ('Star Freeze', 40))

def battle (poke1, poke2):
     while poke1.hp > 0 and poke2.hp > 0:
        poke1.take_damage(poke2.moves[1], poke1.resistence[1])
        poke2.take_damage(poke1.moves[1], poke2.resistence[1])
        
        

     print(poke1)
     print(poke2)

battle(poliwag, bulbasaur)

        