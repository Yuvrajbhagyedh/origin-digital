import pandas as pd

data={
    'name':["yuvraj",'ram','lakshman','janaki'],
    'age':[23,145,67,29],
    'city':['bengaluru','ayodhya','forest','vanavasa']
}
df=pd.DataFrame(data)
print(df)

df.drop('city',axis=1,inplace=True)
dr=df['age']
dr=df['age']=df['age']+2
print(df)
