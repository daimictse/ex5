from sys import argv

script, text_file = argv

text = open(text_file)
text_read = text.read()

text_read = text_read.lower()
list_of_letter = [0] * 26

for char in text_read:
    # only tracks alphabets a to z
    if (ord(char) in range(97, 123)):
        list_of_letter[ord(char)-97] += 1


for item in list_of_letter:
    print item

text.close()