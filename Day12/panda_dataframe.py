
import pandas as pd

data= {
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,29,40,33],
    'City':['New York','Chicago','Los Angeles','Houston']
}
df=pd.DataFrame(data)
print(df,"\n")

# Headers
print(df.head())

data=pd.read_csv("C:/Users/iamta/OneDrive/Documents/Capgemini/Python/customers-1000.csv")

print(df['Name'][1:3])
print(df[df['Age']>30])


k=data.to_json("output.json",index=True)
print(k)
# print(data[1:5])
# data=data.sort_values(by='Email',ascending=False)
# print(data[1:5])
# print(data[1:5])
