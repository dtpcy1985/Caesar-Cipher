# Written By:
# D2L ID:
# Class:
# School:
# Faculty:
# Assignment:
# Purpose: The purpose of this application is to automate the encryption and
# decryption of a phrase via a simple Caesar Cipher.


print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!DISCLAIMER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" +
      "This application is for demonstration purposes only.  It is not meant\n" +
      "to secure communications of any sensitive or protected information.\n" +
      "Please have fun testing the encrytion and decryption of your messages.\n" +
      "!!!!!!!!!!!!!!!!!!!!!!!!!!!!DISCLAIMER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

input("Please press the Enter key to continue after reading the disclaimer")

while True:
    print("1. Encyrpt a plaintext message.")
    print("2. Decrypt a ciphertext message.")
    print("3. Quit Program")

    Choice = int(input("Enter a numerical value 1-3 based on your choice from the options above: "))


    def Encryption():
        print("You chose to encrypt a plaintext message!")
        Plaintext = str(input("Enter your plaintext message for encryption: "))
        EncryptionKey = int(input("Enter your encryption key as an integer value from 1-25: "))
        EncryptedMessage = ''
        for i in Plaintext:
            if i.isupper():
                temp = 65 + ((ord(i) - 65 + EncryptionKey) % 26)
                EncryptedMessage = EncryptedMessage + chr(temp)
            elif i.islower():
                temp = 97 + ((ord(i) - 97 + EncryptionKey) % 26)
                EncryptedMessage = EncryptedMessage + chr(temp)
            else:
                EncryptedMessage = EncryptedMessage + i
        print(("Your input plaintext message is: " + Plaintext).upper())
        print(("Your ciphertext message is: " + EncryptedMessage).upper())


    def Decryption():
        print("You chose to decrypt a ciphertext message!")
        Ciphertext = str(input("Enter a ciphertext message to be decrypted: "))
        DecryptionKey = int(input("Enter your decryption key as an integer value from 1-25: "))
        DecryptedMessage = ''
        for i in Ciphertext:
            if i.isupper():
                if ((ord(i) - 65 - DecryptionKey) < 0):
                    temp = 65 + ((ord(i) - 65 - DecryptionKey + 26) % 26)
                else:
                    temp = 65 + ((ord(i) - 65 - DecryptionKey) % 26)
                DecryptedMessage = DecryptedMessage + chr(temp)
            elif i.islower():
                if ((ord(i) - 97 - DecryptionKey) < 0):
                    temp = 97 + ((ord(i) - 97 - DecryptionKey + 26) % 26)
                else:
                    temp = 97 + ((ord(i) - 97 - DecryptionKey) % 26)
                DecryptedMessage = DecryptedMessage + chr(temp)
            else:
                DecryptedMessage = DecryptedMessage + i
        print(("Your input ciphertext message is: " + Ciphertext).upper())
        print(("Your decrypted plaintext message is: " + DecryptedMessage).upper())


    def QuitProgram():
        print("You chose to quit the program.  Goodbye.")
        quit()


    def Invalid():
        print("You made an invalid selection. Goodbye")
        quit()


    if (Choice == 1):
        Encryption()
    elif (Choice == 2):
        Decryption()
    elif (Choice == 3):
        QuitProgram()
    else:
        Invalid()

