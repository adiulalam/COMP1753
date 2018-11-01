from random import randint

name = input("What is your name? ")

random_num = randint(int (1), int (10))
num_str= str(random_num)
message= ("")

if num_str == "3" or num_str == "9":
    message= "and you have won a prize"
elif num_str == "7":
    message= "and you have hit the jackpot"

print ("Hello " + name + " your lucky number is " + num_str + " " + message)
