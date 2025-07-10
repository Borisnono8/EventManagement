from functools import wraps
from flask import abort, flash, redirect, url_for
from flask_login import current_user

def login_required(f):
    """Decorator to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', 'info')
            return redirect(url_for('users.login'))
        return f(*args, **kwargs)
    return decorated_function

def organizer_required(f):
    """Decorator to require organizer role"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', 'info')
            return redirect(url_for('users.login'))
        if not current_user.is_organizer():
            flash('You need organizer permissions to access this page.', 'error')
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def attendee_required(f):
    """Decorator to require attendee role (or organizer, as organizers can do attendee actions)"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', 'info')
            return redirect(url_for('users.login'))
        return f(*args, **kwargs)
    return decorated_function

def event_owner_required(f):
    """Decorator to require event ownership"""
    @wraps(f)
    def decorated_function(event_id, *args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', 'info')
            return redirect(url_for('users.login'))
        
        from models import Event
        event = Event.query.get_or_404(event_id)
        
        if event.organizer_id != current_user.id:
            flash('You can only manage your own events.', 'error')
            abort(403)
        
        return f(event_id, *args, **kwargs)
    return decorated_function
