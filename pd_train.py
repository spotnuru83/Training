import pandas as pd 

df = pd.read_csv("./data/coffee.csv")

print(df.head(14))

#print(df.loc[(df["Units Sold"]>30) & (df["Coffee Type"]=="Latte") ])

df.loc[(df["Units Sold"]>15) & (df["Coffee Type"]=="Latte"),"Best Sales"]="Yes"
print(df.head(14))