#swapping
#1).with using third variable
#2).without using third variable

"""a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

#a=100 b=50

#temp=a  #temp=100  a=blank
#a=b     #a=50     b=blank
#b=temp  #a=50     temp=blank

#a=a+b  #100+50 a=150
#b=a-b  #150-50 b=100
#a=a-b  #150-100 a=50

a,b=b,a #only use in python
print(f"Value of a is {a} and value of b is {b}")"""

#COnditional statements
age=int(input("Enter your age: "))

if age>100:
    print("You are not eligible for voting")
elif age>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
else:
    print("a and b are equal")