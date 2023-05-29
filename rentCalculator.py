rent = float(input("What is the total monthly \033[2;33mRENT ?  >> "))
electricity = float(input("What is the \033[2;34mELECTRICITY bill ?  >> "))
gas = float(input("What is the \033[2;36mGAS bill ?  >> "))
funkbetrag = float(input("What is the funkbetrag ?  >> "))
homeInternet = float(input("What is the home internet ?  >> "))
numberOfPeople = int(input("How many \033[2;37mPEOPLE are there ?  >> "))

extraPayments = []
while True:
    askingAddition = input("is there anything else to add: y/n  >>  ")
    if askingAddition.upper() == "Y":
        newPayment = float(input("type new payment :  "))
        extraPayments.append(newPayment)
    else: 
        break
summeOfRentMonthly = (rent + electricity + gas + sum(extraPayments)) / numberOfPeople
print ("\033[2;32mthe summary of the monthly rent per person is", summeOfRentMonthly)