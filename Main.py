#!/usr/bin/env python

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("fdic/fdic.csv")

# remove empty rows
df.dropna(subset=["2000"], inplace=True)

cols = df.columns.tolist()
cols.sort()

df = df[cols]
df = df.set_index("Dollar_Amounts_in_Billions", drop=True)
df.drop("Unnamed: 1", axis=1, inplace=True)
df.drop("Unnamed: 2", axis=1, inplace=True)
df = df.transpose()
df = df.rename_axis("Year")

# print(df["CB_Mergers"])
# print(df["CB_Mergers"].dtypes)
df["CB_Mergers_int"] = df["CB_Mergers"].astype("int64")
print(df)
df["Cumulative_CB_Mergers"] = df["CB_Mergers_int"].cumsum()
print(df["Cumulative_CB_Mergers"])


ax1 = sns.scatterplot(data=df, x="Year", y="Number_of_FDIC_Insured", color="red")
ax2 = ax1.twinx()
ax2 = sns.scatterplot(
    data=df, x="Year", y="Cumulative_CB_Mergers", ax=ax2, color="blue"
)
# ax2.invert_yaxis()


ax1.set_xlabel("Year")
ax1.set_ylabel("Number of FDIC Insured", color="red")
ax2.set_ylabel("Commercial Bank Mergers", color="blue")
ax1.invert_yaxis()


plt.show()
