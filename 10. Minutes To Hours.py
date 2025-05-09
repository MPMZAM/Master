print ("Welcome to Minutes To Hours APP")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
str_minutes = input ("Enter The Time In Minutes:\n")
print()
int_minutes = int(str_minutes)
int_hours = int_minutes // 60
refund_minutes = int_minutes % 60
str_result_minutes = str(refund_minutes)
str_hours = str(int_hours)
print("That Equals to " + str_hours + " hours" + " and " + str_result_minutes + " Minutes")
print()
print()