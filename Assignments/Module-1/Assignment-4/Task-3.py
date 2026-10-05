age = int(input("Enter your age: "))
current_time = float(input("Enter current time in 24-hour format (e.g., 23.5 for 11:30 PM): "))

if age >= 18:
    # Nested check: Time condition (crosses midnight)
    if current_time >= 22 or current_time <= 2:
        print("Order allowed")
    else:
        print("Order not allowed")
else:
    print("Order not allowed")