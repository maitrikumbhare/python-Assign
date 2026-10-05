"""l=[1, 2, 3]
l1=[4, 5, 6]
d={}
for i in range(len(l)):
    d[l[i]]=l1[i]

print(d)  



d={}
for i in range(1,31):
    d[i]=i*i*i
    print(d)


s = input("Enter name: ")
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
"""

"""d={'p':400, 'q':100, 'r':250}
d1={'p':200, 'q':100}
for i in d1:
    if i in d:
        d[i]+=d1[i]
    else:
        d[i]=d1[i]
print(d)
"""

d={'p':400, 'q':100, 'r':250}
d1={'p':200, 'q':100}
ans={}
for i,j in d.items():
        if i in d1: 
            ans[i]=j+d1[i]
        else:
            ans[i]=j
print(ans)

