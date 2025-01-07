# Functions with inputs (Arguements and parameters)


# def greet_with(name, location):
#     print (f"Hello {name}")
#     print(f"How's it like in {location}")


# # positional arguements and parameters 
# greet_with("joshua", "lagos")


# #Keyword arguement 
# greet_with(location="Abuja", name='liam')



# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
    
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
    
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
    
    
#     score = int(str(first_digit) + str(second_digit))
#     print(score)


# def calculate_love_score(name_one, name_two):
#     true_value = 0
#     names = (name_one + name_two).lower()
#     true_list = ["t", "r", "u", "e"]
#     for i in range(len(true_list)):
#         letter_count = names.count(true_list[i])
#         true_value += letter_count
            
#     love_value = 0
#     love_list = ["l", "o", "v", "e"]
#     for i in range(len(love_list)):
#         letter_count = names.count(love_list[i])
#         love_value += letter_count
    
#     final_score = int(str(true_value) + str(love_value))
#     print(final_score)
    
    
# calculate_love_score("Angela Yu", "Jack Bauer")
# JULIUS CEASER CIPHER
def encryption_cipher(message, encrypt_shift):
    encrypted_text = ""
    for each_character in message:
        if each_character.isalpha():
            start = ord('A') if each_character.isupper() else ord('a')
            new_char = chr(start + (ord(each_character) - start + encrypt_shift) % 26)
            encrypted_text += new_char
        else:
            encrypted_text += each_character
    return encrypted_text

def decryption_cipher(message, decrypt_shift):
    decrypted_text = ""
    for each_character in message:
        if each_character.isalpha():
            start = ord('A') if each_character.isupper() else ord('a')
            new_char = chr(start + (ord(each_character) - start + decrypt_shift) % 26)
            decrypted_text += new_char
        else:
            decrypted_text += each_character
    return decrypted_text

def cipher_choice():
    user_crypyt_choice = input("\nDo you want to encrypt or decrypt the message!\nType 'en' for Encrypting and 'de' for decrypting: ").lower()
    if user_crypyt_choice == 'en':
        message = input("\nWhat message do you want to encrypt?\n ")
        encrypt_shift = int(input("\nWhat's your encrypting shift value? \n"))
        encrypted_message = encryption_cipher(message, encrypt_shift)
        print(f"Encrypted text : {encrypted_message}")
    elif user_crypyt_choice == 'de':
        message = input("\nWhat message do you want to decrypt?\n ")
        decrypt_shift = int(input("\nWhat's your decrypting shift value? \n")) * -1
        decrypted_message = decryption_cipher(message, decrypt_shift)
        print(f"decrypted text : {decrypted_message}")
    else:
        print("Invalid option")
        
cipher_choice()
user = False
while not user:
    use_cipher_again = input("Do you want to use the cipher entity again? ").lower()
    if use_cipher_again == 'yes':
        cipher_choice()
    elif use_cipher_again == 'no':
        user = True
        quit()