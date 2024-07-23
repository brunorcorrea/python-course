nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

friend = input("Please, enter the name of a friend: ")
user_friends.add(friend)

friends_nearby = nearby_people.intersection(user_friends)
print(friends_nearby)