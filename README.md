#Carpooling App:

Car Pooling App A smart ride-sharing platform that connects riders and drivers based on route, time, and availability to make daily commuting easier, affordable, and efficient.


#Problem Statement:

A mobile application that matches riders and drivers based on route, time, and availability to streamline ride-sharing and reduce transportation costs and congestion.

#System Overview:
The Car Pooling App is a mobile-first application designed to facilitate seamless ride-sharing. It supports two primary user roles—Riders and Drivers—within a single user account. Users can switch roles by enabling the driver option in their profile. The system is built with a Django backend, PostgreSQL database, and a React Native frontend, and is deployed on Render for scalability and reliability.


--------
##Key Features

### 👤 User Management Secure Registration & Login: Users can register and authenticate using a username and password. Role Management: Users can enable the Driver role from their profile settings. Profile Management: Update personal details and manage role preferences.

### 🚗 Ride Management

For Drivers Create Ride Listings: Define pickup location, destination, date/time, and available seats. Manage Riders: View ride requests and accept or reject riders. Ride Updates: Modify ride details or cancel rides when needed. Seat Management: Automatic seat count updates based on bookings. Upcoming Rides: View scheduled rides with current status.

###For Riders Ride Search: 

Search for rides by location, date, and time. View Ride Details: See driver info, route details, and seat availability. 

## Book Seats: Request or book available seats on rides. Booking Status: Track request status (Pending, Accepted, Rejected). Booking History: View past and upcoming rides.

###⭐ Ratings & Feedback Drivers and riders can rate each other after ride completion to build trust and accountability.


-----------------
##🔔 Potential Additional Features Push Notifications: Alerts for ride requests accepted/rejected, upcoming rides, and driver arrival. Maps Integration: Route visualization using Google Maps.


--------------------

## 🛠 Tech Stack Frontend: React Native, Google Maps API Backend: Python (Django) Database: PostgreSQL Deployment: Render

## ⚙️ Installation & Setup

Backend Setup Clone the repository and navigate to the backend root directory. 
Create a virtual environment: python -m venv venv 
Activate the virtual environment: source venv/bin/activate 
Install dependencies: pip install -r requirements.txt

----------------
##Database Setup:

Run PostgreSQL:

CREATE DATABASE carpoolingdb;
CREATE USER anonymoususer WITH PASSWORD 'S3c6rePass123';
GRANT ALL PRIVILEGES ON DATABASE carpoolingdb TO anonymoususer;

________________________

Apply Migrations python manage.py migrate

Run the Server python manage.py runserver

Running Automated Tests pytest

Deployment The application is deployed on Render, with environment variables configured for database access, secrets, and third-party APIs.
-----------------------------
##Future Enhancements:
Advanced matching algorithms for better ride recommendations. 
In-app chat between drivers and riders. 
Payment integration for cost-sharing. 
Enhanced analytics for ride activity and user engagement.

