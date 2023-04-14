if __name__ = "__main__":
     my_dex = (
         # Name: start_hp, energy_type, weakness, resistence, moves
         'Skarmory', 60, 'metal', 'fire', ('grass', 30), ('Steel Beak', 20),
         'Mareep', 40, 'electric', 'fighting', None, ('Thunder Shock', 10),
         'Chansey', 90, 'colorless', 'fighting', None, ('Bind Wound', 15),
         'Machoke', 80, 'fighting', 'psychic', None, ('Punch', 20),
         'Chikorita', 40, 'grass', 'fire', ('water', 30), ('Double Scratch', 20),
         'Doduo', 50, 'colorless', 'electric', None, ('Fury Attak', 10),
         'Clefable', 70, 'colorless', 'fighting', None, ('Doubleslap', 20),
         'Persian', 70, 'colorless', 'fighting', ('psychic', 30), ('Pounce', 30),
         'Weezing', 80, 'grass', 'psychic', None, ('Misfire', 60)
     )

     rival_dex = (
         'Hitmonchan', 70, 'fighting', 'psychic', None, ('Jab', 20),
         'Meganium', 100, 'grass', 'fire', 'water', ('Posion Poweder', 40),
         'Abra', 30, 'psychic', 'psychic', None, ('Psyshock', 10),
         'Zapdos', 90, 'electric', None, 'fighting', ('Thunder', 60),
         'Butterfree', 70, 'grass', 'fire', None, ('Whirlwind', 20),
         'Ekans', 50, 'grass', 'psychic', None, ('Poison Sting', 10),
         'Porygon', 30, 'colorless', 'fighting', 'psychic', ('Conversion1', 10),
         'Dewgong', 80, 'water', 'electric', None, ('Ice Beam', 30),
         'Feraligator', 120, 'water', 'electric', None, ('Rendering Jaw', 30),
         'Venomoth', 70, 'grass', 'fire', 'fighting', ('Venom Powder', 15)
     )

class Pokemon():
    def __init__(self, name, start_hp, energy_type, weakness, resistence, moves):
        self.name = name
        self.hp = start_hp
        self.energy_type = energy_type
        self.weakness = weakness
        self.resistence = resistence
        self.moves = moves
        pass


class PokeCardDex():
    def __init__(self, json_file_path=None):
        # NOTE: It is important to handle the case where no path is passed in
        # meaning that json_file_path has a value of None.
        pass

    def set_order(self, order):
        pass

    def battle(self, challenger_party):
        while challenger_party.hp > 0 and self.hp > 0:
            self.take_damage(challenger_party.moves[1])
            challenger_party.take_damage(self.moves[1])
        pass

    def heal_party(self):
        pass

    def add_to_party(self, pokemon):
        pass



# Below is an example usage for using the classes
# if __name__ == "__main__":
#     my_dex = PokeCardDex('pokemon_party.json')
#     rival_dex = PokeCardDex()
#     pikachu = Pokemon('Pikachu', 100, 'electric', None, None, (('electric charge', 30),))
#     rival_dex.add_to_party(pikachu)

#     my_dex.battle(rival_dex)

    # for pokemon in my_dex.party:
    #     print(pokemon.is_fainted)

    # my_dex.heal_party()