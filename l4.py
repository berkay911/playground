#from secret_number_library import secret_number , hint
#print(hint)

#guess = int(input("Guess the secret number: "))

#for x in range(5,15):
#    if guess == secret_number:
 #       print("Congratulations! You guessed the secret number.")
 #       break
  #  else:
      #  print("Wrong guess. Try again.")
      #  guess = int(input("Guess the secret number: "))


        

 # number_square = 0
 # number = int(input("Enter a number to see its square: "))

 # while number_square**2 < number:
  #    number_square += 1
   #   if number_square**2 > number:
    #      print("Well, there is no integer square root for this number.")
   #       break
    #  elif number_square**2 == number:
   #       print(f"The square root of {number} is {number_square}.")
    #      break
   #   else:
    #      pass    


#Ben = Alyssa - 2
#Cindy = Alyssa*2
#Ben + alyssa + Cindy = 1000 


 # for Ben in range(1001):
  #    Alyssa = Ben + 20
   #   Cindy = Alyssa * 2
    #  if Ben + Alyssa + Cindy == 1000:
    #      print(f"Ben is {Ben}, Alyssa is {Alyssa}, and Cindy is {Cindy}.")
     #     break



#maliyet = x
#satış is y 
#product sold with %20 profit
#y = 2x  y = 4x - 42 


#for x in range(1, 1000):
#    y = 2 * x
#    if y == 4 * x - 42:
#        print(f"Cost: {x}, Selling Price: {y}")
#        break

num = 5
binary_rep = ""

if num == 0:
    binary_rep = "0"

while num > 0:
    remainder = num % 2
    binary_rep = str(remainder) + binary_rep
    num = num // 2
print(f"Binary representation: {binary_rep}")

