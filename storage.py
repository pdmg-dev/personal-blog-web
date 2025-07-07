import os

import frontmatter

from config import ARTICLE_DIR
from utils import generate_filename, slugify


# Save an article
def save_article(title, date_published, content):
    os.makedirs(ARTICLE_DIR, exist_ok=True)  # Check if articles folder exists

    # Create the filepath
    filepath = os.path.join(ARTICLE_DIR, generate_filename(title, date_published))

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
