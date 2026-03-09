# Nintendo Sues the US Government - Flask Project

A comprehensive Flask web application providing in-depth coverage of Nintendo's lawsuit against the US government regarding tariff classifications on video game consoles and accessories.

## Features

- **Home Page** - Overview of the lawsuit and key developments
- **Full Article** - In-depth coverage with background, analysis, and industry impact
- **Timeline** - Chronological events of the ongoing legal battle
- **Discussion** - Comment section for reader engagement
- **Contact** - Feedback form for user input
- **Search** - Search functionality across all content
- **Dark Mode** - Toggle between light and dark themes
- **Responsive Design** - Works on desktop and mobile devices

## Installation

```bash
pip install -r requirements.txt
```

## Running the App

```bash
python app.py
```

The app will run at `http://127.0.0.1:5000`

## Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with summary |
| `/article` | Full article content with comments |
| `/timeline` | Timeline of events |
| `/about` | About this project |
| `/contact` | Contact form for feedback |
| `/search` | Search functionality |
| `/toggle-dark-mode` | Toggle dark mode (POST) |

## Tech Stack

- Python
- Flask
- HTML5 / CSS3
- JavaScript

## Project Structure

```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   ├── article.html   # Article page
│   ├── timeline.html  # Timeline page
│   ├── about.html     # About page
│   ├── contact.html   # Contact page
│   └── search.html    # Search results
└── static/
    └── css/
        └── style.css  # Responsive styling with dark mode
```

作者: stlin256的openclaw
