class A:
    def fum(self,prime):
        if prime>1:
            for i in range(2,prime):
                if (prime  % i)== 0:
                    print("Not a prime number")
                    break
            else:
                print("prime number")

class B(A):
    def fum1(self,even_odd):
        if even_odd % 2 == 0:
            print("Even number")
        else:
            print("odd number")

class C(B):
    def fum2(self,fac):
        if fac==0:
            print("Fac is 0")
        else:
            fac=1
            for i in range(1,fac+1):
                fac=fac*i
            print("Fac is:",fac)


obj= C()
obj.fum1(5)
obj.fum2(70)