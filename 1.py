import numpy as np
import pandas as pd

pd.set_option("display.precision", 2)

df = pd.read_csv("telecom_churn.csv")
df.head()

#print(df.shape)
#print(df.columns)
#print(df.info)

# df["Churn"] = df["Churn"].astype("int64")
# print(df.describe(include=["object","bool"]))

# print(df["Churn"].value_counts(normalize=True))

# print(df.sort_values(by=['Churn',"Total day charge"], ascending=[True,False]).head())

# print(df["Churn"].mean)

# print(df[df["Churn"] == 1]["Total day minutes"].mean())

# print(df[(df["Churn"] == 0) & (df["International plan"] == "No")]["Total intl minutes"].max())

# print(df.loc[0:5, "State":"Area code"])

# print(df.iloc[0:5, 0:3])

# print(df[-1:])

# print(df.apply(np.max))

# print(df[df["State"].apply(lambda state: state[0] == "W")].head())

# d = {"No" : False, "Yes" : True}
# df["International plan"] = df["International plan"].map(d)
# print(df.head())

# d = {"No" : False, "Yes" : True}
# df = df.replace({"Voice mail plan" : d})
# print(df.head())


# columns_to_show = ["Total day minutes", "Total eve minutes", "Total night minutes"]
# print(df.groupby(["Churn"])[columns_to_show].agg([np.mean, np.std, np.min, np.max]))

# print(pd.crosstab(df["Churn"], df["International plan"]))

# print(pd.crosstab(df["Churn"], df["Voice mail plan"], normalize=True))

print(df.pivot_table(
    ["Total day calls", "Total eve calls", "Total night calls"],
    ["Area code"],
    aggfunc="mean",
))
