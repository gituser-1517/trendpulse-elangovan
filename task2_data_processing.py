# Task1
# Load the json file to a dataframe

import pandas as pd
import json

with open("data/trends_20260410.json", "r") as file:

    data = json.load(file)

df = pd.DataFrame(data)

# Print how many rows were loaded and data types of each column

print("Number of rows in loaded data frame is:")
print(df.shape[0])

print(df.info())



#Task 2
# Duplicates — remove any rows with the same post_id

df1 = df.drop_duplicates(subset="post_id")

# Missing values — drop rows where post_id, title, or score is missing

df_clean = df1.dropna()


# Data types — make sure score and num_comments are integers

print(df_clean.info())

# Low quality — remove stories where score is less than 5

df_filtered = df[df["score"] >= 5].copy()
# print(df_filtered)

# Whitespace — strip extra spaces from the title column

df_filtered["title"] = df_filtered["title"].str.strip()


# Print the number of rows remaining after cleaning.

print("\nNumber of rows reamining after cleaning the original data frame is:")
print(df_filtered.shape[0])




# Task 3
# Save the cleaned DataFrame to data/trends_clean.csv

path = "data/trends_clean.csv"
with open(path, "w") as f:
    df_filtered.to_csv(f, index=False)


# Print a confirmation message with the number of rows saved

print(f"\nSaved {len(df_filtered)} rows to {path}")


# Also print a quick summary: how many stories per category

print("\nNumber of stories per category:\n")
df_filtered["category"].value_counts()


