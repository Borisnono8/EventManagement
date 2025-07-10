from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectField, DateTimeField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional, NumberRange
from wtforms.widgets import TextArea
from datetime import datetime

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=50)])
    phone = StringField('Phone Number', validators=[Optional(), Length(max=20)])
    organization = StringField('Organization', validators=[Optional(), Length(max=100)])
    bio = TextAreaField('Bio', validators=[Optional(), Length(max=500)])
    role = SelectField('Role', choices=[('attendee', 'Attendee'), ('organizer', 'Organizer')], default='attendee')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', 
                                   validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[Optional(), Length(max=20)])
    organization = StringField('Organization', validators=[Optional(), Length(max=100)])
    bio = TextAreaField('Bio', validators=[Optional(), Length(max=500)])

class EventForm(FlaskForm):
    title = StringField('Event Title', validators=[DataRequired(), Length(min=5, max=200)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=1000)])
    start_datetime = DateTimeField('Start Date & Time', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
    end_datetime = DateTimeField('End Date & Time', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
    location = StringField('Location', validators=[DataRequired(), Length(min=5, max=200)])
    venue_details = TextAreaField('Venue Details', validators=[Optional(), Length(max=500)])
    max_attendees = IntegerField('Maximum Attendees', validators=[Optional(), NumberRange(min=1, max=10000)])
    registration_deadline = DateTimeField('Registration Deadline', validators=[Optional()], format='%Y-%m-%dT%H:%M')
    event_type = SelectField('Event Type', choices=[
        ('conference', 'Conference'),
        ('networking', 'Networking Event'),
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
        ('meeting', 'Meeting'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    is_active = BooleanField('Active', default=True)
    
    def validate(self, extra_validators=None):
        if not super().validate(extra_validators):
            return False
        
        # Check if end datetime is after start datetime
        if self.end_datetime.data <= self.start_datetime.data:
            self.end_datetime.errors.append('End date must be after start date')
            return False
        
        # Check if registration deadline is before start datetime
        if self.registration_deadline.data and self.registration_deadline.data > self.start_datetime.data:
            self.registration_deadline.errors.append('Registration deadline must be before event start')
            return False
        
        return True

class RegistrationForm(FlaskForm):
    notes = TextAreaField('Notes (Optional)', validators=[Optional(), Length(max=500)])
