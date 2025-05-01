def reverse_string(s):
    reversed_string = ""
    for i in range(len(s) -1, -1, -1):
        reversed_string += s[i]
    return reversed_string

def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

def is_palindrome(s):
    processed_s = ""
    for char in s:
        lower_char = char.lower()
        if lower_char.isalnum():
            processed_s += lower_char
    return processed_s == processed_s[::-1]
        