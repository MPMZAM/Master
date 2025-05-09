print("Calcaulater")
print("~~~~~~~~~~~")
print()

first = float(input("Enter The First Side:\n"))
print()

sign = input('Enter The Sign Between Two Sides: ( "+" or "-" or "*" or "/" ) :\n')
print()

second = float(input("Enter The Second Side:\n"))
print()

if sign == "+":
    print(f"The Result is {first+second}")
elif sign == "-":
    print(f"The Result is {first-second}")
elif sign == "*" or sign == "x":
    print(f"The Result is {first*second}")
elif sign == "/" :
    print(f"The Result is {first/second}")
else:
    print("Enter A Valid Sign or Number")
print()
print()
