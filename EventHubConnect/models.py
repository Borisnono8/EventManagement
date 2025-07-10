from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin, db.Model):
    """Extended User model with custom fields"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    organization = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    role = db.Column(db.String(20), default='attendee', nullable=False)  # 'attendee' or 'organizer'
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    organized_events = db.relationship('Event', backref='organizer', lazy=True, cascade='all, delete-orphan')
    registrations = db.relationship('Registration', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Set password hash"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check password against hash"""
        return check_password_hash(self.password_hash, password)
    
    def is_organizer(self):
        """Check if user is an organizer"""
        return self.role == 'organizer'
    
    def is_attendee(self):
        """Check if user is an attendee"""
        return self.role == 'attendee'
    
    @property
    def full_name(self):
        """Return full name"""
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f'<User {self.username}>'

class Event(db.Model):
    """Event model"""
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    venue_details = db.Column(db.Text, nullable=True)
    max_attendees = db.Column(db.Integer, nullable=True)
    registration_deadline = db.Column(db.DateTime, nullable=True)
    event_type = db.Column(db.String(50), nullable=False)  # 'conference', 'networking', 'workshop', etc.
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    organizer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    registrations = db.relationship('Registration', backref='event', lazy=True, cascade='all, delete-orphan')
    
    @property
    def available_spots(self):
        """Calculate available spots"""
        if self.max_attendees is None:
            return None
        return self.max_attendees - len(self.registrations)
    
    @property
    def is_full(self):
        """Check if event is full"""
        if self.max_attendees is None:
            return False
        return len(self.registrations) >= self.max_attendees
    
    @property
    def is_registration_open(self):
        """Check if registration is still open"""
        now = datetime.utcnow()
        if self.registration_deadline and now > self.registration_deadline:
            return False
        return self.is_active and not self.is_full
    
    @property
    def image_url(self):
        """Get the appropriate image URL for this event type"""
        from flask import url_for
        valid_types = ['conference', 'networking', 'workshop', 'seminar', 'meeting']
        
        if self.event_type in valid_types:
            return url_for('static', filename=f'images/events/{self.event_type}.svg')
        else:
            return url_for('static', filename='images/events/other.svg')
    
    @property
    def type_color(self):
        """Get the appropriate color for this event type"""
        colors = {
            'conference': '#6f42c1',
            'networking': '#198754',
            'workshop': '#ffc107',
            'seminar': '#dc3545',
            'meeting': '#17a2b8',
            'other': '#6c757d'
        }
        return colors.get(self.event_type, colors['other'])
    
    def __repr__(self):
        return f'<Event {self.title}>'

class Registration(db.Model):
    """Registration model - many-to-many relationship between User and Event"""
    __tablename__ = 'registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='registered', nullable=False)  # 'registered', 'cancelled', 'attended'
    notes = db.Column(db.Text, nullable=True)
    
    # Unique constraint to prevent duplicate registrations
    __table_args__ = (db.UniqueConstraint('user_id', 'event_id', name='unique_user_event_registration'),)
    
    def __repr__(self):
        return f'<Registration {self.user.username} -> {self.event.title}>'
