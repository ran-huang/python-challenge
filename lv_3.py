import re

text = ""
with open("lv_3_source.txt") as file_obj:
    for line in file_obj.readlines():
        text += line

print(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",text))
