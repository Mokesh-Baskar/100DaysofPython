#lets create a cipher program which encrypts and decrypts the word the user inputs
#These type of comes under Cyptrography where the data is changed into a different form so that only the intended person with right key can decrypt it and read
#lets implement a basic encryption where the letters in the words are moved by the encryption key the user inputs eg: A moved by 3 position is D

userinput = input("Please enter the word to be encrypted : ")

encryptionkey = int(input("Please enter the encryption number between 1 to 26 : "))

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def encrypt(original_text,key):
    entext = ""
    for letter in original_text:
        #lets find the position of each letter in the list 
        position = alphabets.index(letter)
        #since there are 26 letters i.e 26 items in the list we need to do modulo so that there wont be index error when adding the key will make the index out of bound error
        position = (position+key)%26
        #concat each changed letter 
        entext+= alphabets[position]
    return(entext)

def decrypt(encrypted_text,key):
    detext = ""
    for letter in encrypted_text:
        position = alphabets.index(letter)
        #In python the negative position will pick the items from last so modulo is not needed , just find the position letter and concat
        detext+= alphabets[position-key]
    return(detext)


encrypted_text = encrypt(userinput,encryptionkey)

print(f"Please find the encrypted word : {encrypted_text} \n")

decrypted_text = decrypt(encrypted_text,encryptionkey)

print(f"Please find the encrypted word : {decrypted_text} \n")