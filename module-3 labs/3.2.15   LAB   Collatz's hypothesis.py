number = int(input())
c0 = number
step = 0
while c0!=1 :
    if c0 % 2 == 0 :
        c0 = c0//2
        print(c0)
    else :
        c0 = c0*3 + 1
        print(c0)
    step = step + 1
print("steps = ",step)