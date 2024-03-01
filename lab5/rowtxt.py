import re

def match_pattern_1(string):
    pattern = re.compile(r'ab*')
    return bool(pattern.match(string))

# Example usage:
test_string = "abb"
result = match_pattern_1(test_string)
print(result)  # Output: True




import re

def match_pattern_2(string):
    pattern = re.compile(r'ab{2,3}')
    return bool(pattern.search(string))

# Example usage:
test_string = "abb"
result = match_pattern_2(test_string)
print(result)  # Output: False




import re

def find_lowercase_sequences(string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    return pattern.findall(string)

# Example usage:
test_string = "abc_def_ghi"
result = find_lowercase_sequences(test_string)
print(result)  # Output: ['abc_def', 'ghi']




import re

def find_uppercase_sequences(string):
    pattern = re.compile(r'[A-Z][a-z]+')
    return pattern.findall(string)

# Example usage:
test_string = "HelloWorld ExampleText"
result = find_uppercase_sequences(test_string)
print(result)  # Output: ['Hello', 'World', 'Example', 'Text']





import re

def match_pattern_5(string):
    pattern = re.compile(r'a.*b$')
    return bool(pattern.match(string))

# Example usage:
test_string = "aXYZb"
result = match_pattern_5(test_string)
print(result)  # Output: True




def replace_spaces_commas_dots(string):
    return re.sub(r'[ ,.]', ':', string)

# Example usage:
test_string = "a, b. c d"
result = replace_spaces_commas_dots(test_string)
print(result)  # Output: "a:b:c:d"




def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

# Example usage:
snake_case_str = "my_snake_case_string"
camel_case_str = snake_to_camel(snake_case_str)
print(camel_case_str)  # Output: "mySnakeCaseString"





def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

# Example usage:
test_string = "SplitThisString"
result = split_at_uppercase(test_string)
print(result)  # Output: ['Split', 'This', 'String']




def insert_spaces_before_capital(string):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', string)

# Example usage:
test_string = "InsertSpacesHere"
result = insert_spaces_before_capital(test_string)
print(result)  # Output: "Insert Spaces Here"




