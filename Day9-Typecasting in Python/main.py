# TypeCasting of String datatype to Integer
i = "10"
j = "8"
print(int(i) + int(j))

# Two Types of TypeCasting :
# Implicit & Explicit
# Implicit - Automatic Conversion
# Explicit - Programmer Conversion of Datatype

#Implicit TypeCasting
a = 2.5
b = 6
print(a + b)

#Explicit TypeCasting
num = "1"
mum = 2
num_mum = int(num)  #Throws an error is the string is not a valid integer
sum = mum + num_mum
print("The Sum of both the numbers are : ", sum)