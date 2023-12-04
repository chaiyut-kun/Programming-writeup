import re

prototype = input("")
upper = prototype.upper()
lower = prototype.lower()

if prototype == upper:
    print("All Capital Letter")

elif prototype  == lower:
    print("All Small Letter")
else:
    print("Mix")