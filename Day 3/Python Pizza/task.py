print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total = 0
if size == "S": total += 15
elif size == "M": total += 20
elif size == "L": total += 25
else: print("error")

if pepperoni == "Y":
    if size == "S": total += 2
    else: total += 3
elif pepperoni == "N": total += 0
else: print("error")

if extra_cheese == "Y": total += 1
elif extra_cheese == "N": total += 0
else: print("error")

print(f"Your final bill is: ${total}.")