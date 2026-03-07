from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template for the main page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nintendo Sues US Government - Tariff Refund</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #e60012;
        }
        .meta {
            color: #666;
            font-size: 0.9em;
        }
        nav {
            margin-bottom: 20px;
        }
        nav a {
            margin-right: 15px;
            text-decoration: none;
            color: #0066cc;
        }
        nav a:hover {
            text-decoration: underline;
        }
        .content {
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="container">
        <nav>
            <a href="/">Home</a>
            <a href="/article">Article</a>
            <a href="/about">About</a>
        </nav>
        {{ content | safe }}
    </div>
</body>
</html>
"""


@app.route('/')
def home():
    content = """
    <h1>Nintendo Sues the US Government</h1>
        <p class="meta">TechCrunch | Latest News</p>
        <div class="content">
            <h2>Welcome to the Nintendo Tariff Lawsuit Coverage</h2>
            <p>Nintendo has filed a lawsuit against the US government seeking a refund on tariffs imposed on imported video game consoles and accessories.</p>
            <p>This landmark case could have significant implications for the video game industry and international trade relations.</p>
            <p><a href="/article">Read the full article</a></p>
        </div>
    """
    return render_template_string(HTML_TEMPLATE.replace('{{ content | safe }}', content))


@app.route('/article')
def article():
    content = """
    <h1>Full Article: Nintendo Sues for Tariff Refund</h1>
        <p class="meta">Published: March 2026</p>
        <div class="content">
            <h3>Background</h3>
            <p>Nintendo has taken legal action against the US government, challenging tariffs that the company claims were incorrectly applied to its products. The lawsuit seeks a refund of millions of dollars in tariffs paid over the past years.</p>

            <h3>Key Points</h3>
            <ul>
                <li>Nintendo argues the tariffs were misclassified</li>
                <li>The company seeks refund of tariffs paid since 2019</li>
                <li>The case could affect other electronics manufacturers</li>
                <li>Industry watchers say the outcome could set a precedent</li>
            </ul>

            <h3>Industry Impact</h3>
            <p>Other major electronics companies are closely watching this case, as similar tariff disputes could affect their operations. The lawsuit highlights ongoing tensions between trade policy and the technology sector.</p>

            <p><a href="/">Back to Home</a></p>
        </div>
    """
    return render_template_string(HTML_TEMPLATE.replace('{{ content | safe }}', content))


@app.route('/about')
def about():
    content = """
    <h1>About This Project</h1>
        <div class="content">
            <p>This is a simple Flask web application created to demonstrate routing and basic web development.</p>

            <h3>Routes</h3>
            <ul>
                <li><strong>/</strong> - Home page with summary</li>
                <li><strong>/article</strong> - Full article content</li>
                <li><strong>/about</strong> - About this project</li>
            </ul>

            <h3>Tech Stack</h3>
            <ul>
                <li>Python</li>
                <li>Flask</li>
                <li>HTML/CSS</li>
            </ul>

            <p><a href="/">Back to Home</a></p>
        </div>
    """
    return render_template_string(HTML_TEMPLATE.replace('{{ content | safe }}', content))


if __name__ == '__main__':
    app.run(debug=True)
