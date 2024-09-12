# Khatna - Shuttle Transportation App

**Khatna** is an innovative shuttle transport app that facilitates safe and punctual transportation for students and employees. The app provides a seamless way to connect users with shuttles in their area, offering detailed route information, driver contacts, and more.

---

## Features

- **Find Nearby Shuttles**: Easily locate the nearest shuttle based on your live location.
- **Route Selection**: Browse and select from various routes to find the one that best suits your needs.
- **Shuttle and Driver Details**: View detailed information about the shuttle vehicle and driver, ensuring a safe and informed journey.
- **Trip Types**: Know the type of trip (students, employees, mixed, or other) to help plan your commute accordingly.
- **Contact Drivers**: Reach out to the driver directly to negotiate trip details or confirm availability.
- **Driver Capabilities**:
  - Create and manage routes and trips with clear departure and arrival times.
  - Monitor pickup and drop-off schedules for efficiency.

---

## Technologies Used

- **Backend**: FastAPI
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **Proxy and Load Balancer**: Traefik
- **Database**: PostgreSQL
- **Location Services**: Google Maps API

---

## How It Works

### For Users:
1. Open the app and allow location access to find the nearest available shuttle.
2. Browse the list of routes and select the one that fits your destination and time.
3. View shuttle details, trip type, and driver information to make an informed decision.
4. Contact the driver if necessary to make any custom arrangements.

### For Drivers:
1. Register as a driver and start creating routes.
2. Define the journey from location A to location B, and set the departure and arrival times.
3. Manage multiple routes and trips, and update timings as necessary.

---

## Installation and Setup

### Prerequisites

Ensure you have the following installed:
- **Docker** and **Docker Compose**
- **Git**

### Step-by-Step Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/khatna.git