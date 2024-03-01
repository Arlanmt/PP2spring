import re

pattern = re.compile(r'ab*')

# Test
test_string = "abbb"
if pattern.fullmatch(test_string):
    print("Match")
else:
    print("No match")
 