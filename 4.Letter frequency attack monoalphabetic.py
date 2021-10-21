# function to print possible outcomes
def findPossibleString(Text, length, totalPossibleOutcomes):

    letterFrequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    outcome = [None] * totalPossibleOutcomes  # number of outcomes string

    # count of every alphabet
    count = [0] * 26

    for i in range(length):
        if Text[i] != ' ':
            count[ord(Text[i]) - 65] += 1

    # sorted count array
    sortedCount = [None] * 26
    for i in range(26):
        sortedCount[i] = count[i]
    sortedCount.sort(reverse=True)

    taken = [0] * 26  # to keep check if value is taken before

    # loop from 0 till totalPossibleOutcomes
    for i in range(totalPossibleOutcomes):
        position = -1

        # loop from 0 to 26
        for j in range(26):
            # finding most frequent letter that is not taken before
            if sortedCount[i] == count[j] and taken[j] == 0:
                taken[j] = 1  # setting this element to taken already
                position = j
                break

    # if no such element found
        if position == -1:
            break

    # integer value after shift
        shift = ord(letterFrequency[i]) - 65 - position

    # finding one of totalPossibleOutcomess
        oneOfOutcome = ""
        for iterator in range(length):
            if Text[iterator] == ' ':  # ignore whitespace
                oneOfOutcome += " "
                continue

            possibleOriginalAlphabet = ord(Text[iterator]) - 65 + shift

            if possibleOriginalAlphabet < 0:
                possibleOriginalAlphabet += 26
            if possibleOriginalAlphabet > 25:
                possibleOriginalAlphabet -= 26

            # adding letter
            oneOfOutcome += chr(possibleOriginalAlphabet + 65)

        outcome[i] = oneOfOutcome

    # printing result
    for i in range(totalPossibleOutcomes):
        print(f"Result ={outcome[i]}")

 # encryption function o


def additive_cipher_encrypt(Text):
    additive = 6
    cipher = ""
    for char in Text:
        if(char == " "):
            cipher = cipher + " "
        else:
            cipher = cipher + \
                chr((ord(char) + additive - ord('A')) % 26 + ord('A'))
    return cipher


# driver code
def main():
    Text = input("Enter text: ").upper()  # input text

    cipher = additive_cipher_encrypt(Text)  # encrypting

    print("**********")
    # printing plain text and its cipher
    print(f"Plain Text = {Text}\nCipher Text = {cipher}")

    totalPossibleOutcomes = 10
    while(True):
        # input possible text outcome
        totalPossibleOutcomes = int(
            input("Enter possible outcomes you want NOT MORE THAN 26 : "))
        if(totalPossibleOutcomes > 26):
            print("Value should not be more than 26")
        else:
            break
    length = len(Text)
    findPossibleString(cipher, length, totalPossibleOutcomes)


if __name__ == "__main__":
    main()