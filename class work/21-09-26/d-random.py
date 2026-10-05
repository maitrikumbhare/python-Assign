import random
lucky = random.randint(1, 50)

l =[435889,2558776,775689084,7676840987]
lucky = random.choice(l)
print(lucky)

lucky = random.randint(1, 50)

while True:
    print("*******Enter number between 1 to 50*******")

    choice = int(input("enter your choice: "))

    if choice>50:
        print("Invalid number!!")
        break
    elif choice==lucky:
        print("you are lucky!!")
        break
    elif lucky>choice:
        print("your number is less than lucky number!!")
    
    else:
        print("your number is greater than lucky number!!")
    