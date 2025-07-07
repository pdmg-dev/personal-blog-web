import os
from utils import generate_filename

import frontmatter
import markdown

ARTICLE_DIR = "articles"


# Load articles
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


# Save an article
def save_article(title, date_published, content):
    os.makedirs(ARTICLE_DIR, exist_ok=True)  # Check if articles folder exists

    # Create the filepath
    filepath = os.path.join(ARTICLE_DIR, generate_filename(title, date_published))

    # Create the frontmatter object
    metadata = {"title": title, "date_published": date_published}
    post = frontmatter.Post(content, **metadata)

    # Write the frontmatter and content to the file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post))
