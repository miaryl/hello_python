# Define get_double_alphabet that takes a string argument 
# and concatenates, or combines, the given string with itself as follows:
def get_double_alphabet(alphabet):
    double_alphabet = alphabet + alphabet
    return double_alphabet

print(get_double_alphabet("abc"))

# The next function you define will request a message to encrypt from the user. 
# You will use the built-in function called input().
def get_message():
    str_to_encrypt = input("pls enter a message to encrypt: ")
    return str_to_encrypt





# EX 3
#The cipher key is how far you will shift the letters. 
#By using two alphabets, you can have a cipher key that is any integer from 1 to 25. 
#Don’t count the key at index 26 because that key would shift you back to the original message.

def get_cipher_key():
    shift_amount = input("pls enter a key (Whole number from 1-25): ")
    return shift_amount



# EX 4
def encrypt_message(message, cipher_key, alphabet):
    encrypted_message = ""
    uppercase_message = ""
    uppercase_message = message.upper()
    for current_character in uppercase_message:
         position = alphabet.find(current_character)
         new_position = position + int(cipher_key)
         if current_character in alphabet:
                encrypted_message = encrypted_message + alphabet[new_position]
         else:
                encrypted_message = encrypted_message  + current_character
    return encrypted_message

# EX 5
# write a decryptMessage() function by reusing the encrypt_message(). 
#For this simple encryption, you can undo the encryption by shifting each letter back. 
#Thus, instead of adding the cipher key, you will subtract the cipher key. 
#To avoid rewriting most of the logic, you will pass in a negative cipher key.
def decrypt_message(message, cipher_key, alphabet):
     decrypt_key = -1 * int(cipher_key)
     return encrypt_message(message, decrypt_key, alphabet)

# EX 6 CREATING A MAIN FUNCTION
#You have built a collection of user-defined functions that will help you write a Caesar cipher program. The main logic of the program will, of course, also be contained in a function.
def run_caesar_cipher_program():
     my_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     print(f'Alphabet: {my_alphabet}')
     my_alphabet2 = get_double_alphabet(my_alphabet)
     print(f'Alphabet2: {my_alphabet2}')
     my_message = get_message()
     print(my_message)
     my_cipher_key = get_cipher_key()
     print(my_cipher_key)
     my_encrypted_message = encrypt_message(my_message, my_cipher_key, my_alphabet2)
     print(f'Encrypted Message: {my_encrypted_message}')
     my_decrypted_message = decrypt_message(my_encrypted_message, my_cipher_key, my_alphabet2)
     print(f'Decrypted Message: {my_decrypted_message}')

run_caesar_cipher_program()

run_caesar_cipher_program()



