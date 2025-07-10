from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from datetime import datetime
from events import events_bp
from models import Event, Registration, User
from forms import EventForm, RegistrationForm
from decorators import organizer_required, event_owner_required
from app import db

@events_bp.route('/')
def list_events():
    """List all active events"""
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    event_type = request.args.get('type', '')
    
    query = Event.query.filter_by(is_active=True)
    
    if search:
        query = query.filter(Event.title.contains(search) | Event.description.contains(search))
    
    if event_type:
        query = query.filter_by(event_type=event_type)
    
    events = query.order_by(Event.start_datetime.asc()).paginate(
        page=page, per_page=12, error_out=False
    )
    
    return render_template('events/list.html', events=events, search=search, event_type=event_type)

@events_bp.route('/<int:event_id>')
def event_detail(event_id):
    """Event detail page"""
    event = Event.query.get_or_404(event_id)
    
    # Check if current user is registered
    is_registered = False
    user_registration = None
    if current_user.is_authenticated:
        user_registration = Registration.query.filter_by(
            user_id=current_user.id, event_id=event_id
        ).first()
        is_registered = user_registration is not None
    
    return render_template('events/detail.html', event=event, 
                         is_registered=is_registered, user_registration=user_registration)

@events_bp.route('/create', methods=['GET', 'POST'])
@organizer_required
def create_event():
    """Create new event (organizers only)"""
    form = EventForm()
    
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data,
            start_datetime=form.start_datetime.data,
            end_datetime=form.end_datetime.data,
            location=form.location.data,
            venue_details=form.venue_details.data,
            max_attendees=form.max_attendees.data,
            registration_deadline=form.registration_deadline.data,
            event_type=form.event_type.data,
            is_active=form.is_active.data,
            organizer_id=current_user.id
        )
        
        db.session.add(event)
        db.session.commit()
        
        flash('Event created successfully!', 'success')
        return redirect(url_for('events.event_detail', event_id=event.id))
    
    return render_template('events/create.html', form=form)

@events_bp.route('/<int:event_id>/edit', methods=['GET', 'POST'])
@event_owner_required
def edit_event(event_id):
    """Edit event (event owner only)"""
    event = Event.query.get_or_404(event_id)
    form = EventForm(obj=event)
    
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.start_datetime = form.start_datetime.data
        event.end_datetime = form.end_datetime.data
        event.location = form.location.data
        event.venue_details = form.venue_details.data
        event.max_attendees = form.max_attendees.data
        event.registration_deadline = form.registration_deadline.data
        event.event_type = form.event_type.data
        event.is_active = form.is_active.data
        
        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('events.event_detail', event_id=event.id))
    
    return render_template('events/edit.html', form=form, event=event)

@events_bp.route('/<int:event_id>/delete', methods=['POST'])
@event_owner_required
def delete_event(event_id):
    """Delete event (event owner only)"""
    event = Event.query.get_or_404(event_id)
    
    db.session.delete(event)
    db.session.commit()
    
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('events.organizer_dashboard'))

@events_bp.route('/<int:event_id>/register', methods=['GET', 'POST'])
@login_required
def register_for_event(event_id):
    """Register for an event"""
    event = Event.query.get_or_404(event_id)
    
    # Check if registration is open
    if not event.is_registration_open:
        flash('Registration is not available for this event.', 'error')
        return redirect(url_for('events.event_detail', event_id=event_id))
    
    # Check if already registered
    existing_registration = Registration.query.filter_by(
        user_id=current_user.id, event_id=event_id
    ).first()
    
    if existing_registration:
        flash('You are already registered for this event.', 'info')
        return redirect(url_for('events.event_detail', event_id=event_id))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        registration = Registration(
            user_id=current_user.id,
            event_id=event_id,
            notes=form.notes.data
        )
        
        db.session.add(registration)
        db.session.commit()
        
        flash('Successfully registered for the event!', 'success')
        return redirect(url_for('events.event_detail', event_id=event_id))
    
    return render_template('events/register.html', event=event, form=form)

@events_bp.route('/<int:event_id>/unregister', methods=['POST'])
@login_required
def unregister_from_event(event_id):
    """Unregister from an event"""
    registration = Registration.query.filter_by(
        user_id=current_user.id, event_id=event_id
    ).first()
    
    if not registration:
        flash('You are not registered for this event.', 'error')
        return redirect(url_for('events.event_detail', event_id=event_id))
    
    db.session.delete(registration)
    db.session.commit()
    
    flash('Successfully unregistered from the event.', 'success')
    return redirect(url_for('events.event_detail', event_id=event_id))

@events_bp.route('/organizer/dashboard')
@organizer_required
def organizer_dashboard():
    """Organizer dashboard showing their events"""
    events = Event.query.filter_by(organizer_id=current_user.id).order_by(Event.start_datetime.asc()).all()
    return render_template('events/organizer_dashboard.html', events=events)

@events_bp.route('/<int:event_id>/attendees')
@event_owner_required
def event_attendees(event_id):
    """View event attendees (event owner only)"""
    event = Event.query.get_or_404(event_id)
    attendees = Registration.query.filter_by(event_id=event_id).all()
    return render_template('events/attendees.html', event=event, attendees=attendees)
