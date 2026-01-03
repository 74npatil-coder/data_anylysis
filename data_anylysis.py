import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\l\Desktop\sales_anylysis\train.csv")
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

df=df.drop_duplicates()
df['Postal Code']=df['Postal Code'].fillna(df['Postal Code'].mean())
group=df.groupby("Ship Mode")["Sales"].mean()
countt=df["Order ID"].value_counts().head(10)

fig,axi=plt.subplots(1,2,figsize=(12,6))
axi[0].pie(group.values,labels=group.index,autopct="%1.1f%%")
axi[0].set_title("Percentage Of Ship Mode")
axi[0].get_legend()

axi[1].bar(countt.index,countt.values)
axi[1].set_title("Bar graph")
axi[1].set_xlabel("Order_Id")
axi[1].set_ylabel("Order_Id Count")
axi[1].tick_params(axis='x', rotation=90)

plt.show()




