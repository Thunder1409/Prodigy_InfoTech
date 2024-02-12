def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        letter = text[i]
        # print(letter)
        result += chr(ord(letter) + s * 10 % 26 + 65)
    print("Encrypted text-: ", result)
    return result
def decrept(enc_pass, s):
    result = ""
    for i in range(len(enc_pass)):
        letter = enc_pass[i]
        result += chr(ord(letter) - s * 10 % 26 - 65)
    print("Decrypted text-: ", result)

s = 10
while True:
    print("1. Encryption \n2. Decryption \n\n99. Exit")
    to_do = int(input("Wnat you want to do -: "))

    if to_do == 1:
        password = input("Enter the text -: ")
        encrypt(password, s)
    elif to_do == 2:
        enc_password = input("Enter the encryptrd text -: ")
        decrept(enc_password, s)
    elif to_do == 99:
        break
    else:
        print("Wrong Input....")

    print("\n\n")