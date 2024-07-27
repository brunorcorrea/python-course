import config

lottery_numbers = config.lottery_numbers

players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

winner = {"name": None, "numbers_matched": 0}

for player in players:
    numbers_matched = len(player['numbers'].intersection(lottery_numbers))
    if numbers_matched > winner['numbers_matched']:
        winner = {"name":player['name'], "numbers_matched": numbers_matched}

if winner['name'] != None:
    print(f"{winner['name']} won {100 ** winner['numbers_matched']}.")
