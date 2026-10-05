def rev_number(n,rem=0,rev=0):

    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
n=int(input("Enter Number : "))
print(rev_number(n))

def fac():
    fac=1
    n=8
    i=5

    while(i<=n):
        fac=fac*i
        i+=1

        return fac
print("factorial is : ",fac())   


def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+1
    return sum


while True:
    menu="""
        press 1 for withoutparameter and without return
        press 2 for 
        


"""
    
     
