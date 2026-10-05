user_input = input("Enter a word or song name: ")

for char in user_input:
    lower_char = char.lower()
    
    if lower_char == 'a' or lower_char == 'e' or lower_char == 'i' or lower_char == 'o' or lower_char == 'u':
        print(char)