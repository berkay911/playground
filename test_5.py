secret = 13
x = int(input("Guess a number: "))

if x==secret:
    print("Equal")

elif x > secret:
    print("Your number is bigger")

else:
    print("Your number is smaller")