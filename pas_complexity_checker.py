import string


def rules():
    rule_list = ["Lowercase character (Y/N) -: ", "Upercase character (Y/N) -: ", "Special character (Y/N) -: ", "Numbers (Y/N) -: "]
    yes_no = {}
    for rule in rule_list:
        while True:
            a = input(rule)
            if (a == "Y" or a == "y" or a == "N" or a == "n"):
                rule = rule.replace(" (Y/N) -: ", "")
                if ("character" in rule):
                    rule = rule.replace(" character", "")
                yes_no[rule.lower()] = a.lower()
                break
            else:
                print("Wrong input\n")
    return yes_no

def complexity(rules, length):
    password = input("\nEnter your password -: ")
    if (len(password) < length):
        print("Small password")
    else:
        upper, lower, number, special_char = False, False, False, False
        special = string.punctuation
        comp = 0
        for i in range(len(password)):
            word = password[i]
            if (word.isupper() and rules["upercase"] == "y") or (word.islower() and rules["lowercase"] == "y") or (word.isnumeric() and rules["numbers"] == "y") or (word in special and rules["special"] == "y"):
                if (word.isupper()):
                    upper = True

                elif(word.islower()):
                    lower = True

                elif(word.isnumeric()):
                    number = True

                elif(word in special):
                    special_char = True

            else:
                print("Invalid password [Out of rules]")
                break

        if(upper and lower and number and special_char):
            print(password, "-: is Strong")

        elif(upper or lower) and (number or special_char):
            print(password, "-: is Moderate")

        else:
            print(password, "-: week password")







print("-------RULES-------")
length = int(input("Minimum length of password -: "))
complexity(rules(), length)


