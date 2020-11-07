raw = ''
while True:
    single_line = input()
    if single_line != 'q':
        raw += single_line
    else:
        break

character_dict = {}
for char in raw:
    if char in character_dict.keys():
        character_dict[char] += 1
    else:
        character_dict[char] = 1

sorted_character_dict = sorted(character_dict.items(), key=lambda x:x[1])

for key, value in sorted_character_dict:
    print(f"The character {key} has shown {value} times.")
