from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from flask.views import MethodView
from events import events_bp
from models import Event, Registration
from forms import EventForm
from decorators import organizer_required
from app import db

class EventManagementView(MethodView):
    """Class-based view for event management"""
    decorators = [login_required, organizer_required]
    
    def get(self, event_id=None):
        """Display event management interface"""
        if event_id is None:
            # Show all events created by the organizer
            events = Event.query.filter_by(organizer_id=current_user.id).order_by(Event.start_datetime.asc()).all()
            return render_template('events/organizer_dashboard.html', events=events)
        else:
            # Show specific event management
            event = Event.query.get_or_404(event_id)
            
            # Check if current user owns this event
            if event.organizer_id != current_user.id:
                abort(403)
            
            attendees = Registration.query.filter_by(event_id=event_id).all()
            return render_template('events/attendees.html', event=event, attendees=attendees)
    
    def post(self, event_id=None):
        """Handle event management actions"""
        if event_id is None:
            # Create new event
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
        else:
            # Update existing event
            event = Event.query.get_or_404(event_id)
            
            # Check if current user owns this event
            if event.organizer_id != current_user.id:
                abort(403)
            
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
    
    def delete(self, event_id):
        """Delete event"""
        event = Event.query.get_or_404(event_id)
        
        # Check if current user owns this event
        if event.organizer_id != current_user.id:
            abort(403)
        
        db.session.delete(event)
        db.session.commit()
        
        flash('Event deleted successfully!', 'success')
        return redirect(url_for('events.organizer_dashboard'))

# Register the class-based view
events_bp.add_url_rule('/manage/', view_func=EventManagementView.as_view('event_management'))
events_bp.add_url_rule('/manage/<int:event_id>/', view_func=EventManagementView.as_view('event_management_with_id'))
