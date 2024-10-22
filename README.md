# DJANGO-TASK-MANAGER-APP

A simple yet effective Task Manager application built using Django. This web app allows users to efficiently manage their daily tasks, organize projects, and track progress with ease. 

## Features:
- *User Authentication*: Secure registration, login, and logout functionality.
- *Task Management*: Create, edit, update, and delete tasks.
- *Project Categorization*: Organize tasks under different projects.
- *Task Status Tracking*: Mark tasks as "To-Do," "In Progress," or "Completed."
- *Due Dates*: Set deadlines for tasks and view upcoming deadlines.
- *Prioritization*: Assign priority levels (Low, Medium, High) to tasks.
- *Responsive Design*: Fully functional on desktop and mobile devices.
- *User-specific tasks*: Each user can view and manage their tasks independently.
  
## Technology Stack:
- *Backend*: Django (Python)
- *Frontend*: HTML5, CSS3, JavaScript
- *Database*: SQLite (default), easily extendable to PostgreSQL or MySQL
- *Authentication*: Django's built-in authentication system

## Installation:
1. Clone the repository:
   bash
   git clone https://github.com/vipin956/DJANGO-TASK-MANAGER-APP.git
   
2. Navigate to the project directory:
   bash
   cd django-task-manager
   
3. Create and activate a virtual environment:
   bash
   python3 -m venv venv
   source venv/bin/activate
   
4. Install dependencies:
   bash
   pip install -r requirements.txt
   
5. Run migrations:
   bash
   python manage.py migrate
   
6. Create a superuser to access the admin panel:
   bash
   python manage.py createsuperuser
   
7. Start the development server:
   bash
   python manage.py runserver
   

## Contributing:
Feel free to fork this repository and submit pull requests to add features, improve performance, or fix bugs!

---

Let me know if you'd like any changes or additions!
