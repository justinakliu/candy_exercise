'''
DIRECTIONS
==========

1. In `get_friends_favorite_candy_count()`, return a dictionary of candy names and the
amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

2. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

3. In `get_friends_who_like_specified_candy()`, return 
a tuple of friends who like the candy specified in the candy_name parameter.

4. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

5. Starting with nominal cases, write tests for each of the functions below then 
write tests to handle edge cases.
'''

# 1. In `get_friends_favorite_candy_count()`, return a dictionary of candy names and the
# amount of times each candy appears in the `friend_favorites` list.

# friend_favorites = [
#     ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
#     ["Bob", ["milky way", "licorice", "lollipop" ]],
#     ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
#     ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
# ]

# 1


def get_friends_favorite_candy_count(favorites):
    favorite_candies = {}
    for friend in favorites:
        for candy in friend[1]:
            # print(candy)
            if candy in favorite_candies:
                favorite_candies[candy] += 1
            else:
                favorite_candies[candy] = 1
    print(favorite_candies)
    return favorite_candies


friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy"]],
    ["Bob", ["milky way", "licorice", "lollipop"]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
]

get_friends_favorite_candy_count(friend_favorites)

# 2. Given the list `friend_favorites`, create
# a new data structure in the function `create_new_candy_data_structure`
# that describes the different kinds of candy paired with a list of friends that
# like that candy.


def create_new_candy_data_structure(data):
    candy_data = {}
    for friend in data:
        for candy in friend[1]:
            if candy in candy_data:
                if friend not in candy_data[candy]:

                    candy_data[candy].append(friend)
            else:
                candy_data[candy] = [friend]
    return candy_data


# 3


def get_friends_who_like_specific_candy(data, candy_name):
    pass

# 4


def create_candy_set(data):
    pass
