import validators 
import secrets
from flask import Flask, render_template, request, redirect, url_for, flash
from extensions import db
from models import LinkVault

app = Flask(__name__)

# CONFIGURATION
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vault.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)

# Helper function to generate a unique 6-character code
def generate_unique_code():
    while True:
        code = secrets.token_urlsafe(4) 
        if not LinkVault.query.filter_by(short_code=code).first():
            return code

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url_display = None
    
    if request.method == 'POST':
        user_url = request.form.get('original_url')
        
        if not user_url:
            flash('Please enter a URL.', 'danger')
        elif not validators.url(user_url):
            flash('Invalid URL format. Ensure it starts with http:// or https://', 'warning')
        else:
            existing_link = LinkVault.query.filter_by(original_url=user_url).first()
            
            if existing_link:
                short_code = existing_link.short_code
                flash('URL retrieved from vault!', 'info')
            else:
                short_code = generate_unique_code()
                new_link = LinkVault(original_url=user_url, short_code=short_code)
                db.session.add(new_link)
                db.session.commit()
                flash('URL successfully shortened!', 'success')
            
            short_url_display = request.host_url + short_code

    return render_template('index.html', short_url=short_url_display)

@app.route('/history')
def history():
    all_links = LinkVault.query.order_by(LinkVault.created_at.desc()).all()
    return render_template('history.html', links=all_links, host_url=request.host_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    link_entry = LinkVault.query.filter_by(short_code=short_code).first_or_404()
    
    link_entry.visit_count += 1
    db.session.commit()
    
    return redirect(link_entry.original_url)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)