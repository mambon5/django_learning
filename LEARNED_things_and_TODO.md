# Keep track of to do issue, and learned things

- [Keep track of to do issue, and learned things](#keep-track-of-to-do-issue-and-learned-things)
  - [TO DO list](#to-do-list)
  - [I was last doing:](#i-was-last-doing)
  - [Learned things](#learned-things)
  - [Python Django tutorial](#python-django-tutorial)
    - [How to import files and functions](#how-to-import-files-and-functions)
    - [Activate python virtual environment \& server](#activate-python-virtual-environment--server)
    - [Bootstrap for CSS styling in Python:](#bootstrap-for-css-styling-in-python)
    - [Creating database tables](#creating-database-tables)
    - [The views send data to html files](#the-views-send-data-to-html-files)
    - [Django admin for adding data to the tables](#django-admin-for-adding-data-to-the-tables)
    - [How does the url.py work?](#how-does-the-urlpy-work)
  - [Set up git repo locally](#set-up-git-repo-locally)

## TO DO list

## I was last doing:

  1. > Django tutorial, Blog App: Templates  https://www.removepaywall.com/article/current#blog-app-templates
  2. From the second tutorial, I stopped here: > https://docs.djangoproject.com/en/4.1/intro/tutorial02/  "Go to http://localhost:8000/polls/ in your browser, and you should see the text “Hello, world. You’re at the polls index.”, which"
  3. Part 3 ofthe second tutorial > https://docs.djangoproject.com/en/4.1/intro/tutorial03/
   
## Learned things  

1. It is NOT the same thing, to create a python project than to create a python app. Each project can have multiple apps running on it, and each app can be running 
  in multiple projects.

## Python Django tutorial 
1. From this python tutorial about django: https://realpython.com/get-started-with-django-1/
2. Another tutorial on how to build a *polling app* > https://docs.djangoproject.com/en/4.1/intro/tutorial01/
3. Good explanation of what is Django and how it's structured > https://www.w3schools.com/django/django_intro.php

### How to import files and functions 
Depends on the entry-point script.

In a file system like this:

```
application 
├── app
│   └── folder
│       └── file.py
└── app2
    └── some_folder
        └── some_file.py
```

We can import a function *function1* placed within *file.py* from *some_file.py* given that the main script is run in the **application** folder. In other words:
*Python only searches the directory that the **entry-point** script is running from and sys.path*. 

In the above example we would write inside the file *some_file.py*:

`from app1.folder.file import function1`

considering the main script is executed in the folder *application*.

I had to do this for importing the *views.py* file while running the *urls.py* file placed withing my *hello_world* folder. My file system was the following:

```
application 
├── db.sqlite3
├── hello_world
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── hello_world.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── LEARNED_things_and_TODO.md
├── manage.py
├── personal_portfolio
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

### Activate python virtual environment & server

Just run

`source venv/bin/activate`

for activating the previously created python virtual environment. In order to run the python server, just run:

`python manage.py runserver`

### Bootstrap for CSS styling in Python:
 We can use **Boostrap** to style our front-end, without having to do all the details of CSS! Isn't this cool? https://getbootstrap.com/docs/4.1/getting-started/introduction/#quick-start

### Creating database tables

1. A database table is a django *model*. Each model is a class (in python) where each property will be a column in the database table, and where each instance will be a new row of the table. By default Django uses *SQLite*.

2. In order to create a table, we create a **migration** using the command:
   `python3 manage.py makemigrations projects`
   where *projects* is the directory that contains the *models.py* file. Inside the *models.py* the classes (or database tables) are declared.

3. First we create a model class (or table), then a migration.

4. Finally we *apply the migrations* or database table creations, by runnin the command:
   `python3 manage.py migrate projects`

### The views send data to html files

 As the tutorial says: *view functions to send the data from the database to the HTML templates*

### Django admin for adding data to the tables

### How does the url.py work?

This file is called informally the URLconf of python. It has an:

1. **path() argument: route**

*route* is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.

Patterns don’t search GET and POST parameters, or the domain name. For example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/. In a request to https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.

2. **path() argument: view**

When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments. We’ll give an example of this in a bit.

3. **path() argument: kwargs**

Arbitrary keyword arguments can be passed in a dictionary to the target view. We aren’t going to use this feature of Django in the tutorial.

4. **path() argument: name**

Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

When you’re comfortable with the basic request and response flow, read part 2 of this tutorial to start working with the database.


## Set up git repo locally

In order to start ur dir run

`git init .`

2. Then create a repo on github.com

3. Then run

```
git add .
git commit
```

and then 
```
git push origin url.of.repository
```

in my last case for "inversions" this is the command that worked:

```
git remote add origin url.of.repository
git push -u origin master
```

For storing your token run
`git config --global credential.helper store`

After running this command, do a commit and push, and when you input your password/token again, it will be saved forever.