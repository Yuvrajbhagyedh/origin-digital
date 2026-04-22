import numpy as np

data=np.random.randint(1,21,(5,5))
data[2:3]=1 
da=np.diag(data,k=0)
print(da)