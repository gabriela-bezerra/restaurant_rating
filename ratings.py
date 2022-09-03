"""Restaurant rating lister."""


# put your code here

# def restaurant_ratings(filename):

#     data_score = open(filename)

#     ratings_log = {}

#     for line in data_score:
#         line = line.rstrip()
#         restaurant, score = line.split(":")
#         ratings_log[restaurant] = score

#     for restaurant, rating in sorted(ratings_log.items()):
#         print(f"{restaurant} is rated at {rating}.")

#     print()

#     print('You can add rating for new restaurants.')

#     print()

#     new_restaurant = input(' Please, type the restaurant name > ').title()
#     new_restaurant_rating = int(input(' Rating > '))

#     # while True:
#     #     new_restaurant_rating < 6:
#     #     continue
#     # else:
#     #     print(' Please rate within 1 - 5')
#     #     new_restaurant_rating = int(input(' Rating > '))

#     ratings_log[new_restaurant] = new_restaurant_rating

#     for restaurant, rating in sorted(ratings_log.items()):
#         print(f"{restaurant} is rated at {rating}.")


# restaurant_ratings('scores.txt')

import sys
from types import new_class

""" Reads ratings in a file"""


def ratings(file=sys.argv[1]):

    file_data = open(file)

    rating = {}

    user_input = input("Would you like to add a restaurant? y/n >").lower()

    while True:
        if user_input == "y":
            new_restaurant = input("Restaurant name > ").title()
            score = input("Score > ")
            if type(score) != int:
                print("Score not valid, please choose a number between 0-5.")
                score = input("Score > ")
            if int(score) > 5:
                print("Score not valid, please choose a number between 0-5.")
                score = input("Score > ")

            rating[new_restaurant] = score
            break
        if user_input == "n":
            break

    for line in file_data:
        line = line.rstrip()
        restaurants = line.split(":")

        rating[restaurants[0]] = restaurants[1]

    for restaurant, rate in sorted(rating.items()):
        print(f"{restaurant} is rated at {rate}.")

    file_data.close()


ratings()
