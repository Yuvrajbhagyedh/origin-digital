a=[12,12,4,2,675,3,8]

for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
print(a)        