from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlparse as url_parse
from users import users_bp
from models import User, Registration
from forms import LoginForm, RegisterForm, ProfileForm
from app import db

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('events.list_events'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f'Welcome back, {user.first_name}!', 'success')
            
            # Redirect to next page or dashboard
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('events.list_events')
            return redirect(next_page)
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('auth/login.html', form=form)

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('events.list_events'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if username or email already exists
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists', 'error')
            return render_template('auth/register.html', form=form)
        
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered', 'error')
            return render_template('auth/register.html', form=form)
        
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone=form.phone.data,
            organization=form.organization.data,
            bio=form.bio.data,
            role=form.role.data
        )
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('users.login'))
    
    return render_template('auth/register.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@users_bp.route('/profile')
@login_required
def profile():
    """User profile view"""
    return render_template('users/profile.html', user=current_user)

@users_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Edit user profile"""
    form = ProfileForm(obj=current_user)
    
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

@users_bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard showing registered events"""
    registrations = Registration.query.filter_by(user_id=current_user.id).all()
    return render_template('users/dashboard.html', registrations=registrations)
