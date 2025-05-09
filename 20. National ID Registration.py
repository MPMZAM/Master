print("National ID Registration")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print()
egyptian = input("Are You Egyptian?\n").lower()

print()
if egyptian=="yes":
    print("Great! You Have Passed The First Step")
    print()
    age = int(input("How Old Are You?\n"))
    print()
    if age>14 :
        print("You Can Have an ID")
    else:
        print("You Are Below The Age Please Try Again When You Are 15")
else:
    print("Sorry! Egyptian IDs Are For Egyptians Only")
print()
print()