# a = 0
# while (a < 3):
#   print(a)
#   a = a + 1


i = int(input("Guess a random number : "))
if(i == 3):
  while True:
    print("Value Matched")
    break
else:
  print("Value doesn't match")


#emulating do-while loop

k = 0
while True:
  print(k)
  k = k + 1
  if(k%100 == 0):
    break