class Cipher:
    # encryption function
    def affine_cipher_encrypt(text, key):

        return ''.join([chr(((key[0] * (ord(i) - ord('A')) + key[1]) %
                       26) + ord('A')) for i in text.upper().replace(' ', '')])

    def affine_cipher_decrypt(cipher, key):

        return ''.join([chr(((Util.inverse(key[0], 26) *
                              (ord(alphabet) -
                               ord('A') -
                               key[1])) %
                             26) +
                            ord('A')) for alphabet in cipher])


class Util:
    # finding gcd

    def extended_gcd(x, y):
        a, b, m, n = 0, 1, 1, 0
        while x != 0:
            f, k = y // x, y % x
            u, v = a - m * f, b - n * f
            y, x, a, b, m, n = x, k, m, n, u, v
        gcd = y
        return gcd, a, b

    # finding inverse

    def inverse(s, n):
        gcd, p, q = Util.extended_gcd(s, n)
        if gcd != 1:
            return None
        else:
            return p % n


def main():

    plaintext = input('enter text :').upper()
    key = [3, 7]

    # encrypting
    ciphertext = Cipher.affine_cipher_encrypt(plaintext, key)

    print(f"Encrypted Text: {Cipher.affine_cipher_encrypt(plaintext,key)}")

    # decrypting
    print(f"Decrypted Text:{Cipher.affine_cipher_decrypt(ciphertext, key)}")


if __name__ == '__main__':
    main()