# Made by Thijs van Loenhout and Robin Holen on 2021 - 01 - 29

import pandas as pd
import numpy as np

# all types (except null)
types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

# resistances
resistances = {
    'none':[],
    'bug':['fighting','flying','poison','ghost','steel','fairy'],
    'dark':['fighting','dark','fairy'],
    'dragon':['steel','fairy'],
    'electric':['ground','grass','electric','dragon'],
    'fairy':['poison','steel','fire'],
    'fighting':['flying','poison','ghost','psychic','fairy'],
    'fire':['rock','fire','water','dragon'],
    'flying':['rock','electric','steel'],
    'ghost':['normal','dark'],
    'grass':['flying','poison','bug','steel','fire','grass','dragon'],
    'ground':['flying','bug','grass'],
    'ice':['steel','fire','water','ice'],
    'normal':['rock','ghost','steel'],
    'poison':['ground','rock','ghost','steel'],
    'psychic':['steel','pychic','dark'],
    'rock':['fighting','ground','steel'],
    'steel':['steel','fire','water','electric'],
    'water':['water','grass','dragon']
}

# read the pokemon data
data = pd.read_csv('pokemon.csv')

# show welcome message
welcome_message = """

                                    = = = = = = = = = = = = = = = = = 
                                    =                               =
                                    =     Welcome to PokéFinder     =
                                    =   (made by Thijs and Robin!)  =
                                    =                               = 
                                    = = = = = = = = = = = = = = = = =

This tool lets you enter any number of types and returns all Pokémon that resist these types.

"""

print(welcome_message)

# get user input
intput_types_string = input("Enter types: ")
input_types_list    = intput_types_string.lower().split(" ")
print(input_types_list)

# choice              = input("Pokemon or types? (p/t)") 
# generation          = input("Maximum generation (1-8)")

# verify user input
valid_input_types_list = []
for word in input_types_list:
    if word not in types:
        print(word,'is not a type! We will continue without it!')
    else: 
        valid_input_types_list.append(word)

# later maybe: stuff with generations etc?

# determine types that resist input types
# maybe use this later for fancier printing:
# qualified_pokemon_numbers = []
for pokemon in data.values:
    qualified = True
    type1 = pokemon[2] # first type of pokemon (possibly 'none')
    type2 = pokemon[3] # second type of pokemon
    for word in valid_input_types_list:
        list_of_resistances = resistances[word]
        if type1 not in list_of_resistances and type2 not in list_of_resistances:
            qualified = False
    if qualified == True:
        print(pokemon)
        # qualified_pokemon_numbers.append(pokemon[0])




# how it works:
# ------------
# 
# As input, we get a list of types: valid_input_types
# For each type 'word' in this list, we have a list of types that resist 'word'
# We then want to check, for each Pokemon, whether each list of resistances has a representative in the Pokemon's types
# 
# An example:
# ----------
# valid_input_types_list: ground       water                    fairy
# list_of_resistances:    [bug,grass]  [grass, dragon, water]   [poison, steel, fire]
# first pokemon:          Bulbasaur:   poison, grass
# 
# So, Bulbasaur is qualified, as each resistance list has a representative:
#    ground -> [bug,grass]             -> type1 = grass
#    water  -> [grass, dragon, water]  -> type1 = grass  
#    fairy  -> [poison, steel, fire]   -> type2 = poison


