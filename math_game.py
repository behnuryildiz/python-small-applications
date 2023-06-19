#math game

multiple = int(input("What is your multiple number: "))
scored = 0
for x in range(0 + 1, 11):
    answer = int(input(f"What is the answer of that: \t {x} x {multiple} = "))
    if (answer == x * multiple):
        print("great job!")
        scored += 1
    else:
        print("ups! wrong answer")

print(f"You got {scored} score of 10")