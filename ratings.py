"""Restaurant rating lister."""


# put your code here

def restaurant_ratings(filename):

    data_score = open(filename)

    ratings_log = {}

    for line in data_score:
        line = line.rstrip()
        restaurant, score = line.split(":")
        ratings_log[restaurant] = score

    for restaurant, rating in ratings_log.items():
        print(f"{restaurant} is rated at {rating}.")

    print()

    print('You can add rating for new restaurants. ')

    print()

    new_restaurant = input(' Please, type the restaurant name > ').title()
    new_restaurant_rating = int(input(' Rating > '))

    ratings_log[new_restaurant] = new_restaurant_rating

    for restaurant, rating in sorted(ratings_log.items()):
        print(f"{restaurant} is rated at {rating}.")


restaurant_ratings('scores.txt')
