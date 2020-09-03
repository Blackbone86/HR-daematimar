p1_move = input("Player 1's move: ")
p2_move = input("Player 2's move: ")

scissors = "scissors"
rock = "rock"
paper = "paper"

p1_wins = None

# ...now fill in the rest

if p1_move == rock:
    if p2_move == scissors:
        p1_wins = True
    elif p2_move == paper:
        p1_wins = False
elif p1_move == scissors:
    if p2_move == rock:
        p1_wins = False
    elif p2_move == paper:
        p1_wins = True
elif p1_move == paper:
    if p2_move == rock:
        p1_wins = True
    elif p2_move == scissors:
        p1_wins = False

if p1_wins:
    print("Winner: Player 1")
elif p1_wins == False:
    print("Winner: Player 2")
else:
    print("It's a draw")


# if p1_move == p2_move:
#     p1_wins = None