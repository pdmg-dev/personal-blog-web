# Personal Blog

A simple personal blog built with Flask where you can write, publish, edit, and delete articles. The blog has a clean guest-facing home page and a protected admin dashboard, with articles stored as Markdown files on the filesystem.

---

## Features

- Guest Section
  - View list of published articles (`/`)
  - View full article content (`/article/<slug>`)

- Admin Section
  - Login/Logout authentication
  - Dashboard to manage articles (`/dashboard`)
  - Add new articles with title, date, and content
  - Edit existing articles
  - Delete articles with confirmation

- File-Based Storage
  - Each article is saved as a separate Markdown file with frontmatter metadata
  - No database required

---

## Folder Structure
```bash
personal-blog/
│
├── app.py # Main Flask app
├── config.py # Configuration (e.g., article folder path)
├── storage.py # Save / Update article files
├── utils.py # Helpers: slugify, get articles, etc.
│
├── articles/ # Stored Markdown article files
│
├── templates/
│ ├── base.html
│ ├── auth/login.html
│ ├── guest/home.html
│ ├── guest/view_article.html
│ └── admin/
│ ├── dashboard.html
│ ├── add_article.html
│ └── edit_article.html
│
├── static/
│ └── style.css # Custom styling
│
└── requirements.txt
```


---

## Getting Started

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/pdmg-dev/personal-blog-web.git
cd personal-blog-web
```
2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

```
3. Install dependencies

```bash
pip install -r requirements.txt
```
4. Run the app

```bash
python app.py
```
5. Open in browser
```bash
http://localhost:5000
```

### Admin Login
```bash 
Username: admin	
Password: admin1234
```
You can modify this in app.py under the users dictionary.

## Tech Stack
```bash 
Backend: Flask
Frontend: HTML + CSS (no JavaScript)
Storage: Markdown files with YAML frontmatter
Authentication: Session-based login (no database)
```

## License
This project is open-source and available under the MIT License.

## Project Source
Built as part of the roadmap.sh project series.
Project: [Personal Blog](https://roadmap.sh/projects/personal-blog)


