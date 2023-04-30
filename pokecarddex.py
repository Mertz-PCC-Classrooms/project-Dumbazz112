if __name__ == "__main__":
    class Pokemon():
        def __init__(self, name, start_hp, energy_type, weakness, resistence, moves):
            self.name = name
            self.hp = start_hp
            self.start_hp = start_hp
            self.energy_type = energy_type
            self.weakness = weakness
            self.resistence = resistence
            self.moves = moves
            self.is_fainted = False
            pass

        # def take_damage(self, damage_amount):
        #     self.hp = self.hp - (damage_amount * 2(weakness) - resist_amount)


                # if self.weakness[0] == #$insert(energy_type):
                #      self.hp = self.hp - (damage_amount*2) - resist_amount

                # # elif self.resistence[0] == #$insert(energy_type):
                #     self.hp = (self.hp + resist_amount) - damage_amount

                # elif self.hp = self.hp - damage_amount

    #     my_dex = [
    #         # Name: start_hp, energy_type, weakness, resistence, moves
    #          'Skarmory', 60, 'metal', 'fire', ('grass', 30), [('Steel Beak', 20),('Air Cutter', 5)],
    #          'Mareep', 40, 'electric', 'fighting', None, ('Thunder Shock', 10),
    #          'Chansey', 90, 'colorless', 'fighting', None, [('Bind Wound', 5),('Dogpile', 5)],
    #          'Machoke', 80, 'fighting', 'psychic', None, [('Punch', 20),('Mega Kick', 50)],
    #          'Chikorita', 40, 'grass', 'fire', ('water', 30), [('Hipnotic Gaze', 5), ('Double Scratch', 20)],
    #          'Doduo', 50, 'colorless', 'electric', None, ('Fury Attak', 10),
    #          'Clefable', 70, 'colorless', 'fighting', None, ('Doubleslap', 20),
    #          'Persian', 70, 'colorless', 'fighting', ('psychic', 30), [('Scratch', 20),('Pounce', 30)],
    #          'Weezing', 80, 'grass', 'psychic', None, [('Foul Gas', 5), ('Misfire', 60)]
    #      ]

    #      rival_dex(Pokemon) = [
    #         # Name: start_hp, energy_type, weakness, resistence, moves
    #          'Hitmonchan', 70, 'fighting', 'psychic', None, [('Jab', 20), ('Special Punch', 40)],
    #          'Meganium', 100, 'grass', 'fire', ('water', 30), ('Posion Poweder', 40),
    #          'Abra', 30, 'psychic', 'psychic', None, ('Psyshock', 10),
    #          'Zapdos', 90, 'electric', None, ('fighting', 30), [('Thunder', 60), ('Thunderbolt', 100)],
    #          'Butterfree', 70, 'grass', 'fire', None, [('Whirlwind', 20), ('Mega Drain' 40)],
    #          'Ekans', 50, 'grass', 'psychic', None, ('Poison Sting', 10),
    #          'Porygon', 30, 'colorless', 'fighting', ('psychic', 30), [('Conversion1', 5), ('Conversion2', 5)],
    #          'Dewgong', 80, 'water', 'electric', None, [('Aurora Beam', 50), ('Ice Beam', 30)],
    #          'Feraligator', 120, 'water', 'electric', None, ('Rendering Jaw', 30),
    #          'Venomoth', 70, 'grass', 'fire', ('fighting', 30), ('Venom Powder', 15)
    #      ]

    class PokeCardDex():
        def __init__(self, json_file_path=None):
        # NOTE: It is important to handle the case where no path is passed in
        # meaning that json_file_path has a value of None.
            import json

            self.party = {}

            if json_file_path is not None:

                with open (json_file_path) as reader_my_dex:
                    my_dex = json.load(reader_my_dex)

                for pokedict in my_dex:
                    self.name = pokedict['name']
                    self.hp = int(pokedict['hp'])
                    self.energy_type = pokedict['types']
                    self.weakness = pokedict['weaknesses']
                    self.resistence = pokedict['resistences']
                    self.moves = pokedict['attacks']

                # for name in pokedict:
                #     for self.name in self.party:
                #         if self.name == name:
                #             self.party.append(self)

                # self.party = Pokemon(pokedict).append
                # my_party = PokeCardDex('myParty.json')
                # my_party = self.party
            

            ## pass in order variable??? 

#     Example
#     my_dex = PokeCardDex('pokemon_party.json')
#     rival_dex = PokeCardDex()
#     pikachu = Pokemon('Pikachu', 100, 'electric', None, None, (('electric charge', 30),))
#     rival_dex.add_to_party(pikachu)
        
        def set_order(self, order):
            #outer loop int 
            #create a local variable, list of string of pokemon, another int.... *for loop with another for loop*... 
            temp_list=[]

            for name in order:
                for self.name in party:
                    if self.name == name:
                        temp_list.append(self)
                
            party = temp_list
            # print(party)
            pass


        # def battle(self, my_party, challenger_party):
        #     while challenger_party.hp > 0 and my_party.hp > 0:
        #         my_party.take_damage(challenger_party.moves[1], challenger_party.energy_type, challenger_party.resistence[1])
        #         challenger_party.take_damage(my_party.moves[1], my_party.energy_type, my_party.resistence[1])
        #         my_party.take_damage(challenger_party.moves[2], challenger_party.energy_type, challenger_party.resistence[1])
        #         challenger_party.take_damage(my_party.moves[2], my_party.energy_type, my_party.resistence[1])
            # else challenger_party.hp <= 0 or my_party.hp <= 0:
                #$insert new pokemon...break???
        
            # pass

        # def __str__(self):
        #     if self.hp > 0:
        #          return f"Pokemon: {self.name} with {self.hp} HP left"
        #     elif self.hp <= 0:
        #          return f"Pokemon: {self.name} has fainted"     
        #     pass

        # def heal_party(self):
        #     if self.hp < self.start_hp:
        #         self.hp = self.start_hp
        #     pass

        # def add_to_party(self, pokemon):
        #     my_dex.add_to_party(self.name)
        #     pass



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