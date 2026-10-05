class Myclass1:
    def even_odd(self,num):
        if num %2==0:
            print("Even number")
        else:
            print("odd number")

class Myclass2:
    def prime(self,num):
        if num>1:
            for i in range(2,num):
                if (num % i) == 0:
                    print("Not a prime number")
                    break
            else:
                print("Prime number")
        else:
            print("Not a prime number")

class Myclass3:
    def factorial(self,num):
        if num == 0:
            print("Factorial is 0")
        else:
            fact = 1
            for i in range(1,num+1):
                fact = fact * i
            print("Factorial is:",fact)

obj1 = Myclass1()
obj2 = Myclass2()
obj3 = Myclass3()

obj1.even_odd(10)
obj2.prime(17)
obj3.factorial(5)