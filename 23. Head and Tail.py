import random

print("Head and Tail Game")
print("~~~~~~~~~~~~~~~~~~")
print()

random_choice = random.randint(1, 2)  # 1 or 2
user_input = input("Head or Tail:\n").lower()  # head or tail
print()

if user_input == "head":
    if random_choice == 1:
        print("Yup, Head is Right")
    else:
        print("No, Tail is Correct")
elif user_input == "tail":
    if random_choice == 2:
        print("Yup, Tail is Right")
    else:
        print("No, Head is Correct")
else:
    print("Enter a Valid Answer")
print()
print()