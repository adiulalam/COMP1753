from random import randint

name = input("What is your name? ")
random_num = randint(int (1), int (100))

print("Hello "+name+", your lucky number is "+str(random_num))
