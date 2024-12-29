# # The Print function takes parameters and displays them on the terminal
# print("Hello World!\n")

# # Printing exercise
# # print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
# # print("2. Knead the dough for 10 minutes.")
# # print("3. Add 3g of Salt.")
# # print("4. Leave to rise for 2 hours.")
# # print("5. Bake at 200 degrees C for 30 minutes.")

# # Instead of writing every statement you can use the backslash character "\n"
# # print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")

# # String Concatenation is the joining of strings using the plus sign "+" remember to always add a wen using string concaternation

# print("Hello" + "your name\n") # without space
# print("Hello" +" "+ "your name") # withspace

# # Using the input Function
# # this collects values from the terminal or output in form of a string data type
# input("What's your name? ")
# print("Hello " + input("What's your name? ")) #hello yourname


# # Excercise

# # Variables
# # We have 2 variables glass1 and glass2. 
# # glass1 contains milk and glass2 contains juice.
# # Write 3 lines of code to switch the contents of the variables. 
# # You are not allowed to type the words "milk" or "juice". 
# # You are only allowed to use variables to solve this exercise.

# # Answer
# # glass1 = "milk"
# # glass2 = "juice"
# # glass1, glass2 = glass2, glass1
# # print(glass1, glass2)

# # Project 1: BANDNAME GENERATOR 
print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in? \n")
pet_name = input("What's your pet's name? \n")
print("Your band name could be " + city_name +" "+ pet_name) 