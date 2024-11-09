import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_parquet("./data/olympics.parquet")

df = df.rename(columns={
    "athlete_id":"ID",
    "name":"Name",
    "born_date":"DOB",
    "born_city":"Born City",
    "born_country":"Born Country",
    "height_cm":"Height",
    "weight_kg":"Weight",
    "born_region":"Born Region",
    "died_date":"DOD"
})

#print(df["Born City"].value_counts())
#print(df.describe())


#print(df.dtypes)
df["DOD"] = pd.to_datetime(df["DOD"])
df["DOB"] = pd.to_datetime(df["DOB"])
#print(df.dtypes)
#print(df.isna().sum())
print(df.loc[df.duplicated(subset=["Born Region"])])

df_q =df.query(' "Born Country"=="USA" ') 
print(df_q.shape)
print(df_q["Height"].value_counts())

#plot_h = df_q['Height'].value_counts().head(10).plot(kind='bar')
#obj = sns.scatterplot( x='Height',y='Weight',data=df_q)
#print(obj)

df_q.plot.bar(x="Height",y="Weight")
plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
