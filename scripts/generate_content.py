import random
import json
import os
from datetime import datetime

# Create scripts directory if it doesn't exist
os.makedirs("scripts", exist_ok=True)

# Load quotes
with open('quotes.txt', 'r') as f:
    quotes = [line.strip() for line in f if line.strip()]

# Hashtag pools
general_hashtags = ["#Motivation", "#Success", "#Growth", "#Mindset", "#Inspiration"]
day_hashtags = {
    "Monday": ["#MondayMotivation", "#MondayMindset", "#WeeklyGoals"],
    "Tuesday": ["#TuesdayThoughts", "#TuesdayMotivation", "#TuesdayTips"],
    "Wednesday": ["#WednesdayWisdom", "#WednesdayMotivation", "#MidweekMotivation"],
    "Thursday": ["#ThursdayThoughts", "#ThursdayMotivation", "#ThursdayInspiration"],
    "Friday": ["#FridayMotivation", "#FridayFeeling", "#WeekendMotivation"],
    "Saturday": ["#SaturdayMotivation", "#WeekendWisdom", "#SaturdaySuccess"],
    "Sunday": ["#SundayMotivation", "#SundayThoughts", "#WeeklyPrep"]
}

# Generate content for today
def generate_daily_content():
    today = datetime.now()
    day_name = today.strftime("%A")
    
    # Select random quote
    quote = random.choice(quotes)
    
    # Select hashtags
    selected_hashtags = random.sample(general_hashtags, 2)
    selected_hashtags.append(random.choice(day_hashtags[day_name]))
    hashtag_text = " ".join(selected_hashtags)
    
    # Create content
    content = {
        "quote": quote,
        "hashtags": hashtag_text,
        "full_post": f"{quote}\n\n{hashtag_text}",
        "date": today.strftime("%Y-%m-%d"),
        "day": day_name
    }
    
    # Save to content.json
    with open('content.json', 'w') as f:
        json.dump(content, f, indent=2)
    
    return content

if __name__ == "__main__":
    content = generate_daily_content()
    print(f"Generated content for {content['date']}:")
    print(content['full_post'])
