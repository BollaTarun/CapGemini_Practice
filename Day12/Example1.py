import pandas as pd
data= {
    'Region': ['North','South','West','East','North'],
    'State' : ['Delhi','Kerala','Rajasthan','Assam','Delhi'],
    'Year'  : [ 2012,2013,2009,2015,2012],
    'Sales' : [ 750000,65000,4050000,3945000,750000],
    'Profit': [ 145000,20000, 125000,2000000,145000]
}

df=pd.DataFrame(data)
print(df)
df.set_index(['Region','State','Year'],inplace=True)

print(df.loc[('South','Kerala',2013),'Profit'])
#df.print()



df_sales=pd.DataFrame({'State':['Delhi','Pune','Ranchi'],
			'Sales':[30000,44000,56000]})


df_profits=pd.DataFrame({'State':['Delhi','Pune','Ranchi'],
			'Profits':[10000,15000,35000]})

df_merged=pd.merge(df_sales,df_profits,on='State',how='inner')
print(df_merged)