import json
import os
from datetime import datetime

# Load generated content
with open('content.json', 'r') as f:
    content = json.load(f)

# Create Jekyll post file
today = datetime.now()
post_date = today.strftime("%Y-%m-%d")
post_filename = f"_posts/{post_date}-daily-motivation.md"

# Create post content with Jekyll front matter
post_content = f"""---
layout: post
title: "Daily Motivation - {post_date}"
date: {post_date} 12:00:00 +0000
categories: motivation
---

{content['quote']}

{content['hashtags']}
"""

# Create _posts directory if it doesn't exist
os.makedirs("_posts", exist_ok=True)

# Write post file
with open(post_filename, 'w') as f:
    f.write(post_content)

print(f"Created blog post: {post_filename}")
