print("""
\033[2;35m
PRINT YOUR MOVE
# R, r = Rock
# P, p = Paper
# S, s = Scissors
""")
from getpass import getpass
counter1 = 0
counter2 = 0

pcOrManually = input("Do you wannt to play versus PC or another person?\n1 for versus PC\n2 for versus PERSON\t")

while counter1 < 10 and counter2 < 10:
    if pcOrManually == "1":
        import random
        pcMove = random.choice(["R", "P", "S"])
        playerMove = input("\033[02;32mPLAYER >\tWhat is your move?\t")
        pcMove = pcMove.upper()
        playerMove = playerMove.upper()
        print("\nThe move of PC was the", pcMove)
        if playerMove == "R" and pcMove == "R":
            print("SAME MOVE! 😌")
        elif playerMove == "R" and pcMove == "S":
            print("YOU WON! 🥳")
            counter1 += 1
        elif playerMove == "R" and pcMove == "P":
            print("PC WON! 🥳")
            counter2 += 1
        elif playerMove == "P" and pcMove == "P":
            print("SAME MOVE! 😌")
        elif playerMove == "P" and pcMove == "S":
            print("PC WON! 🥳")
            counter2 += 1
        elif playerMove == "P" and pcMove == "R":
            print("YOU WON! 🥳")
            counter1 += 1
        elif playerMove == "S" and pcMove == "S":
            print("SAME MOVE! 😌")
        elif playerMove == "S" and pcMove == "P":
            print("YOU WON! 🥳")
            counter1 += 1
        elif playerMove == "S" and pcMove == "R":
            print("PC WON! 🥳")
            counter2 += 1
        else:
            print("try again 🥴")

        print("\n", "XXXXXXXXXX"*2, f"\n\033[2;33mYOUR SCORE:\t{counter1}👏\nPC SCORE:\t{counter2}👏\n", "XXXXXXXXXX"*2, "\n")
        

    elif pcOrManually == 2:
        player1 = getpass("\033[02;32mPLAYER 1 >\tWhat is your move?\t")
        player2 = getpass("PLAYER 2 >\tWhat is your move?\t")
        player1 = player1.upper()
        player2 = player2.upper()
        if player1 == "R" and player2 == "R":
            print("SAME MOVE! 😌")
        elif player1 == "R" and player2 == "S":
            print("Player 1 WON! 🥳")
            counter1 += 1
        elif player1 == "R" and player2 == "P":
            print("Player 2 WON! 🥳")
            counter2 += 1
        elif player1 == "P" and player2 == "P":
            print("SAME MOVE! 😌")
        elif player1 == "P" and player2 == "S":
            print("Player 2 WON! 🥳")
            counter2 += 1
        elif player1 == "P" and player2 == "R":
            print("Player 1 WON! 🥳")
            counter1 += 1
        elif player1 == "S" and player2 == "S":
            print("SAME MOVE! 😌")
        elif player1 == "S" and player2 == "P":
            print("Player 1 WON! 🥳")
            counter1 += 1
        elif player1 == "S" and player2 == "R":
            print("Player 2 WON! 🥳")
            counter2 += 1
        else:
            print("try again 🥴")
        print("\n", "XXXXXXXXXX"*2, f"\n\033[2;33mPLAYER 1 SCORE:\t{counter1}👏\nPLAYER 2 SCORE:\t{counter2}👏\n", "XXXXXXXXXX"*2, "\n")
    else:
        print("something is invalid here, give another try.")
        break
    if counter1 == 3 or counter2 == 3:
      exitAsking = input("Game is Over! Do you want to QUIT the game? Y/N \t")
      if exitAsking.upper() != "Y":
        continue
      else:
        exit()