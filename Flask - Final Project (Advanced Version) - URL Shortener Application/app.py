import validators 
import secrets
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from extensions import db
from models import LinkVault, User

app = Flask(__name__)

# CONFIGURATION
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vault.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)

# --- LOGIN MANAGER SETUP ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Redirect here if not logged in

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper function
def generate_unique_code():
    while True:
        code = secrets.token_urlsafe(4) 
        if not LinkVault.query.filter_by(short_code=code).first():
            return code

# --- AUTH ROUTES ---

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # 1. Length Validation (5-9 chars)
        if len(username) < 5 or len(username) > 9:
            flash('Username must be between 5 to 9 characters long', 'danger')
            return redirect(url_for('signup'))
            
        # 2. Uniqueness Validation
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash(f'The username "{username}" already exists. Please choose another.', 'danger')
            return redirect(url_for('signup'))
            
        # Create new user
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
        
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check username and password.', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# --- APP ROUTES ---

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    short_url_display = None
    
    if request.method == 'POST':
        user_url = request.form.get('original_url')
        
        if not user_url:
            flash('Please enter a URL.', 'danger')
        elif not validators.url(user_url):
            flash('Invalid URL format. Ensure it starts with http:// or https://', 'warning')
        else:
            # Check if this specific user already saved this link
            existing_link = LinkVault.query.filter_by(original_url=user_url, user_id=current_user.id).first()
            
            if existing_link:
                short_code = existing_link.short_code
                flash('You have already shortened this URL!', 'info')
            else:
                short_code = generate_unique_code()
                # Link the new entry to the CURRENT USER
                new_link = LinkVault(original_url=user_url, short_code=short_code, author=current_user)
                db.session.add(new_link)
                db.session.commit()
                flash('URL successfully shortened!', 'success')
            
            short_url_display = request.host_url + short_code

    # Show history below the form (as requested)
    user_links = LinkVault.query.filter_by(user_id=current_user.id).order_by(LinkVault.created_at.desc()).all()
    
    return render_template('index.html', short_url=short_url_display, history=user_links)

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