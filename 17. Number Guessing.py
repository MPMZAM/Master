import random
num = random.randint(1,3)
print("Number Guessing")
print("~~~~~~~~~~~~~~~")
print()
password = int(input("Guess a Number From 1 To 3\n"))
print()
if password==num:
    print(f"Yup,Thats Right Its {num}")
elif password>5:
    print("That Bigger Than 3")
elif password<1:
    print("The Number Is Less Than One")
else:
    print(f"Thats Wrong The Correct Number is {num}")
print()
print()