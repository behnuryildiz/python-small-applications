## GUILT-SPLIT CALCULATOR
myBill = float(input("How high is your bill?  >\t"))
numberOfPeople = int(input("How many people attended?  >\t"))
answer = round((myBill / numberOfPeople), 2)  # iki haneliye yuvarlar
#answer = round(answer, 2)     #or we can write an extra code for that
print("You each all owe  >\t", answer)