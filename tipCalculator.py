## TIP-CALCULATOR
spended = float(input("How much did you spend?  >\t"))
tipPercentage = int(input("What percentage do you want to tip?  >\t"))
numberOfPerson = int(input("How many people are there in the group?  >\t"))
tipPercentage = (tipPercentage / 100)

tip = round(((spended / numberOfPerson) * tipPercentage), 3)
print(tip)