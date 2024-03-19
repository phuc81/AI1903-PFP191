def replace_chars(input_str, char1, char2):
    return input_str.replace(char1, char2)
user_input = input("Enter a string: ")
char1 = input("Enter the first character: ")
char2 = input("Enter the second character: ")
result = replace_chars(user_input, char1, char2)
print("Output:", result)
