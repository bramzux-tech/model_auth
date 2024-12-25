
 Django Project: model_auth

 Overview
This project demonstrates a Django application with two separate authentication systems:
1. app1 - Manages authentication for Students.
2. app2 - Manages authentication for Staff.

The project implements custom models extending `AbstractUser`, along with custom authentication backends for role-based authentication.

---

 Project Structure
```
model_auth/
|-- app1/
|   |-- models.py      # Defines the Student model for app1
|   |-- forms.py       # Contains forms for Student CRUD and login
|   |-- views.py       # Handles views for app1 operations
|   |-- urls.py        # Maps URLs for app1
|   |-- signals.py     # Automatically assigns groups to Students
|   |-- auth_backends.py # Custom backend for Student authentication
|-- app2/
|   |-- models.py      # Defines the Staff model for app2
|   |-- forms.py       # Contains forms for Staff CRUD and login
|   |-- views.py       # Handles views for app2 operations
|   |-- urls.py        # Maps URLs for app2
|   |-- signals.py     # Automatically assigns groups to Staffs
|   |-- auth_backends.py # Custom backend for Staff authentication
|-- model_auth/
    |-- settings.py    # Project settings with authentication backends defined
    |-- urls.py        # Main URL configuration
```

 Authentication Models

 1. app1 - Student Model
The `Student` model in `app1/models.py` is a custom user model extending Django's `AbstractUser`. Key features include:

- Automatic `student_id` Generation: 
  Each student is assigned a unique `student_id` like `ST1234`.
  
- Custom Password Logic:
  Passwords are auto-generated based on the `date_of_birth` in `ddmmyy` format, prefixed with "student@" (e.g., `student@010199` for January 1, 1999).

- Fields:
  - `full_names` and `surname`: Student's full name and surname.
  - `gender`: Limited to predefined choices (`Male`, `Female`, `Other`).
  - `mobile_number`: Validated to ensure correct format with a country code.
  - `groups` and `permissions`: Custom related names to avoid conflicts.

- Authentication:
  The `StudentAuthenticationBackend` in `app1/auth_backends.py` authenticates users based on their `student_id` and hashed password.

- Usage:
  - When a student logs in, the backend validates `student_id` and password.
  - Once authenticated, students can manage their profiles and access features defined for the `Students` group.

 2. app2 - Staff Model
The `Staff` model in `app2/models.py` is another custom user model extending `AbstractUser`. Key features include:

- Email-Based Authentication:
  Staff members log in using their email addresses.

- Password Handling:
  Staff passwords are manually set during creation and hashed before saving.

- Fields:
  - Similar to the `Student` model but customized for staff-specific requirements.

- Authentication:
  The `StaffAuthenticationBackend` in `app2/auth_backends.py` handles authentication by validating the `email` and hashed password.

- Usage:
  - Staff members log in using their email and password.
  - They can manage their profiles and access features defined for the `Staff` group.

---

 Authentication Flow

 app1 - Student Authentication
1. Registration:
   - A new student is created via the `StudentCreateView` in `app1/views.py`.
   - The `student_id` is auto-generated, and the password is based on `date_of_birth`.
2. Login:
   - The `StudentLoginForm` validates the `student_id` and password.
   - Upon successful login, the user is redirected to the student dashboard.
3. Group Assignment:
   - The `post_save` signal ensures every student is added to the `Students` group.

 app2 - Staff Authentication
1. Registration:
   - A new staff member is created via the `StaffCreateView` in `app2/views.py`.
   - The password is manually entered during creation.
2. Login:
   - The `StaffLoginForm` validates the email and password.
   - Upon successful login, the user is redirected to the staff dashboard.
3. Group Assignment:
   - The `post_save` signal ensures every staff member is added to the `Staffs` group.

---

 Signals

 app1 - Student Group Assignment
- Ensures all students belong to the `Students` group after creation.

 app2 - Staff Group Assignment
- Ensures all staff belong to the `Staffs` group after creation.

---

 Custom Authentication Backends
 app1/auth_backends.py
- `StudentAuthenticationBackend`: Authenticates using `student_id` and password.

 app2/auth_backends.py
- `StaffAuthenticationBackend`: Authenticates using `email` and password.

---

 Templates
- `index.html`: Links to student and staff lists and login pages.
- `student_list.html`: Displays and manages students.
- `staff_list.html`: Displays and manages staff.

---

 Running the Project
1. Install dependencies:
```bash
pip install django
```
2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Start the development server:
```bash
python manage.py runserver
```
4. Access the application at `http://127.0.0.1:8000/`.

---

Enjoy building and exploring the project!
