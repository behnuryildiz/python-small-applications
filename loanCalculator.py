# Loan Calculator

loanedMoney = float(input("How many do you need to load? "))
howLong = int(input("How long do you need to pay it back ( in years ) ? "))
interest = 5
print(f"the interest is for {howLong} years {interest}%")

calculationResultList = []
for year in range(howLong):
    calculationOfResultInterest = (loanedMoney * interest * (year + 1) / 100)
    calculationResultList.append(calculationOfResultInterest)

    print(f"Year {year+1} is ", (loanedMoney + calculationOfResultInterest), "$")
print(
    f"You paid for interest for {howLong} years totally : {sum(calculationResultList)}$"
)
"""A main money(capital)
t interest for year,
n time in year,
F interest; F=A.n.t/100
If we want to calculate month based; F=A.n.t1200
"""