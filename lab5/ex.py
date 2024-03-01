import re

def match_pattern(string):
    pattern = r'a*b*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False


test_strings = ["ab", "abb", "a", "aaa", "b", "c", "abab", "abbbb"]
for test_string in test_strings:
    print(f"String: {test_string}, Match: {match_pattern(test_string)}")