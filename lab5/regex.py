import re

pattern = re.compile(r'ab*')

# Test
test_string = "abbb"
if pattern.fullmatch(test_string):
    print("Match")
else:
    print("No match")




import re

pattern = re.compile(r'ab{2,3}')

# Test
test_string = "abb"
if pattern.fullmatch(test_string):
    print("Match")
else:
    print("No match")



import re

pattern = re.compile(r'[a-z]+_[a-z]+')

# Test
test_string = "hello_world"
if pattern.fullmatch(test_string):
    print("Match")
else:
    print("No match")





import re

pattern = re.compile(r'[a-z]+_[a-z]+')

# Test
test_string = "hello_world"
if pattern.fullmatch(test_string):
    print("Match")
else:
    print("No match")




import re

pattern = re.compile(r'a.*b$')

# Test
test_string = "aanythingb"
if pattern.fullmatch(test_string):
    print("Match")
else:
    print("No match")




import re

pattern = re.compile(r'[ ,.]')

# Test
test_string = "This is a test, string."
result = pattern.sub(':', test_string)
print(result)




def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case

# Test
snake_case_string = "hello_world_example"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)


import re

pattern = re.compile(r'[A-Z][a-z]*')

# Test
test_string = "SplitThisString"
result = pattern.findall(test_string)
print(result)




import re

pattern = re.compile(r'(?<=[a-z])(?=[A-Z])')

# Test
test_string = "InsertSpacesHere"
result = pattern.sub(' ', test_string)
print(result)




import re

def camel_to_snake(camel_case):
    snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case).lower()
    return snake_case

# Test
camel_case_string = "convertCamelCase"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)




#FFFFFFFFFFFFFFFF
import re

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case


camel_case_string = "ConvertThisCamelCaseStringToSnakeCase"
snake_case_string = camel_to_snake(camel_case_string)
print("Camel case:", camel_case_string)
print("Snake case:", snake_case_string)