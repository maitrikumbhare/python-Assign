def prime_number(n,rem=0,rev=0):
    for i in range(1,n+1):
        if(n%i==0):
            prime+=1
    if (prime==2):
        print("prime number!!")
    else:
        print("Not a prime number!!")

n1=int(input("Enter a number :"))
prime_number(n1)


"""
def rev_number(n,rem=0,rev=0):
    while(n!=0):
        rev=n%10
        rev=rev*10+rev
        n//=10
    print(rev)

n1=int(input("Enter a number :"))
prime_number(n1)
"""