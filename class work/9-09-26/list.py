l=[]
ev=[]
od=[]
for i in range(1,31):
    l.append(i)

    if i%2==0:
        ev.append(i)

    else:
        od.append(i)

print(l)
print(ev)
print(od)


l=[1,2,3,1,2]
uni=[]
dup=[]
for i in l:
    if i not in uni:
        uni.append(i)
    else:
        dup.append(i)


print(uni)
print(dup)


l=[56,34,24,16,21]
l.sort()
print("smallest number is:",l[0])
print("largest number is:",l[-1])
print("second largest number is:",l[-2])



l=[34,13,39,11,10]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        l[j],l[i]=l[i],l[j]

print(l)