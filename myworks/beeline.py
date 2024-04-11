import re

text = "+77012345678, 87771234567, +7 701 234 56 78, 8 (707) 123 45 67,87056210084"
pattern = r'(?:\+7|8)\s?(?:77|70|71|75)\s?\d{3}\s?\d{2}\s?\d{2}'`

matches = re.findall(pattern, text)
print(matches)
