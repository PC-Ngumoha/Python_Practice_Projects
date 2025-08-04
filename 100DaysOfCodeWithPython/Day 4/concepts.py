"""
Day 4:
- Randomisation
- Lists
"""
import random
import mymodule

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(mymodule.fav_number)

"""Creating random floating point numbers
"""
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
# random_float = random.uniform(1, 10)
# print(random_float)

"""Practice program
"""
# # Heads = 0, Tails = 1
# coin_toss = random.randint(0, 1)
# # if coin_toss == 1:
# #     print("Heads")
# # else:
# #     print("Tails")
# print("Heads" if coin_toss == 1 else "Tails")

"""Lists
- indexing is zero-based i.e counting / indexing starts from number 0 not 1
"""
# states = ["Kaduna", "Lagos", "Cross River", "Enugu"]
#
# states.append("Aroland")
# states.extend(["Bauchi", "Gongola", "Bakassi Peninsula"])
#
# print(states)

"""Who will pay the bill ?
"""
# friends = ["Chidi", "Nneka", "Aramide", "Sandra", "Chinenye", "Mustapha", "Buchi", "Segun",
#            "Gbemi", "Inemesit", "Evolution", "Bassey", "Echekwu", "Ephraim", "Edison"]
# # Approach 1
# choice = random.randint(0, len(friends) - 1)
# print(friends[choice])
#
# # Approach 2
# print(random.choice(friends))

"""IndexErrors and working with nested lists
"""
states = ["Kaduna", "Lagos", "Cross River", "Enugu"]
cities = ["Kaduna", "Ikeja", "Ogoja", "Enugu"]
# print(states[4]) # Will raise an IndexError

states_and_cities = [states, cities]
print(len(states_and_cities))