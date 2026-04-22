import pandas as pd

data=("annual-enterprise-survey-2024-financial-year-provisional.csv")

df=pd.read_csv(data)
print(df.head())

df.head().to_csv("output.csv",index=False)