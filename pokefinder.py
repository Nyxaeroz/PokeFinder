# Made by Thijs van Loenhout and Robin Holen on 2021 - 01 - 29

import pandas as pd
import numpy as np

# all types (except null)
types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water', 'none']

# weakness and resistance chart
# [attacker][defender]                    bug   drk  dgn  eltk fry  fgh  fire fly  ghst grs  grnd ice  nrml psn  psy  rck  stl  wtr  
weakness_chart = np.array([
                                          [1,   2,   1,   1,   0.5, 0.5, 0.5, 0.5, 0.5, 2,   1,   1,   1,   0.5, 2,   1,   0.5, 1  ],  # bug 
                                          [1,   0.5, 1,   1,   0.5, 0.5, 1,   1,   2,   1,   1,   1,   1,   1,   2,   1,   1,   1  ],  # drk
                                          [1,   1,   2,   1,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0.5, 1  ],  # dgn
                                          [1,   1,   0.5, 0.5, 1,   1,   1,   2,   1,   0.5, 0,   1,   1,   1,   1,   1,   1,   2  ],  # eltk
                                          [1,   2,   2,   1,   1,   2,   0.5, 1,   1,   1,   1,   1,   1,   0.5, 1,   1,   0.5, 1  ],  # fry
                                          [0.5, 2,   1,   1,   0.5, 1,   1,   0.5, 0,   1,   1,   2,   2,   0.5, 0.5, 2,   2,   1  ],  # fhg
                                          [2,   1,   0.5, 1,   1,   1,   0.5, 1,   1,   2,   1,   2,   1,   1,   1,   0.5, 2,   0.5],  # fire
                                          [2,   1,   1,   0.5, 1,   2,   1,   1,   1,   2,   1,   1,   1,   1,   1,   0.5, 0.5, 1  ],  # fly
                                          [1,   0.5, 1,   1,   1,   1,   1,   1,   2,   1,   1,   1,   0,   1,   2,   1,   1,   1  ],  # ghst
                                          [0.5, 1,   0.5, 1,   1,   1,   0.5, 1,   1,   0.5, 2,   1,   1,   0.5, 1,   2,   0.5, 2  ],  # grs
                                          [0.5, 1,   1,   2,   1,   1,   2,   0,   1,   0.5, 1,   1,   1,   2,   1,   2,   2,   1  ],  # grnd
                                          [1,   1,   2,   1,   1,   1,   0.5, 2,   1,   2,   2,   0.5, 1,   1,   1,   1,   0.5, 0.5],  # ice
                                          [1,   1,   1,   1,   1,   1,   1,   1,   0,   1,   1,   1,   1,   1,   1,   0.5, 0.5, 1  ],  # nrml
                                          [1,   1,   1,   1,   2,   1,   1,   1,   0.5, 2,   0.5, 1,   1,   0.5, 1,   0.5, 0.5, 1  ],  # psn
                                          [1,   0,   1,   1,   1,   2,   1,   1,   1,   1,   1,   1,   1,   2,   0.5, 1,   0.5, 1  ],  # psy
                                          [2,   1,   1,   1,   1,   0.5, 2,   2,   1,   1,   0.5, 2,   1,   1,   1,   1,   0.5, 1  ],  # rck
                                          [1,   1,   1,   0.5, 2,   1,   0.5, 1,   1,   1,   1,   2,   1,   1,   1,   2,   0.5, 0.5],  # stl
                                          [1,   1,   0.5, 1,   1,   1,   2,   1,   1,   0.5, 2,   1,   1,   1,   1,   2,   1,   0.5]]) # water

# calculate weakness multiplier depending on type1 (is it 'none' or not?)
def weakness_multiplier(type1, type2):
    if type1 == 18: 
        return weakness_chart[type_index][type2]
    else: 
        return weakness_chart[type_index][type1] * weakness_chart[type_index][type2]

def print_pokemon(pokemon):
    if pokemon[2] == 'none':
        print('-',pokemon[1],'(', pokemon[3],')')
    else:
        print('-',pokemon[1],'(', pokemon[2], ',', pokemon[3],')')   


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
intput_types_string = input("Resistant to: ")
input_types_list    = intput_types_string.lower().split(" ")

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
for pokemon in data.values:
    qualified = True
    type1 = types.index(pokemon[2])
    type2 = types.index(pokemon[3])

    for word in valid_input_types_list:
        type_index = types.index(word)
        mult = weakness_multiplier(type1,type2)
        
        # check whether pokemon is qualified 
        if mult >= 1:
            qualified = False

    if qualified == True:
        print_pokemon(pokemon)
        # qualified_pokemon_numbers.append(pokemon[0])


# how it works:
# ------------
# 
# 1 We loop over all pokemon
# 2 A pokemon has 2 types, type1 and type2. type1 can be 'none'
# 3 loop over the input types
# 4 for each input type, calculate whether the type-combo of a pokemon resists it, using the weakness chart
# 5 if one of the input types is not resisted by the pokemon, it is not qualified
# 6 print pokemon if it the qualified


