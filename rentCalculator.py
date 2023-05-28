rent = float(input("What is the total monthly \033[2;33mRENT ?\t"))

electricity = float(input("What is the \033[2;34mELECTRICITY bill ?\t"))
gas = float(input("What is the \033[2;36mGAS bill ?\t"))
funkbetrag = float(input("What is the funkbetrag ?\t"))
homeInternet = float(input("What is the home internet ?\t"))
numberOfPeople = int(input("How many \033[2;37mPEOPLE are there ?\t"))

newPayments = 0.0
askingAddition = input("is there anything else to add: y/n\t")
if askingAddition.upper() == "Y":
    newPayments = float(input("type new payment :\t"))

summeOfRentMonthly = (rent + electricity + gas + newPayments) / numberOfPeople
print ("\033[2;32mthe summary of the monthly rent is", summeOfRentMonthly)