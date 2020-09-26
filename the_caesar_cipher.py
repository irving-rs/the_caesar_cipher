#the_caesar_cipher.py
#Date: 25/September/2020
#by irving-rs

#Description:
#The Caesar Cipher: A famous cypher that encrypts/decrypts plaintext.

#Basics:
#The written letter experience a shift (change of position). For example,
#if we shift letter "A" one position then it it will be converted into a "B".
#The user wil select the magnitude of the shift (measured in number of positions).
#The shift displacement will vary between 1 and 25.

#Functions:
def shift(key, letter): #Makes the translation of positions.
    if letter.isupper(): #If it is an uppercase.
        suma = ord(letter) + key
        if suma > 90:
            return chr((suma%90)+64)
        else:
            return chr(suma)
    elif letter.islower(): #If it is a lowercase.
        suma = ord(letter) + key
        if suma > 122:
            return chr((suma%122)+96)
        else:
            return chr(suma)
    else: #Not a letter of the alphabet.
        return letter
        
def cypher(key, text): #Cyphers the text and prints the result.
    for i in range(len(text)):
        print( shift(key, text[i]), end="" )

#Variables:

#Presentation of the game:
print("\nThe Caesar Cipher:\n")

#Description:
print("Description:")
print("1. This cypher/decypher only processes alphabet characters.")
print("2. The key number (shift) must be between 1 and 25.\n")

#Menu:
print("Menu:\n")
print("1) Encrypt.")
print("2) Decrypt using key.")
print("3) Decrypt using brute force.")
print("\nEnter any other number to exit.\n")

sel = int(input("Choose your selection: "))

if sel == 1: #If the user wants to encrypt.
    #Reading the plaintext:
    print("\nWrite your message:")
    text = input()

    #Setting the key:
    key = int(input("\nEnter the key number: "))

    #Cyphering:
    print("\nThe message has been encrypted:")
    cypher(key, text)
    
elif sel == 2: #If the user wants to decrypt using key.
    #Reading the plaintext:
    print("\nWrite the encrypted message:")
    text = input()

    #Setting the key:
    key = int(input("\nEnter the key number: "))

    #Decyphering:
    print("\nThe message has been decrypted:")
    cypher(26-key, text)
    
elif sel == 3: #If the user wants to decrypt using brute force.
    #Reading the plaintext:
    print("\nWrite the encrypted message:")
    text = input()

    #Decyphering using brute force (using all the valid keys):
    print("\nThe message has been decrypted using brute force:")
    for i in range (25, 0, -1):
        print("\n",26-i, ". ", sep="", end="")
        cypher(i, text)

else: #If the user wants to exit.
    print("\nSee you later\n")
