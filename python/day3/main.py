# age = int(input("Enter your age: "))

# if age >= 18:  # Outer if
#     membership = input("Are you a member? (yes/no): ").strip().lower()
#     if membership == "yes":  # First inner if
#         access_level = input("Do you have premium, basic, or trial membership? ").strip().lower()
#         if access_level == "premium":  # Second inner if
#             special_permission = input("Do you have admin privileges? (yes/no): ").strip().lower()
#             if special_permission == "yes":  # Third inner if
#                 print("Welcome, Admin! You have full access to all premium and administrative features.")
#             else:  # Third inner else
#                 print("Welcome to the premium plan! Enjoy your exclusive features.")
#         elif access_level == "basic":
#             feature_request = input("Do you want to upgrade to premium? (yes/no): ").strip().lower()
#             if feature_request == "yes":  # Nested if for basic plan
#                 print("Please visit our website to upgrade to premium.")
#             else:
#                 print("Enjoy the basic plan with limited features.")
#         elif access_level == "trial":
#             days_left = int(input("How many trial days are left? "))
#             if days_left > 0:  # Nested if for trial plan
#                 print(f"You have {days_left} days left. Explore the features before your trial ends!")
#             else:
#                 print("Your trial has expired. Consider becoming a member.")
#         else:  # Second inner else
#             print("Invalid membership type entered.")
#     else:  # First inner else
#         print("You need to be a member to access this service.")
# else:  # Outer else
#     print("You must be at least 18 years old to apply.")

# num = int(input("What is the number you wish to check? "))
# if num % 2 == 0 :
#     print("Number is an even number")
# else:
#     print("Number is odd")

# print("Welcome to python Pizza Deliveries!")
# bill = 0
# small_size = 15
# mediup_size = 20
# large_size = 25
    

# pizza_choice = input("for extra $2 or $3 do you want a pepperoni added pizza?(y/n) ")

    
# cheese_addons = input("for an extra $1 do you want extra cheese?(y/n) ")
# if cheese_addons.lower() == "y":
#     bill+=1


# pizza_size = input("What size do you want?(s for small = $15, m for medium = $20 and l for large = $25) ")
# if pizza_size.lower() == "s" :
#     if pizza_choice.lower() == "y":
#         bill+=small_size+2
#     else:
#         bill+=small_size
#     print(f"Your total bill is ${bill}")
# elif pizza_size.lower() == "m" :
#     if pizza_choice.lower() == "y":
#         bill+=mediup_size+3
#     else:
#         bill+=mediup_size
#     print(f"Your total bill is {bill}")
# else:
#     if pizza_choice.lower() == "y":
#         bill+=large_size + 3
#     else:
#         bill+=large_size
#     print(f"Your total bill is {bill}")

# PROJECT THREE: TREASURE ISLAND GAME
print("Welcome to Treasure Island your mission is to find the treasure!")
cross_road = input("You are at a crossroad. pick a path left or right?\n   ")
if cross_road.lower() == "left":
    move_to_lake = input("You've come to a lake. There's an island in the middle of the lake,\n type 'swim' to swim across or 'wait' to wait for a boat? ")
    if move_to_lake.lower() == 'swim':
        print("You met an Electric eel, and it shocked you off the game....Game Over!!!")
    elif move_to_lake.lower() == 'wait':
        color_choice = input("Hurray!!! You made it across the lake.\n Here are three pick pick any one to decide your fate (yellow, red, or blue): ")
        if color_choice.lower() == 'red':
            print("You picked the fire pill...Sorry, You got burnt...Game Over!!!")
        elif color_choice.lower() == 'Yellow':
            print("You picked the treasure pill...Hurray, You found the treasure...congrats!!!")
        elif color_choice.lower() == 'blue':
            print("You picked the beast feast pill...Sorry, You got eaten by beasts...Game Over!!!")
        else:
            print("Invalid Input....Game ends!!!")
elif cross_road.lower() == "right":
    print("Sorry mate You fell into a hole. Game Over!!!")
else:
    print("Invalid Input....Game ends!!!")

