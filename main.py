def encrypt(text,s):
    result = ""


    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def decrypt(text,s):
    result = ""


    for i in range(len(text)):
        char = text[i]


        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)


        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result

text = input("Input Text: ")
s = int(input("Input Key / Shift: "))
mode = int(input("input [1] for cypher and [2] for decypher"))

if mode == 1:
  print(f"Text: {text}")
  print(f"Shift: {str(s)}")
  print(f"Result: {encrypt(text,s)}")
elif mode == 2:
  print(f"Text: {text}")
  print(f"Shift: {str(s)}")
  print(f"Result: {decrypt(text,s)}")
else:
    print("WRONG INPUT.")