# REPLIT LOGIN SYSTEM
import getpass


def logInSystem(logInName, password):
  if (logInName.lower() == "admin" and password == "Gfjsl65a78511sfPq"):
    print("Welcome", logInName.capitalize(), "!")
  else:
    print("Try again!")


logInName = str(input("What is the login name?:\t"))
password = getpass.getpass("What is the password?:\t")
logInSystem(logInName, password)