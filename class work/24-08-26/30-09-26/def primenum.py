def prime(n,i):

    if n==i:
        return 1
    if n%i==0:
        return 0
    else:
        return print(n,i+1)

n=int(input("Enter number:"))
if prime:
    print(n,"prime Nub=mber :")
else:
    print(n,"not prime Num=mber:")
    
        