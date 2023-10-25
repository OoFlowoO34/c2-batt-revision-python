import re

print("url du fichier: ")
url =  input()

fichier = open(url, "r")
text = fichier.read()

with open("exo/result.txt", "w") as result:
    result.write(text)
    
words = re.findall(r'\b\w+\b', text)

print(len(words))



