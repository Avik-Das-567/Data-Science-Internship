from datetime import datetime
from flask_login import UserMixin
from extensions import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # Relationship: One user has many links
    links = db.relationship('LinkVault', backref='author', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class LinkVault(db.Model):
    __tablename__ = 'link_vault'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    visit_count = db.Column(db.Integer, default=0)
    
    # Foreign Key: Link to the User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<LinkVault {self.short_code}>"