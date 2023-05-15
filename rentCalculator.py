rent = float(input("What is the total monthly \033[2;33mRENT ?\t"))

electricity = float(input("What is the \033[2;34mELECTRICITY bill ?\t"))
gas = float(input("What is the \033[2;36mGAS bill ?\t"))
#funkbetrag = float(input("What is the funkbetrag ?\t"))
#homeInternet = float(input("What is the home internet ?\t"))
numberOfPeople = int(input("How many \033[2;37mPEOPLE are there ?\t"))

summeOfRentMonthly = (rent + (-electricity) + (-gas) ) / numberOfPeople
print ("\033[2;32mthe summary of the monthly rent is", summeOfRentMonthly)