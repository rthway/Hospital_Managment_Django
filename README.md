# Django Hospital Management App

The Django Hospital Management App is a web application for managing patients, doctors, appointments, and a dashboard for administrative tasks. The app allows users to add and view patients, doctors, and appointments, providing an easy way to keep track of medical records and schedules.

## Features

-   Add and view patient information (Name, Gender, Age, Address).
-   Add and view doctor information (Name, Phone, Specialization).
-   Schedule and view appointments with doctors (Date, Time).
-   Dashboard page for administrative tasks.

## Requirements

-   Python (>=3.6)
-   Django (>=2.2)

## Installation

1.  Clone the repository:
   

    git clone  https://github.com/rthway/hospital_managment_Django.git

2.  Create a virtual environment (optional, but recommended):


   

 

python -m venv venv
   

 source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
    

cd hospital_managment_Django

3.  Install the required dependencies:

`pip install -r requirements.txt` 

4.  Run database migrations:


`

    python manage.py makemigrations
    python manage.py migrate`

 

5.  Create a superuser (optional):



`python manage.py createsuperuser` 

6.  Start the development server:



`python manage.py runserver` 

The app should now be accessible at `http://localhost:8000/`.
