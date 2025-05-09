print("Can You Drive?")
print("~~~~~~~~~~~~~~")
print()
age = int(input("How Old Are You?\n"))
print()
license = input("Do You Have a License? (Type yes or no)\n")
print()
if age >= 18 and license.lower() == "yes":
    print("You Can Drive")
else:
    print('You Can not Drive')
print()
print()