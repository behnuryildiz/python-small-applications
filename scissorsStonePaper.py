from getpass import getpass

print("""
\033[2;35m
PRINT YOUR MOVE
# R, r = Rock
# P, p = Paper
# S, s = Scissors]
""")

counter1 = 0
counter2 = 0

while counter1 < 100 and counter2 < 100:
    player1 = getpass("\033[02;32mPLAYER 1 >\tWhat is your move?\t")
    player2 = getpass("PLAYER 2 >\tWhat is your move?\t")
    player1 = player1.upper()
    player2 = player2.upper()

    if player1 == "R" and player2 == "R":
        print("SAME MOVE! 😌")

    elif player1 == "R" and player2 == "S":
        print("Player 1 won! 🥳")
        counter1 += 1

    elif player1 == "R" and player2 == "P":
        print("Player 2 won! 🥳")
        counter2 += 1

    elif player1 == "P" and player2 == "P":
        print("SAME MOVE! 😌")

    elif player1 == "P" and player2 == "S":
        print("Player 2 won! 🥳")
        counter2 += 1

    elif player1 == "P" and player2 == "R":
        print("Player 1 won! 🥳")
        counter1 += 1

    elif player1 == "S" and player2 == "S":
        print("SAME MOVE! 😌")

    elif player1 == "S" and player2 == "P":
        print("Player 1 won! 🥳")
        counter1 += 1

    elif player1 == "S" and player2 == "R":
        print("Player 2 won! 🥳")
        counter2 += 1

    else:
        print("try again 🥴")
    print(
        f"\n\033[2;33mPLAYER 1 SCORE:\t{counter1}👏\nPLAYER 2 SCORE:\t{counter2}👏\n")
  
    if counter1 == 3 or counter2 == 3:
      exitAsking = input("Game is Over! Do you want to QUIT the game? Y/N \t")
      if exitAsking.upper() != "Y":
        continue
      else:
        exit()