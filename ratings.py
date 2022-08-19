"""Restaurant rating lister."""


# put your code here

def restaurant_ratings(filename):

    data_score = open(filename)

    ratings_log = {}

    for line in data_score:
        line = line.rstrip()
        words = line.split(":")
        restaurant = words[0]
        score = words[1]

        ratings_log[restaurant] = score

    return ratings_log

    # for word in words:
    #     ratings_log[word] =


print(restaurant_ratings('scores.txt'))
