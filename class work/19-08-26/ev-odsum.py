i=1
ev=0
od=0
evsum=0
odsum=0
sum=0



while(i<=5):
    no=(int(input("Enter Number")))

    if(no % 2 == 0):
        print("Even Number")
        ev += 1
        evsum += no

    else:
        print("Odd Number")
        od += 1
        odsum += no

        sum=sum+no
    i+=1

    print("Even count:",ev)
    print("Even sum:",evsum)
    print("Odd count:",od)
    print("Odd sum:",odsum)
    print("sum is",sum)