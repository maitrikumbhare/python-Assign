try:
    n=int(input("Enter a number:"))
    if (n==0):
        print("Zero")

    else:
        print("Non Zero!!")

except ValueError as e:
    print(e)

else:
    print("try here!!")

finally:
    print("Everytime!!")

#1) valueerror
#2) ZeroDivisionError  

try:
    n=int(input("Enter a number 1: "))
    n1=int(input("Enter a number 2: "))

    print("Division :",n/n1)

except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

try:
    l=[65,78,96,45,23]
    n=int(input("Enter Index: "))
    print("value of index: ", l[n])
except  ValueError as e:
    print(e)
except  IndexError as e:
    print(e)