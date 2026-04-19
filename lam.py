from functools import reduce
from mod import add

a=[12,7,65,4,645,3]
res=list(filter(lambda a:a%2==0,a))
ma=list(map(lambda a:a*82,res))
rs=reduce(lambda b,a:b+a,res)

print(ma)


    

print(add(221,12))

