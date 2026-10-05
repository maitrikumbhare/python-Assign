"""def fac(n):

    if n==1:
        return 1

    else:
        return n*fac(n-1)

       #5*fac(4)
       #4*fac(3)
       #3*fac(2)
       #2*fac(1)
       #(1)

print(fac(5))"""

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

        #0+1=1
        #1+1=2
        #1+2=3
        #2+3=5
        #3+5=8
        #5+8=13
        #8+13=21
        
n=int(input("Enter a number:"))
for i in range(11):
    print(fibo(i))