"""
Database initialization script for Event Management System
This script creates sample data for development and testing purposes.
"""

import os
import sys
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash

# Add the parent directory to the path to import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models import User, Event, Registration

def init_database():
    """Initialize the database with sample data"""
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        
        print("Creating sample users...")
        
        # Create sample users
        users = [
            {
                'username': 'admin',
                'email': 'admin@eventmanagement.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'phone': '+1-555-0100',
                'organization': 'Event Management Co.',
                'bio': 'System administrator and event coordinator.',
                'role': 'organizer',
                'password': 'admin123'
            },
            {
                'username': 'john_organizer',
                'email': 'john@techconf.com',
                'first_name': 'John',
                'last_name': 'Smith',
                'phone': '+1-555-0101',
                'organization': 'Tech Conference Inc.',
                'bio': 'Experienced event organizer specializing in technology conferences.',
                'role': 'organizer',
                'password': 'organizer123'
            },
            {
                'username': 'sarah_events',
                'email': 'sarah@networkpro.com',
                'first_name': 'Sarah',
                'last_name': 'Johnson',
                'phone': '+1-555-0102',
                'organization': 'Network Pro Events',
                'bio': 'Professional networking event coordinator with 10+ years experience.',
                'role': 'organizer',
                'password': 'organizer123'
            },
            {
                'username': 'mike_attendee',
                'email': 'mike@example.com',
                'first_name': 'Mike',
                'last_name': 'Davis',
                'phone': '+1-555-0201',
                'organization': 'Tech Startup XYZ',
                'bio': 'Software developer interested in tech events and networking.',
                'role': 'attendee',
                'password': 'attendee123'
            },
            {
                'username': 'emma_developer',
                'email': 'emma@webdev.com',
                'first_name': 'Emma',
                'last_name': 'Wilson',
                'phone': '+1-555-0202',
                'organization': 'Web Development Agency',
                'bio': 'Full-stack developer passionate about learning new technologies.',
                'role': 'attendee',
                'password': 'attendee123'
            },
            {
                'username': 'alex_student',
                'email': 'alex@university.edu',
                'first_name': 'Alex',
                'last_name': 'Chen',
                'phone': '+1-555-0203',
                'organization': 'State University',
                'bio': 'Computer Science student looking to network with professionals.',
                'role': 'attendee',
                'password': 'attendee123'
            },
            {
                'username': 'lisa_manager',
                'email': 'lisa@corporate.com',
                'first_name': 'Lisa',
                'last_name': 'Brown',
                'phone': '+1-555-0204',
                'organization': 'Corporate Solutions Ltd.',
                'bio': 'Project manager interested in leadership and management events.',
                'role': 'attendee',
                'password': 'attendee123'
            },
            {
                'username': 'david_freelancer',
                'email': 'david@freelance.com',
                'first_name': 'David',
                'last_name': 'Miller',
                'phone': '+1-555-0205',
                'organization': 'Freelance Consulting',
                'bio': 'Independent consultant specializing in business development.',
                'role': 'attendee',
                'password': 'attendee123'
            }
        ]
        
        created_users = {}
        for user_data in users:
            user = User(
                username=user_data['username'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                phone=user_data['phone'],
                organization=user_data['organization'],
                bio=user_data['bio'],
                role=user_data['role']
            )
            user.set_password(user_data['password'])
            db.session.add(user)
            created_users[user_data['username']] = user
        
        db.session.commit()
        print(f"Created {len(users)} users")
        
        print("Creating sample events...")
        
        # Create sample events
        now = datetime.utcnow()
        events_data = [
            {
                'title': 'AI & Machine Learning Conference 2025',
                'description': 'Join us for the premier AI and Machine Learning conference featuring industry leaders, cutting-edge research, and hands-on workshops. Learn about the latest developments in artificial intelligence, neural networks, and machine learning applications across various industries.',
                'start_datetime': now + timedelta(days=30),
                'end_datetime': now + timedelta(days=30, hours=8),
                'location': 'San Francisco Convention Center, CA',
                'venue_details': 'Main auditorium, Level 3. Registration opens at 8:00 AM. Parking available in adjacent garage.',
                'max_attendees': 500,
                'registration_deadline': now + timedelta(days=25),
                'event_type': 'conference',
                'organizer': 'john_organizer'
            },
            {
                'title': 'Tech Startup Networking Mixer',
                'description': 'Connect with fellow entrepreneurs, investors, and tech professionals in a relaxed networking environment. Perfect opportunity to share ideas, find co-founders, and build valuable business relationships.',
                'start_datetime': now + timedelta(days=7),
                'end_datetime': now + timedelta(days=7, hours=3),
                'location': 'Innovation Hub, Austin, TX',
                'venue_details': 'Main floor networking area. Light refreshments and drinks provided. Business casual attire recommended.',
                'max_attendees': 100,
                'registration_deadline': now + timedelta(days=5),
                'event_type': 'networking',
                'organizer': 'sarah_events'
            },
            {
                'title': 'Full-Stack Web Development Workshop',
                'description': 'Intensive hands-on workshop covering modern web development technologies including React, Node.js, and database integration. Suitable for intermediate developers looking to expand their skill set.',
                'start_datetime': now + timedelta(days=14),
                'end_datetime': now + timedelta(days=15, hours=6),
                'location': 'Tech Academy, Seattle, WA',
                'venue_details': 'Computer lab with pre-configured development environments. Please bring your own laptop as backup.',
                'max_attendees': 30,
                'registration_deadline': now + timedelta(days=10),
                'event_type': 'workshop',
                'organizer': 'admin'
            },
            {
                'title': 'Digital Marketing Strategies Seminar',
                'description': 'Learn the latest digital marketing trends, social media strategies, and conversion optimization techniques from industry experts. Includes case studies and practical applications.',
                'start_datetime': now + timedelta(days=21),
                'end_datetime': now + timedelta(days=21, hours=4),
                'location': 'Business Center, New York, NY',
                'venue_details': 'Conference room A-1. Materials and lunch provided. Presentation slides will be shared after the event.',
                'max_attendees': 75,
                'registration_deadline': now + timedelta(days=18),
                'event_type': 'seminar',
                'organizer': 'sarah_events'
            },
            {
                'title': 'Cybersecurity Best Practices Conference',
                'description': 'Comprehensive conference covering enterprise security, threat detection, incident response, and compliance frameworks. Features keynotes from leading security professionals.',
                'start_datetime': now + timedelta(days=45),
                'end_datetime': now + timedelta(days=46, hours=7),
                'location': 'Cyber Security Center, Washington, DC',
                'venue_details': 'Main conference hall with breakout rooms for workshops. Security clearance not required for attendance.',
                'max_attendees': 300,
                'registration_deadline': now + timedelta(days=40),
                'event_type': 'conference',
                'organizer': 'john_organizer'
            },
            {
                'title': 'Women in Tech Leadership Summit',
                'description': 'Empowering women in technology through leadership development, mentorship opportunities, and career advancement strategies. Features panel discussions and networking sessions.',
                'start_datetime': now + timedelta(days=35),
                'end_datetime': now + timedelta(days=35, hours=6),
                'location': 'Tech Diversity Center, Portland, OR',
                'venue_details': 'Multi-purpose event space with breakout areas. Childcare services available upon request.',
                'max_attendees': 150,
                'registration_deadline': now + timedelta(days=30),
                'event_type': 'networking',
                'organizer': 'admin'
            },
            {
                'title': 'Data Science & Analytics Workshop',
                'description': 'Hands-on workshop covering data analysis, visualization, and machine learning using Python and R. Includes real-world datasets and practical exercises.',
                'start_datetime': now + timedelta(days=28),
                'end_datetime': now + timedelta(days=29, hours=8),
                'location': 'Data Science Institute, Boston, MA',
                'venue_details': 'Computer lab with Jupyter notebooks pre-installed. Basic programming knowledge recommended.',
                'max_attendees': 40,
                'registration_deadline': now + timedelta(days=25),
                'event_type': 'workshop',
                'organizer': 'john_organizer'
            },
            {
                'title': 'Blockchain and Cryptocurrency Seminar',
                'description': 'Explore the fundamentals of blockchain technology, cryptocurrency markets, and decentralized applications. Covers both technical and business perspectives.',
                'start_datetime': now + timedelta(days=38),
                'end_datetime': now + timedelta(days=38, hours=5),
                'location': 'Financial District Center, Chicago, IL',
                'venue_details': 'Executive conference room with presentation equipment. Light refreshments provided.',
                'max_attendees': 80,
                'registration_deadline': now + timedelta(days=35),
                'event_type': 'seminar',
                'organizer': 'sarah_events'
            },
            {
                'title': 'Mobile App Development Conference',
                'description': 'Two-day conference focusing on iOS and Android development, cross-platform solutions, and app store optimization. Includes hands-on coding sessions and expert panels.',
                'start_datetime': now + timedelta(days=60),
                'end_datetime': now + timedelta(days=61, hours=8),
                'location': 'Mobile Tech Center, Los Angeles, CA',
                'venue_details': 'State-of-the-art facility with device testing labs. Lunch and networking dinners included.',
                'max_attendees': 250,
                'registration_deadline': now + timedelta(days=55),
                'event_type': 'conference',
                'organizer': 'admin'
            },
            {
                'title': 'Cloud Computing Workshop',
                'description': 'Practical workshop on cloud infrastructure, deployment strategies, and cost optimization using AWS, Azure, and Google Cloud Platform.',
                'start_datetime': now + timedelta(days=42),
                'end_datetime': now + timedelta(days=42, hours=6),
                'location': 'Cloud Academy, Denver, CO',
                'venue_details': 'Hands-on lab with cloud console access provided. Bring laptop for exercises.',
                'max_attendees': 35,
                'registration_deadline': now + timedelta(days=38),
                'event_type': 'workshop',
                'organizer': 'john_organizer'
            }
        ]
        
        created_events = []
        for event_data in events_data:
            event = Event(
                title=event_data['title'],
                description=event_data['description'],
                start_datetime=event_data['start_datetime'],
                end_datetime=event_data['end_datetime'],
                location=event_data['location'],
                venue_details=event_data['venue_details'],
                max_attendees=event_data['max_attendees'],
                registration_deadline=event_data['registration_deadline'],
                event_type=event_data['event_type'],
                organizer_id=created_users[event_data['organizer']].id
            )
            db.session.add(event)
            created_events.append(event)
        
        db.session.commit()
        print(f"Created {len(events_data)} events")
        
        print("Creating sample registrations...")
        
        # Create sample registrations
        registrations_data = [
            # AI Conference registrations
            {'user': 'mike_attendee', 'event_index': 0, 'notes': 'Interested in deep learning applications'},
            {'user': 'emma_developer', 'event_index': 0, 'notes': 'Looking forward to the neural network workshop'},
            {'user': 'alex_student', 'event_index': 0, 'notes': 'First AI conference - very excited!'},
            {'user': 'lisa_manager', 'event_index': 0, 'notes': 'Want to understand AI for business applications'},
            
            # Networking Mixer registrations
            {'user': 'mike_attendee', 'event_index': 1, 'notes': 'Looking for potential co-founders'},
            {'user': 'david_freelancer', 'event_index': 1, 'notes': 'Interested in business partnerships'},
            {'user': 'alex_student', 'event_index': 1, 'notes': 'Looking for internship opportunities'},
            
            # Web Development Workshop registrations
            {'user': 'emma_developer', 'event_index': 2, 'notes': 'Want to learn React hooks and context'},
            {'user': 'alex_student', 'event_index': 2, 'notes': 'Need to improve full-stack skills'},
            {'user': 'mike_attendee', 'event_index': 2, 'notes': 'Transitioning from backend to full-stack'},
            
            # Digital Marketing Seminar registrations
            {'user': 'lisa_manager', 'event_index': 3, 'notes': 'Need to update marketing strategies'},
            {'user': 'david_freelancer', 'event_index': 3, 'notes': 'Want to improve client acquisition'},
            
            # Cybersecurity Conference registrations
            {'user': 'mike_attendee', 'event_index': 4, 'notes': 'Security is crucial for our startup'},
            {'user': 'emma_developer', 'event_index': 4, 'notes': 'Want to learn about secure coding practices'},
            {'user': 'lisa_manager', 'event_index': 4, 'notes': 'Need to understand compliance requirements'},
            
            # Women in Tech Summit registrations
            {'user': 'emma_developer', 'event_index': 5, 'notes': 'Excited about mentorship opportunities'},
            {'user': 'lisa_manager', 'event_index': 5, 'notes': 'Want to connect with other women leaders'},
            
            # Data Science Workshop registrations
            {'user': 'alex_student', 'event_index': 6, 'notes': 'Working on data science thesis'},
            {'user': 'mike_attendee', 'event_index': 6, 'notes': 'Need data analysis skills for product development'},
            {'user': 'lisa_manager', 'event_index': 6, 'notes': 'Want to understand data-driven decision making'},
            
            # Blockchain Seminar registrations
            {'user': 'david_freelancer', 'event_index': 7, 'notes': 'Considering blockchain consulting services'},
            {'user': 'mike_attendee', 'event_index': 7, 'notes': 'Exploring crypto integration possibilities'},
        ]
        
        attendee_users = [user for user in created_users.values() if user.role == 'attendee']
        
        for reg_data in registrations_data:
            user = created_users[reg_data['user']]
            event = created_events[reg_data['event_index']]
            
            registration = Registration(
                user_id=user.id,
                event_id=event.id,
                notes=reg_data['notes']
            )
            db.session.add(registration)
        
        db.session.commit()
        print(f"Created {len(registrations_data)} registrations")
        
        print("\nDatabase initialization completed!")
        print("\nSample Login Credentials:")
        print("=" * 50)
        print("Organizers:")
        print("  Username: admin, Password: admin123")
        print("  Username: john_organizer, Password: organizer123")
        print("  Username: sarah_events, Password: organizer123")
        print("\nAttendees:")
        print("  Username: mike_attendee, Password: attendee123")
        print("  Username: emma_developer, Password: attendee123")
        print("  Username: alex_student, Password: attendee123")
        print("  Username: lisa_manager, Password: attendee123")
        print("  Username: david_freelancer, Password: attendee123")
        print("=" * 50)
        
        # Print summary statistics
        print(f"\nDatabase Summary:")
        print(f"  Total Users: {User.query.count()}")
        print(f"  Total Events: {Event.query.count()}")
        print(f"  Total Registrations: {Registration.query.count()}")
        print(f"  Organizers: {User.query.filter_by(role='organizer').count()}")
        print(f"  Attendees: {User.query.filter_by(role='attendee').count()}")

if __name__ == '__main__':
    print("Initializing Event Management System Database...")
    print("This will delete all existing data and create sample data.")
    
    # Set environment variables for development
    os.environ.setdefault('DATABASE_URL', 'sqlite:///event_management.db')
    os.environ.setdefault('SESSION_SECRET', 'dev-secret-key-change-in-production')
    
    confirmation = input("Are you sure you want to proceed? (y/N): ")
    if confirmation.lower() == 'y':
        init_database()
    else:
        print("Database initialization cancelled.")
