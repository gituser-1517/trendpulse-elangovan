# Task4

# Load data/trends_analysed.csv into a DataFrame
# Create a folder called outputs/ if it doesn't exist
# Use plt.savefig() before any plt.show() on all charts

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("data/trends_analysed.csv")

os.makedirs("outputs", exist_ok=True)




# 2 — Chart 1: Top 10 Stories by Score
# Create a horizontal bar chart showing the top 10 stories by score
# Use the story title on the y-axis (shorten titles longer than 50 characters)
# Add a title and axis labels
# Save as outputs/chart1_top_stories.png

top10_stories = df.sort_values(by="score", ascending=False).head(10)
top10_stories["short_title"] = top10_stories["title"].str.slice(0, 50)

plt.figure(figsize=(10, 6))

plt.barh(top10_stories["short_title"], top10_stories["score"], color="skyblue")

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.tight_layout()

plt.savefig("outputs/chart1_top_stories.png", dpi=150, bbox_inches="tight")

plt.show()




# 3 — Chart 2: Stories per Category 
# Create a bar chart showing how many stories came from each category
# Use a different colour for each bar
# Add a title and axis labels
# Save as outputs/chart2_categories.png


category_counts = df["category"].value_counts()

plt.figure(figsize=(10, 6))

plt.bar(category_counts.index, category_counts.values, color=plt.cm.tab10.colors)

# labels
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Number of Stories per Category")
plt.tight_layout()

plt.savefig("outputs/chart2_categories.png", dpi=150, bbox_inches="tight")

plt.show()



# 4 — Chart 3: Score vs Comments
# Create a scatter plot with score on the x-axis and num_comments on the y-axis
# Colour the dots differently for popular vs non-popular stories (use the is_popular column)
# Add a legend, title, and axis labels
# Save as outputs/chart3_scatter.png

sns.scatterplot(data=df,
               x="score",
               y="num_comments",
               hue="is_popular",
               alpha=0.7)


plt.title("Score vs Number of comments")
plt.xlabel("Total Score")
plt.ylabel("Number of comments")
plt.tight_layout()

plt.savefig("outputs/chart3_scatter.png", dpi=150, bbox_inches="tight")
plt.show()
