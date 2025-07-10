from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from flask.views import MethodView
from users import users_bp
from models import User, Registration
from forms import ProfileForm
from app import db

class UserProfileView(MethodView):
    """Class-based view for user profile management"""
    decorators = [login_required]
    
    def get(self, user_id=None):
        """Display user profile"""
        if user_id is None:
            user = current_user
        else:
            user = User.query.get_or_404(user_id)
            # Users can only view their own profile or if they're an organizer
            if user.id != current_user.id and not current_user.is_organizer():
                abort(403)
        
        return render_template('users/profile.html', user=user)
    
    def post(self, user_id=None):
        """Update user profile"""
        if user_id is not None and user_id != current_user.id:
            abort(403)
        
        form = ProfileForm()
        if form.validate_on_submit():
            # Check if email is already taken by another user
            if form.email.data != current_user.email:
                if User.query.filter_by(email=form.email.data).first():
                    flash('Email already registered by another user', 'error')
                    return render_template('users/edit_profile.html', form=form)
            
            # Update user information
            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            current_user.email = form.email.data
            current_user.phone = form.phone.data
            current_user.organization = form.organization.data
            current_user.bio = form.bio.data
            
            db.session.commit()
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('users.profile'))
        
        return render_template('users/edit_profile.html', form=form)

# Register the class-based view
users_bp.add_url_rule('/profile/', view_func=UserProfileView.as_view('profile_view'))
users_bp.add_url_rule('/profile/<int:user_id>/', view_func=UserProfileView.as_view('profile_view_with_id'))
