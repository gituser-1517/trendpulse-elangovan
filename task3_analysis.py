# Task1

# Load data/trends_clean.csv into a Pandas DataFrame
import pandas as pd
import numpy as np

df = pd.read_csv("data/trends_clean.csv", encoding="cp1252") # Added encoding method due to decode error received

# Print the first 5 rows

print("Printing first 5 rows of the dataframe")
print(df.head(5))

# Print the shape of the DataFrame (rows and columns)

print("\nThe shape of dataframe is:")
print(df.shape)

# Print the average score and average num_comments across all stories

print("\nAverage score:", df["score"].mean())
print("Average number of comments:", df["num_comments"].mean())



# Task 2 — Basic Analysis with NumPy
# Use NumPy to answer these questions and print the results:

# What is the mean, median, and standard deviation of score?

mean_score = np.mean(df["score"])
median_score = np.median(df["score"])
std_score = np.std(df["score"])

print("\nMean score:", mean_score)
print("Median score:", median_score)
print("Std deviation:", std_score)

# What is the highest score and lowest score?

max_score = np.max(df["score"])
min_score = np.min(df["score"])

print("\nHighest score:", max_score)
print("Lowest score:", min_score)


# Which category has the most stories?

values, counts = np.unique(df["category"], return_counts=True)
print("List of categories in the dataframe:",values)
print("Count of respective categories in the dataframe:",counts)
most_stories = values[np.argmax(counts)]

print("\nCategory with most stories:", most_stories)



# Which story has the most comments? Print its title and comment count.

max_comments = np.argmax(df["num_comments"])

top_story_title = df["title"].iloc[max_comments]
top_story_comments = df["num_comments"].iloc[max_comments]
top_story_full_row = df.iloc[max_comments]

print("\nTop story:", top_story_title)
print("Number of comments for top story:", top_story_comments)




# Task3 — Add New Columns
# Add these two new columns to your DataFrame:

# Column	         Formula
# engagement	     num_comments / (score + 1) — how much discussion a story gets per upvote
# is_popular	     True if score > average score, else False

# average score
avg_score = df["score"].mean()

# engagement metric
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# popularity flag
df["is_popular"] = df["score"] > avg_score

print("\nDataframe is updated with two new columns")


# Save the updated DataFrame (with the 2 new columns) to data/trends_analysed.csv
# Print a confirmation message

# save to CSV
df.to_csv("data/trends_analysed.csv", index=False)
print("\nUpdated dataframe saved successfully to trends_analysed.csv")
