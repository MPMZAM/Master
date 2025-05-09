print("Random PIN")
print("~~~~~~~~~~")
print()
import random
random = random.randint(1000,9999)
input = int(input("Enter Your Pin Code:\n"))
print()
if random == input:
    print(f"Yup, The Number is {random}")
elif len(str(input)) != 4:
    print("Please Enter 4 Digit Number")
else:
    print(f"The PIN Code is Incorrect The Correct one is {random}")
print()
print()