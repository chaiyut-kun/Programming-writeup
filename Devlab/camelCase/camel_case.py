import re 

word = input()

regex = re.split("[-_?.]",word)
if "" in regex:
    regex.remove("")

clean_word = [word.lower() if index == 0 else word.title() for index , word in enumerate(regex) ]
print("".join(clean_word))