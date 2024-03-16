secret_number = 777
number=int(input())
found = True
while found :
    if number!=secret_number :
        print("Ha ha! You're stuck in my loop!")
        number=int(input())
    if number==secret_number :
        print(number,"Well done, muggle! You are free now.")
        found = False