def hill_cipher_encrypt(plaintext):
    """this is the key resembling as HILL as
    { H  I
      L  L }
    """

    key = [[7, 8],
           [11, 11]]
    length = len(plaintext)
    ciphertext = ""
    i = 0
    space = []
    plaintext_ws = ""
    for i in range(length):
        if(plaintext[i] == " "):
            space.append(i)
        else:
            plaintext_ws = plaintext_ws + plaintext[i]
    length_ws = len(plaintext_ws)
    i = 0
    while i <= length_ws - 2:

        char1 = numeric_equivalent(plaintext_ws[i])
        char2 = numeric_equivalent(plaintext_ws[i + 1])
        diagraph = [[char1], [char2]]

        char1_eq = (7 * char1 + 8 * char2) % 26
        char2_eq = (11 * char1 + 11 * char2) % 26
        # print(char1,char2)

        #print("char 1",chr(char1_eq+ord('A')))
        #print(" char 2", chr(char2_eq+ord('A')))
        ciphertext = ciphertext + \
            chr(char1_eq + ord('A')) + chr(char2_eq + ord('A'))
        i = i + 2
    for i in space:
        ciphertext = ciphertext[0:i] + " " + ciphertext[i:]
    return ciphertext, space


def hill_cipher_decrypt(ciphertext, space):

    determinant = 15
    multiplicative_inverse = 0
    for i in range(26):
        if (determinant * i) % 26 == 1:
            multiplicative_inverse = i
    adjoint_matrix = [[11, 18], [15, 7]]
    for row in adjoint_matrix:
        for col in row:
            col = (col * multiplicative_inverse) % 26
            #print("col ",col)
    # so K inverse is [[25 , 22 ],[1,23]
    # as K was [[7 ,8 ],[11,11]]
    # now to decrypt we can simply muliply this with ciphertext elements
    ciphertext_ws = ""
    # removing spaces in cipher text
    for char in ciphertext:
        if(char == " "):
            continue
        else:
            ciphertext_ws = ciphertext_ws + char
    print("ciphertext :", ciphertext_ws)
    # now decrypting
    plaintext = ""
    # using k inverse * [[char1],[char2]]
    length_ws = len(ciphertext_ws)
    i = 0
    while i <= length_ws - 2:
        char1 = numeric_equivalent(ciphertext_ws[i])
        char2 = numeric_equivalent(ciphertext_ws[i + 1])
       # print("char ",char1," ",char2)
        char1_eq = (25 * char1 + 22 * char2) % 26
        char2_eq = (char1 + 23 * char2) % 26

        plaintext = plaintext + \
            (chr(char1_eq + ord('A'))) + chr(char2_eq + ord('A'))
        i = i + 2
    for i in space:
        plaintext = plaintext[0:i] + " " + plaintext[i:]

    return plaintext


def numeric_equivalent(char):
    return ord(char) - ord('A')


def main():
    plaintext = input("enter the message to encrypt\n").upper()
    ciphertext, space = hill_cipher_encrypt(plaintext)
    print(f"encrypted message :{ciphertext}\n")
    print(f"decrypted text :{hill_cipher_decrypt(ciphertext,space)}\n")


# program entry point
if __name__ == "__main__":
    main()