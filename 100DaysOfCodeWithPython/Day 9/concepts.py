"""
Day 9:
- Dictionaries
- Nesting
"""
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    1: "A number"
}

# print(programming_dictionary)

# Adding a new entry to the dictionary
programming_dictionary["Refactoring"] = "The process of refining code"

# print(programming_dictionary)

empty_dictionary = {}

# # Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an entry in a dictionary
programming_dictionary["Bug"] = "A moth stuck in your computer"
# print(programming_dictionary)

# # Looping through the contents of a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# # Nested List in Dictionary
# travel_log = {
#     "Nigeria": ["Abuja", "Lagos", "Enugu", "Kaduna"],
#     "Ghana": ["Accra", "Aburi"],
#     "South Africa": ["Johannesburg", "Cape Town"],
#     "Rwanda": ["Kigali"]
# }
#
# # Print out Enugu
# print(travel_log["Nigeria"][2])
#
# # Nesting List in List
# nested_list = ["A", "B", ["C", "D"]]
#
# # Print
# print(nested_list[2][1])

# More complex data
travel_log = {
    "Nigeria": {
        "total_visits": 20,
        "cities_visited": ["Abuja", "Lagos", "Enugu", "Kaduna"],
    },
    "Ghana": {
        "total_visits": 5,
        "cities_visited": ["Accra", "Aburi"],
    },
    "South Africa": {
        "total_visits": 10,
        "cities_visited": ["Johannesburg", "Cape Town"],
    },
    "Rwanda": {
        "total_visits": 1,
        "cities_visited": ["Kigali"],
    }
}

# Print "I've visited Cape Town 5 out of 10 times"
print(f"I've visited {travel_log["South Africa"]["cities_visited"][1]} 5 out \
of {travel_log["South Africa"]["total_visits"]} times")