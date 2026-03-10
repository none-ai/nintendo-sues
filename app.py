from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from datetime import datetime
import logging
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'nintendo-tariff-secret-key'

# In-memory storage for comments (in production, use a database)
comments = []

# Request ID middleware
@app.before_request
def before_request():
    g.request_id = str(uuid.uuid8())[:8]
    logger.info(f"[{g.request_id}] {request.method} {request.path}")

@app.after_request
def after_request(response):
    logger.info(f"[{g.request_id}] Status: {response.status_code}")
    response.headers['X-Request-ID'] = g.request_id
    return response

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'request_id': g.request_id}), 200

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('error.html', error_code=404, error_message='Page not found'), 404

@app.errorhandler(500)
def server_error(e):
    logger.error(f"Server error: {e}")
    return render_template('error.html', error_code=500, error_message='Internal server error'), 500


@app.context_processor
def inject_dark_mode():
    """Inject dark mode setting into all templates"""
    return {'dark_mode': session.get('dark_mode', False)}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/article')
def article():
    return render_template('article.html', comments=comments)


@app.route('/article/comment', methods=['POST'])
def add_comment():
    """Handle new comment submission"""
    name = request.form.get('name', '').strip()
    comment_text = request.form.get('comment', '').strip()

    if name and comment_text:
        comments.append({
            'name': name,
            'text': comment_text,
            'date': datetime.now().strftime('%B %d, %Y')
        })

    return redirect(url_for('article'))


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    feedback = ""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        if name and email and subject and message:
            # In production, save to database or send email
            feedback = f"Thank you, {name}! Your message has been received. We'll get back to you at {email} soon."

    return render_template('contact.html', feedback=feedback)


@app.route('/toggle-dark-mode', methods=['POST'])
def toggle_dark_mode():
    """Toggle dark mode preference"""
    session['dark_mode'] = not session.get('dark_mode', False)
    return redirect(request.referrer or url_for('home'))


@app.route('/search')
def search():
    """Search functionality"""
    query = request.args.get('q', '').lower()

    # Simple search across all content
    results = []

    if 'tariff' in query or 'lawsuit' in query:
        results.append({
            'title': 'Nintendo Sues for Tariff Refund',
            'url': '/article',
            'snippet': 'Nintendo has taken legal action against the US government, challenging tariffs...'
        })

    if 'timeline' in query or 'history' in query:
        results.append({
            'title': 'Timeline of Events',
            'url': '/timeline',
            'snippet': 'Chronological development of the Nintendo tariff lawsuit...'
        })

    return render_template('search.html', query=query, results=results)


# API Endpoints
@app.route('/api/comments', methods=['GET'])
def api_get_comments():
    """Get all comments"""
    return jsonify(comments)

@app.route('/api/comments', methods=['POST'])
def api_add_comment():
    """Add a new comment via API"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    name = data.get('name', '').strip()
    comment_text = data.get('comment', '').strip()
    
    if not name or not comment_text:
        return jsonify({'error': 'Name and comment are required'}), 400
    
    comment = {
        'name': name,
        'text': comment_text,
        'date': datetime.now().strftime('%B %d, %Y')
    }
    comments.append(comment)
    
    return jsonify({'message': 'Comment added', 'comment': comment}), 201

@app.route('/api/search')
def api_search():
    """Search API endpoint"""
    query = request.args.get('q', '').lower()
    results = []

    if 'tariff' in query or 'lawsuit' in query:
        results.append({
            'title': 'Nintendo Sues for Tariff Refund',
            'url': '/article',
            'snippet': 'Nintendo has taken legal action against the US government, challenging tariffs...'
        })

    if 'timeline' in query or 'history' in query:
        results.append({
            'title': 'Timeline of Events',
            'url': '/timeline',
            'snippet': 'Chronological development of the Nintendo tariff lawsuit...'
        })

    return jsonify({'query': query, 'results': results})


if __name__ == '__main__':
    app.run(debug=True)
