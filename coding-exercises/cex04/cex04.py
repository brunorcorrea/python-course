lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        "name": "Bruno",
        "numbers": {5,13,19,20,22}
    },
    {
        "name": "Yasmin",
        "numbers": {28,2,21,23,26}
    }
]

player_message = "Player {name} got {right_numbers} numbers right."

player1_name = players[0]["name"]
player1_right_numbers = len(players[0]["numbers"].intersection(lottery_numbers))

player2_name = players[1]["name"]
player2_right_numbers = len(players[1]["numbers"].intersection(lottery_numbers))

print(player_message.format(name=player1_name, right_numbers=player1_right_numbers))
print(player_message.format(name=player2_name, right_numbers=player2_right_numbers))