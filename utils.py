import re


# Create text to a filename (in slug)
def slugify(text):
    return re.sub(r"\W+", "-", text.lower().strip("-"))


# Remove date's dash lines
def compact_date(date_str):
    return date_str.replace("-", "")


# Generate filename
def generate_filename(title, date_str):
    return f"{slugify(title)}-{compact_date(date_str)}.md"
