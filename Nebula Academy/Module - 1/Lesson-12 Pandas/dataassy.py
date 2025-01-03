import pandas as pd

df = pd.read_csv("data.csv")

#rows
#print(df.head())
#columns
#print(df[["name", "email"]])

sales_employees = df[df["department"] == "Sales"]
#print(sales_employees)


filtered = df[(df["age"] > 30) & (df["salary"] < 60000)]
#print(filtered)
