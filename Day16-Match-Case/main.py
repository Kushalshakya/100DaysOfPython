#python 3.10 is important for matchCase
#break statement is complimentary (i.e: without break by default it halts the process when matched)

i = int(input("Enter the value of i : "))
match i:
  case 0:
    print("The value is zero")

  case 1:
    print("Value is one")

  case 4:
    print("Value is four")

  case _ if i!=90:
    print(i, "i is not 90")

  case _ if i!=80:
    print(i, "i is not 80")

  case _:
    print(i)