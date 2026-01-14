# print("Code Rail")
# Name=input("Enter your Name-->")
# Age=int(input("Enter your Age-->"))
# travel_class=input("Enter your Travel Class \n 1: First Class \n 2: Second Class \n 3: Sleeeper Class \n Enter Choice (1/2/3): ")
# price=0
# class_name="Enter Class Name"
# if travel_class=="1":
#     price=1500
#     class_name="First Class"
# elif travel_class=="2":
#     price=1000
#     class_name="Second Class"
# elif travel_class=="3":
#     price=500
#     class_name="Sleeper Class"
# else:
#     print("Invalid Class")

# discount="0"
# if Age<=5:
#     discount_price=price
#     discount="100%"
#     print("Free")
# elif Age>5 and Age<=60:
#     discount_price=0
#     discount="No Discount"
#     print("Full Ticket")
# elif Age>60:
#     discount_price=(price*20)/100
#     discount="20% off"
#     print("20% off")
# else:
#     print("Invalid")
# total_price=price-discount_price
# discount_price=total_price

# meal_price=0
# item_included="Item Included"


# meal=input("Do you want to include a meal? (Yes/No):")
# if meal=="yes":
#     meal_price=200
#     item_included="yes"
#     extra_charges="200 Extra"
# elif meal=="no":
#     meal_price=0
#     item_included="no"
#     extra_charges="No Extra Charges"

# final_price=total_price+meal_price

# print("\n------ Ticket Summary ------")
# print("Name:",Name)
# print("Age:",Age)
# print("Travel Class:",class_name)
# print("Price:",price)
# print("Discount:",discount)
# print("Meal Added:",item_included)
# print("Extra Charges For Meal:",extra_charges)
# print("Total Price:",final_price)
# print("----------------------------")



# print("Welcome to Burger King")

# print("-----Our Menu-----\n"
#     "1:Whooper Burger -- 150\n" 
#     "2:Crispy Veg -- 100\n"
#     "3:Chicken Wing -- 120"
# )
# price1 = 150
# price2 = 100
# price3 = 120

# choice = int(input("Enter item number (1-3): "))
# quantity = int(input("Enter quantity: "))

# if choice == 1:
#     item_name = "Whopper Burger"
#     total = price1 * quantity
# elif choice == 2:
#     item_name = "Crispy Veg"
#     total = price2 * quantity
# elif choice == 3:
#     item_name = "Chicken Wings"
#     total = price3 * quantity
# else:
#     print("Invalid choice")
#     total = 0

# coupon = input("Enter coupon code--> ")
# discount=0
# if coupon == "KING50":
#     print("Coupon Code Successfuy Applied")
#     discount = (total * 50)/100 
# elif coupon == "BK20":
#     print("Coupon Code Successfuy Applied")
#     discount = 20
# elif coupon == "NOCOUPON":
#     discount = 0
# else:
#     print("Invalid coupon code")

# final_bill = total - discount

# # Display Bill
# print("\n🧾 FINAL BILL")
# print("Item:", item_name)
# print("Quantity:", quantity)
# print("Total Price: ₹", total)
# print("Discount: ₹", discount)
# print("Amount to Pay: ₹", final_bill)



# print("Welcome to Burger King")
# menu=input("Menu: \n 1: Wooper Burger \n 2: Crispy Veg \n 3: Chicken Wing  \n Enter Choice (1/2/3):")
# quantity=int(input("Item Quantity:"))
# coupon=input("Do you Have Coupon Code?(Yes or No):")
# discount="0"
# price=0 #default value
# item="Burgers"

# if menu=="1":
#     item="Wopper Burger"
#     price=150
# elif menu=="2":
#     item="Crispy Veg"
#     price=100
# elif menu=="3":
#     item="Chicken Wings"
#     price=120
# else:
#     print("Invalid Choice")

# total_price=price*quantity
# discount_price=0
# # discount_price=total_price-discount_price

# if coupon=="yes":
#     code=input("Enter Coupon Code: ")
#     if code=="KING50":
#         discount="50%"
#         discount_price=(total_price*50)/100
#     elif code=="BK20":
#         discount="RS. 20 off"
#         discount_price=20
#     elif code=="NOCODE":
#         discount="0"
#         discount_price=0
# else:
#     print("INVALID CODE")

# final_bill=total_price-discount_price

# print("\n------ORDER SUMMARY------")
# print("Menu:",menu)
# print("Quantity:",quantity)
# print("Coupon:",coupon)
# print("Item:",item)
# print("Price:",price)
# print("Total Price:",total_price)
# print("Discount:",discount)
# print("Final Bill:",final_bill)
# print("-------------------------")

        
    

