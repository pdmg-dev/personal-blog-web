import os
import re
from datetime import datetime

import frontmatter
import markdown

from config import ARTICLE_DIR


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


# get the articles
def get_articles(slug=None):
    article_list = []
    for filename in os.listdir(ARTICLE_DIR):
        filepath = os.path.join(ARTICLE_DIR, filename)
        if os.path.isfile(filepath) and filename.endswith(".md"):
            post = frontmatter.load(filepath)  # Load the metadata and contents

            if slug is not None:
                if post["slug"] == slug:
                    return {
                        "title": post["title"],
                        "date_published": post["date_published"],
                        "slug": post["slug"],
                        "content": markdown.markdown(post.content),
                    }
            else:
                article_list.append(
                    {
                        "title": post["title"],
                        "date_published": post["date_published"],
                        "slug": post["slug"],
                    }
                )
    return sorted(article_list, key=lambda x: x["date_published"], reverse=True)
