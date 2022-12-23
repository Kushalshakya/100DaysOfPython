print("\"Calculator:\"\n1 For Addition\n2 For Subtraction\n3 For Division\n4 For Multiplication\n5 For Modulus\n6 For Exponential")
i = int(input("Enter First Number : "))
j = int(input("Enter Second Number : "))
count = int(input("Enter Number Between 1-6 : "))

if count == 1:
    print("Sum is : ", i + j)
elif count == 2:
    print("Sub is : ", i - j)
elif count == 3:
    print("Div is : ", i / j)
elif count == 4:
    print("Mul is : ", i * j)
elif count == 5:
    print("Mod is : ", i % j)
elif count == 6:
    print("Exponential is : ", i ** j)
else:
    print("Range Exceeded")

# elif count > 4:
#     print("Range Exceeded")