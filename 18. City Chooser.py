print("Area Chooser")
print("~~~~~~~~~~~~")
print()
print("Our Branches Are in Cairo and Alexandria and Aswan and Hurghada")
print()
input_area = input ("Enter The Name Of Your Country:\n")
print()
if input_area.upper() == "CAIRO" or input_area.upper() =="ALEXANDRIA"or input_area.upper() =="ASWAN" or input_area.upper() =="Hurghada":
    print("Our Branch In " + input_area.lower() + " is Here For Your Service")
else:
    print(f"Sorry {input_area} is not on our List")
print()
print()



