import re
import os
import frontmatter

ARTICLE_DIR = "articles"


# Create text to a filename (in slug)
def slugify(text):
    return re.sub(r"\W+", "-", text.lower().strip("-"))


def compact_date(date_str):
    return date_str.replace("-", "")


# To save the article
def save_article(title, date_published, content):
    os.makedirs(ARTICLE_DIR, exist_ok=True)  # Check if articles folder exists

    # Create the filename
    slug = slugify(title)
    date_str = compact_date(date_published)
    filename = f"{slug}-{date_str}.md"
    filepath = os.path.join(ARTICLE_DIR, filename)

    # Create the frontmatter object
    metadata = {"title": title, "date_published": date_published}
    post = frontmatter.Post(content, **metadata)

    # Write the frontmatter and content to the file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post))
