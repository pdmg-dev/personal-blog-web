import os

import frontmatter

from config import ARTICLE_DIR
from utils import generate_filepath, generate_filename, slugify


# Save an article
def save_article(title, date_published, content):
    os.makedirs(ARTICLE_DIR, exist_ok=True)  # Check if articles folder exists

    # Create the filepath
    filepath = generate_filepath(title, date_published)

    # Create the frontmatter object
    metadata = {
        "title": title,
        "date_published": date_published,
        "slug": slugify(title),
    }
    post = frontmatter.Post(content, **metadata)

    # Write the frontmatter and content to the file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post))


# Update an article
def update_article(title, date_published, content, slug):
    for filename in os.listdir(ARTICLE_DIR):
        filepath = os.path.join(ARTICLE_DIR, filename)
        if os.path.isfile(filepath) and filename.endswith(".md"):
            post = frontmatter.load(filepath)  # Load the metadata and contents

            if post["slug"] == slug:
                old_filepath = filepath
                break

    new_slug = slugify(title)
    new_filepath = generate_filepath(title, date_published)

    metadata = {
        "title": title,
        "date_published": date_published,
        "slug": new_slug,
    }
    post = frontmatter.Post(content, **metadata)

    if old_filepath != new_filepath:
        os.remove(old_filepath)

    with open(new_filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post))
