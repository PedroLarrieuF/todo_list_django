Release 1.0 - Final django app.

Corrections:
Database query related bugs.
html bugs
Bugs in the application in general.

Fixtures:
New search tools
Cleaner code
performance gain
Ready to deploy
Running independently of other applications.

How to run the app?

First download, or clone the project.

Second, open the root folder of the project 'todo_list/todo_list' in your terminal and run the initial migrations:
1 - python3 (or just 'python' for windows) manage.py makemigrations
2 - python3 (or just 'python' for windows) manage.py migrate.

After the initial migrations you can start the app, remembering that it comes with a simple database with two 'admins' for testing. But you can delete the 'db.sqlite3' file straight from the root and run the code above to recreate the database.

After that you run the app with the command 'python3 (or just 'python' for windows) manage.py runserver'

Note: You can try to start directly with the command 'python3 (or just 'python' for windows) manage.py runserver', but it may fail in unscheduled environment variables.


Requirements:
DJango installed
Python 3.7xx installed
updated browser
