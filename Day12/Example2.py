
import pandas as pd

data= {
    'Name': ['Aadi','Bhanu','Chari'],
    'Age' : [ 23, 25, 29],
    'Dept': ['IT', 'HR', 'CSD']
}

df=pd.DataFrame(data)
print(df)
df.to_csv("data.csv",index=False)  
k=df.set_index(['Name'], inplace=False)
print(k)
