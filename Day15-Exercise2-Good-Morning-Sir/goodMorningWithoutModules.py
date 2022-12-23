time = int(input("Enter the current time of your area : "))
gender = input("Enter your gender: ")

if (time <= 12):
    if (gender == "Male" or gender == "male"):
        print("Good Morning Sir\nWhat a good day to start your work")
    elif (gender == "Female" or gender == "female"):
        print("Good Morning Mam\nWhat a good day to start your work")
    else:
        print("Sorry you have entered the wrong keyword")

elif (time>12 and time <=17):
    if (gender == "Male" or gender == "male"):
        print("Good Afternoon Sir\nKeep it up the work")
    elif (gender == "Female" or gender == "female"):
        print("Good Afternoon Mam\nKeep it up the work")
    else:
        print("Sorry you have entered the wrong keyword")

elif (time>17 and time <=22):
    if (gender == "Male" or gender == "male"):
        print("Good Evening Sir\nTime for chilling after a hectic day")
    elif (gender == "Female" or gender == "female"):
        print("Good Evening Mam\nTime for chilling after a hectic day")
    else:
        print("Sorry you have entered the wrong keyword")

elif (time>22 and time <=24):
    if (gender == "Male" or gender == "male"):
        print("Good Night Sir\nSleep well")
    elif (gender == "Female" or gender == "female"):
        print("Good Night Mam\nSleep well")
    else:
        print("Sorry you have entered the wrong keyword")