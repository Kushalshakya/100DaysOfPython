#So Excited to learn break & continue Statement

for a in range(1,10):
    if(a == 5):
        break
    print(a)

for i in range(5,30):
    if(i == 20):
        continue
    print(i)

# Table of Five

for a in range(1,13,1):
    print("5 X ",a,"=",5*a)
    if(a == 10):
        break