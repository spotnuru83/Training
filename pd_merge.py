import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Age': [25, 30, 35]
})

df3 = pd.DataFrame({
    'ID': [1, 3, 5],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Merge df1 and df2 on 'ID'
merged_df = pd.merge(df1, df2, on='ID', how='outer')

# Merge the result with df3 on 'ID'
merged_df = pd.merge(merged_df, df3, on='ID', how='outer')

print(merged_df)
