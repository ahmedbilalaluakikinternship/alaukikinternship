# restaurant system 
print("=================================")
print("WELCOME TO BILAL RESTAURANT")
print("=================================")

print("HOW CAN I HELP YOU?")

print("--------MENU--------")

print("1. pizza 200₹")
print("2. biryani 220₹")
print("3. butter chicken 350₹")
print("4. shawerma 80₹")
print("5. chicken burger 150₹")

print("---------------------")


order = input("Please Enter your order:").lower()
print("your order: ", order)


price = 0

if (order == "pizza"):
    price= 200 
elif (order == "biryani"):
    price = 220
elif (order == "butter chicken") :
    price = 350
elif (order == "shawerma"): 
    price = 80 
elif (order == "chicken burger") :
    price = 150
else:
    print("Sorry ! item not avaliable.")

print("price is :",price)

quantity = int(input("how many items you wants..: "))
total = quantity * price
print("----------------------")
print("your actual total is :", total)

discount = 0
if(total >= 1000):
    print("Congratulations you got specail 10% off")
    discount = total * 10 / 100
else:
    print("no Discount applied")

final_price = total - discount
print("and now your final total is :", final_price)


print("Thank you ❤")
print("visite again ☺")
print("=======================")