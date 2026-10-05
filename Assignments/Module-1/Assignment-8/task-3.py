def reverse_message(message):
    reversed_message = ""

    # Reverse the string using a loop
    for i in range(len(message) - 1, -1, -1):
        reversed_message += message[i]

    return reversed_message


# Example
message = input("Enter your message: ")
print("Reversed message:", reverse_message(message))