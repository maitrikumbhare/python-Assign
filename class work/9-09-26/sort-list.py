l=[34,67,56,23,89,12]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("sorted list is:",l)


