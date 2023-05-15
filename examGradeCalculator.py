## EXAM GRADE CALCULATOR
lessonName = (input("Name of exam : "))
scoreMax = int(input("Max score: "))
studentScore = int(input("Stundent score: "))

if (studentScore >= 90):
    print(f"Student got the {studentScore}, \033[1;36m which is a A+")

elif (71 <= studentScore <= 80):
    print(f"Student got the {studentScore}, \033[1;37m which is a A-")

elif (61 <= studentScore <= 70):
    print(f"Student got the {studentScore}, \033[1;33m which is a B")

elif (51 <= studentScore <= 60):
    print(f"Student got the {studentScore}, \033[1;32m which is a C")

elif (41 <= studentScore <= 50):
    print(f"Student got the {studentScore}, \033[1;35m which is a D")

elif (studentScore <= 40):
    print(f"Student got the {studentScore}, \033[4;31mwhich is a U")
else:
    print("Try again")

## COLOR SET UP
""" 
30m : gray
 31m : red
 32m : orange
 33m : yellow
 34m : blue
 35m : purple
 36m : blue
 37m : white
 1 : normal
 2 : opac
 3 : italic
 4 : underlined 
 """