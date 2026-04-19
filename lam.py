from functools import reduce

a=[12,7,65,4,645,3]
res=list(filter(lambda a:a%2==0,a))
rs=reduce(lambda b,a:b+a,res)

print(rs)