import random
otp = random.randint(1001,9999)
d={}

while True:
    menu="""
     pass 1 for sign up
     pass 2 for login
     pass 3 for forgot password 
     pass 4 for exit
"""
    print(menu)
    choice=int(input("Enter your choice:  "))
    if choice==1:
        name=input("Enter name: ")
        email=input("Enter email: ")
        mobile=int(input("Enter mobile number: "))
        password=input("Enter password: ")
        cpassword=input("Enter confirm password: ")

        if password==cpassword:
            d['email']=email
            d['mobile']=mobile
            d['password']=password

            print("Signup Successfully!!")

        else:
            print("password & confirm password does not match!!")

    elif choice==2:
        email=input("Enter Email: ")
        password=input("Enter password: ")

        if d['email']==email and d['password']==password:
            print("login successfully!!")

        else: 
            print("Invaild Credentials!!")

    elif choice==3:
        mobile=int(input("Enter mobile number: "))

        if d['mobile']==mobile:
            print("**********Yout otp is: ",otp)
            uotp = int(input("Enter OTP: "))

            if otp==uotp:
                password=(input("Enter password: "))

                d['password']=password
                print("password updated!!")

            else:
                print("invalid otp!!")

        else:
            print("mobile number does not exist!!")

    elif choice==4:
        print("Thank uh!!")
        break
