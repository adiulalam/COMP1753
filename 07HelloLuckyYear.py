from random import randint

name = input("What is your name? ")

birth_year = int(input("What is your year of birth? "))

random_num = randint(int (0), int (70))

addition= birth_year + random_num

print("Hello "+name+", your lucky year is "+str(addition))


