from sys import argv

def main():
    script, text_file = argv

    text = open(text_file)
    text_read = text.read()
    text.close()

    text_read = text_read.lower()
    list_of_letter = [0] * 26

    for char in text_read:
        char_idx = ord(char) - 97
        # only tracks alphabets a to z
        if char_idx >= 0 and char_idx < 26:
            list_of_letter[char_idx] += 1
        # if (ord(char) in range(97, 123)):
            # list_of_letter[ord(char)-97] += 1

    for item in list_of_letter:
        print item

main()