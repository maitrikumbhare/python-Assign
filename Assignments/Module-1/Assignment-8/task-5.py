def mask_phone_number(phone):
    # Take the last 4 digits
    last_four = phone[-4:]
    
    # Replace the first 6 digits with *
    return "******" + last_four


# Example
phone = input("Enter 10-digit phone number: ")
print("Masked phone number:", mask_phone_number(phone))