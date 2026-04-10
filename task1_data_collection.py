import requests
from datetime import datetime
import os
import json

# Defining a function for returning cateogry from the keywords in title

def categorize_story(title):
    """Return category based on keywords."""
    title = title.lower()
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in title:
                return category
        
    return None
    
# Defining the keywords under each category in a dictionary

CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}



ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Using try & except for error handling

try:
    response = requests.get(ids_url, timeout=10)
    if response.status_code == 200:
        story_ids = response.json() # Converting json response to a python list/dict
        story_ids_first_500 = story_ids[:500] # Slicing first 500 id's
            
except Exception as e:
    print("Request Failed") # In case response code is not 200, then print this message


# Create dictionary for storing the category as key

categorized = {}

for cat in CATEGORIES:
    categorized[cat] = []



for category in CATEGORIES:
    
    for story_id in story_ids_first_500:
        if len(categorized[category]) >= 25: # Limiting 25 stories per category
            break
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        response1 = requests.get(story_url, timeout=10)
        if response1.status_code == 200:
            story = response1.json()
        
        if not story or "title" not in story:
            continue        
            
        story_category = categorize_story(story["title"]) # Calling the function to return the category based on keyword in title

        # Based on the category, below values will be appended to respective keys
        
        if story_category == category:
            categorized[category].append({
                    "post_id": story["id"],
                    "title": story["title"],
                    "category": category,
                    "score": story["score"],
                    "num_comments": story["descendants"],
                    "author": story["by"],
                    "collected_at": datetime.now().isoformat()
                })
    time.sleep(2) # Sleep time after each category iteration completion

print("Number of stories collected based on the category:\n")
for i in categorized:
    print(f"{i} stories: {len(categorized[i])}")

# Combining all stories in categorized dictionary to one list 

combined_stories = []
for cat, stories in categorized.items():
    combined_stories.extend(stories)

# Create the directory for saving the json file

os.makedirs("data", exist_ok=True)

# Write the content of combined_stories list to json file

output_path = f"data/trends_{datetime.now().strftime("%Y%m%d")}.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(combined_stories, f, indent=2)


print(f"\nTotal stories collected: {len(combined_stories)}")
print(f"Saved to: {output_path}")
