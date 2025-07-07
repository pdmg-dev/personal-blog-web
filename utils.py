import re
from config import ARTICLE_DIR
import os
import frontmatter
import markdown
from datetime import datetime


# Create text to a filename (in slug)
def slugify(text):
    return re.sub(r"\W+", "-", text.lower().strip("-"))


# Remove date's dash lines
def compact_date(date_str):
    return date_str.replace("-", "")


# Generate filename
def generate_filename(title, date_str):
    return f"{slugify(title)}-{compact_date(date_str)}.md"


# Get current date and time
def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


# List the articles
def list_articles():
    article_list = []
    for filename in os.listdir(ARTICLE_DIR):
        filepath = os.path.join(ARTICLE_DIR, filename)
        if os.path.isfile(filepath) and filename.endswith(".md"):
            post = frontmatter.load(filepath)  # Load the metadata and contents

            article = {
                "title": post["title"],
                "date_published": post["date_published"],
                "content": markdown.markdown(post.content),  # Convert md to html
            }
            article_list.append(article)
    return sorted(article_list, key=lambda x: x["date_published"], reverse=True)
