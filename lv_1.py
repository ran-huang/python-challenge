"""
challenge = input("Code: ")
decoded_string = ''
special_chars = [',', '.', ' ', '\'', '(',')']
for char in challenge:
    if char in special_chars:
        decoded_string += char
    else:
        if ord(char) < 121:
            decoded_string += chr(ord(char)+2)
        else:
            decoded_string += chr(ord(char)-24)

print(decoded_string)
"""

# try string.maketrans()

origin = input("Decode this: ")
Decoding = origin.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print(origin.translate(Decoding))
