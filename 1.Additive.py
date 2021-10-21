#encryption function 
def additive_cipher_encrypt(string):
    additive=6
    cipher=""
    for char in string:
        if(char == ' '):
            cipher = cipher + " "
        else:    
            cipher=cipher+chr((ord(char)+additive-ord('A'))%26+ord('A')) 
        
    return cipher  



#decrypting function 
def additive_cipher_decrypt(string):
    additive=6
    plaintext=""
    for char in string:
        if(char == ' '):
           plaintext =plaintext + " "
        else:
            plaintext=plaintext+chr((ord(char)-additive+ord('A'))%26+ord('A'))
            
    return plaintext   



def main():
	#taking input from the user 
    text=input("enter the text to cipher\n").upper()
    #generating cipher text
    ciphered_text=additive_cipher_encrypt(text)
    print("ciphered text ",ciphered_text)
    #decrypting cipher text
    print("deciphered text :",additive_cipher_decrypt(ciphered_text))

#program entry point 
if __name__ == "__main__":
    main()