'''
#Erika Fortune
10.2.17
Purpose: To to tell a customer their meal order depending on their choices
'''



meal=int(input("Choose an entree 1. Fish and vegetables, 2. Steak and baked potato or 3. Burger and fries:"))
age=input("Are you 21 or older?(y/n)")

if (meal==1):
    if (age=="y"):
        drink=input("Iced tea(t) or white wine (w)?")
        if (drink=="t"):
            print("Order: Fish and vegetables with ice tea")
        elif(drink=="w"):
            print("Order: Fish and vegetables with white wine")
    else:
          print("Order: Fish and vegetables with ice tea")
if (meal==2):
    if (age=="y"):
        drink=input("lemonade(L) or red wine (w)?")
        if (drink=="L"):
            print("Order: Steak and baked potato with lemonade")
        elif(drink=="w"):
            print("Order: Steak and baked potato with red wine")
    else:
          print("Order: Fish and vegetables with lemonade")
if (meal==3):
    if (age=="y"):
        drink=input("cola(c) or beer(b)?")
        if (drink=="c"):
            print("Order: Burger and fries with cola")
        elif(drink=="b"):
            print("Order: Steak and baked potato with beer")
    else:
          print("Order: Fish and vegetables with cola")
