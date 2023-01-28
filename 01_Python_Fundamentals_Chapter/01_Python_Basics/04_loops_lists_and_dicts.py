# --------------
# REMEMBER
# --------------

my_list = ["Sara", "Peter", "Tom"]
my_dict = {
    "name": "Samuel",
    "age": 35, 
    "developer": True
}

# i) Lists
# For Loop Type 1 -> Numeric Range Loop
# for idx in range(len(my_list)): # traverse list indexes
#     print(idx, my_list[idx])

# # For Loop Type 2 -> Collection-Based or Iterator-Based Loop
# for each in my_list:  # traverse list elements
#     print(each)

# ii) Dict
# For Loop Type 2 > Collection-Based or Iterator-Based Loop

# print("*"*50)

# # Way 1
# print("-"*50)
# print(type(my_dict))
# print(my_dict)
# print("-"*50)
# for key in my_dict:  # traverse dict keys
#     print(type(key), type(my_dict[key]))
#     print(key, my_dict[key])

# print("*"*50)

# # Way 2
# print("-"*50)
# print(type(my_dict.items()))
# print(my_dict.items())
# print("-"*50)
# for key, val in my_dict.items(): # traverse dict keys and values
#     print(type(key), type(val))
#     print(key,val)

# print("*"*50)

# # Way 3
# print(type(my_dict.keys()))
# for key in my_dict.keys():  # traverse dict keys (as a dict_key class)
#     print(type(key))
#     print(key)

# print("*"*50)

# # Way 4
# print(type(my_dict.values()))
# for val in my_dict.values():  # traverse dict keys (as a dict_key class)
#     print(type(val))
#     print(val)

# print("*"*50)

# --------------
# EXCERCISE
# --------------

my_list=[1,2.3]


print(my_list)

dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
    "admins" : ["Jorge", "Samuel"]
}

# Expected Output

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

# 1) REALLY BAD APPROACH
def printInfo_solution_1(some_dict):
    print(f"{len(dojo['locations'])} LOCATIONS")
    for each in dojo["locations"]: # iterator-based for loop
        print(f"{each}")

    print(f"{len(dojo['instructors'])} INSTRUCTORS")
    for idx in range(len(dojo["instructors"])): # range for loop
        print(f"{dojo['instructors'][idx]}")

# 2) GOOD APPROACH, BUT LONG
def printInfo_solution_2(some_dict):

    keys= list(some_dict.keys())
    key_1 = keys[0]
    key_2 = keys[1]
    print(keys, type(keys))
    print(key_1, type(key_1))
    print(key_2, type(key_2))

    value_1 = some_dict[key_1]  # dojo['locations']
    value_2 = some_dict[key_2]  # dojo['instructors']

    # LOCATIONS
    print(f"{len(value_1)} {key_1.upper()}")
    for idx in range(len(value_1)):
        print(f"{value_1[idx]}")

    # INSTRUCTORS
    print(f"{len(value_2)} {key_2.upper()}")
    for each in value_2:
        print(f"{each}")

# 3) BEST APPROACH
def printInfo_solution_3(some_dict):
    # 1st Loop -> through the dict
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")  # Loop 1: 'LOCATIONS'
                                                       # Loop 2: 'INSTRUCTORS'
         # 2nd Loop -> through list (value of each key in dict)
        for each in some_dict[key]:
            print(each) # Loop 1: 'San Jose', 'Seattle'....
                        # Loop 2: 'Michael, 'Amy', ...


printInfo_solution_3(dojo)