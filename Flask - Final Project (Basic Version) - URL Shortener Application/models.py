from datetime import datetime
from extensions import db

class LinkVault(db.Model):
    __tablename__ = 'link_vault'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    visit_count = db.Column(db.Integer, default=0) # Tracks usage

    def __repr__(self):
        return f"<LinkVault {self.short_code}>"