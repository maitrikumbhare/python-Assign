user_bio = 'Music lover | Foodie | Traveller'

char_count = 0

for char in user_bio:
    if char != ' ':
        char_count += 1

print("Number of characters (excluding spaces):", char_count)