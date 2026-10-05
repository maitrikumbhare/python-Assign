def rev(n,rem=0,rev=0):

    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10

    return rev

n=int(input("Enter Number :"))
print(rev(n))