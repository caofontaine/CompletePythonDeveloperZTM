import re

pattern = re.compile(r'^[a-zA-Z0-9$%#@]{8,}$')
string = 'Secure1#'

a = pattern.fullmatch(string)
print(a)