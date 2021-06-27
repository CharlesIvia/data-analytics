# Import required libraries
import pandas as pd
import numpy as np

# Read data

oceans_table = pd.read_html(
    "https://www.worldatlas.com/articles/the-oceans-of-the-world-by-size.html"
)

# Check number of tables

print(f"Total tables: {len(oceans_table)}")

# the page has a single table

# Create a dataframe

df = oceans_table[0]
print(df)

# Clean the data

# remove percentages from Area and Volume column

df["Area (km2)"] = (
    df["Area (km2)"].str.split(" ").str[0].str.replace(",", "").astype("int")
)
df["Volume (km3)"] = (
    df["Volume (km3)"].str.split(" ").str[0].str.replace(",", "").astype("int")
)
print(df)

# Save dataframe as csv

df.to_csv("./data/oceans_data.csv", index=False)
