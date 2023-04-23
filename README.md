# TO DO
Mini project to practice Django CRUD operations

_Styled with Bootstrap 4.6.2_

## Features
- [x] Create a new task
- [x] Edit a task
- [x] Delete a task
- [x] Mark a task as done
- [x] Unmark a task

## Technologies Used
- [Django 3.2.18](https://www.djangoproject.com/)
- [Bootstrap 4.6.2](https://getbootstrap.com/docs/4.6/getting-started)
- [jQuery 3.5.1](https://jquery.com/)
- [Font Awesome](https://fontawesome.com/)

## Project Setup
- ### Virtual Environment
#### Set Up Virtualenv with Virtualenvwrapper on Ubuntu 22.04
1. **Create a virtual environment** (flag `-a` means to associate the virtual environment with a project):
    ```
    $ cd <path to project>
    $ mkvirtualenv -a <path to project> <name of virtual environment>
    ```
2. Activate the virtual environment:
    ```
    $ workon <name of virtual environment>
    ```

- ### Django Setup
[Hello Django Instructions Sheet](https://docs.google.com/document/d/113P2BPOkrG6rMxsrm8GCbO6CVG2b1R9htD4tRdkSltQ/edit#heading=h.hvy9tw74f1o0)
1. Install Django:
    ```
    $ pip install django
    ```
2. Configuring Environment Variables:
    - Install `python-dotenv`:
        ```
        $ pip install python-dotenv
        ```
    - Import the `load_dotenv()` function in the `<settings.py>` file:
        ```
        from dotenv import load_dotenv
        load_dotenv()
        ```
    - Create environment variable `<.env>` for sensitive information and add it to the `<.gitignore>` file:
        ```
        $ touch .env .gitignore
        $ echo .env >> .gitignore
        ```
    - Set the environment variables in the `<.env>` file:
        See the `<.env_example>` file.
    - Import the environment variables in the `<settings.py>` file:
        ```
        import os
        SECRET_KEY = os.getenv('SECRET_KEY')
        ```
    - Update the DATABASES setting in `settings.py`:

    **# install `dj-database-url`: `pip install dj_database_url`**

        ```
        if DEBUG == 'True':
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }
        else:
            import dj_database_url

            if DEBUG:
                # --//--
            else:
                DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
        ```

3. Create a Django project:
    ```
    $ django-admin startproject <name of project> .
    ```
4. Run the Django server:
    - Install `livereload` extension for the browser to refresh the browser automatically:

        LiveReload extension for Chrome: https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei?hl=en
        ```
        $ pip install livereload
        ```
    - Run servers and enable LiveReload extension in the browser:
        ```
        $ python manage.py runserver
        $ livereload
        ```

5. Create a Django app:
_Allows Django to recognize the app and look for a template folder in the app_
    ```
    $ python manage.py startapp <name of app>
    ```
    - Add the app to the `INSTALLED_APPS` list in `settings.py`:
        ```
        INSTALLED_APPS = [
            ...
            '<name of app>',
        ]
        ```
    - Add the app to the `urls.py` file of the project:
    _This will allow the app to have its own `urls.py` file and registers any URLs defined there. And the app's `urls.py` file will be used to define the all routes for the certain app_
        ```
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('<name of app>.urls')),
        ]
        ```
    - Create a `urls.py` file in the app:
        ```
        from django.urls import path
        from . import views

        urlpatterns = [
            path('url_path/', views.<name of view function>, name='<name of view function>'),
        ]
        ```
6. Create a Django superuser:
_Allows you to access the admin UI panel and manage the database_
    ```
    $ python manage.py createsuperuser
    ```

- ### Database Setup
#### Django Local Migrations
1. Make migrations:
The `makemigrations` command looks at the models you have defined in your apps and creates a set of migration files for those changes.
    ```
    $ python manage.py makemigrations
    ```
2. Migrate:
The `migrate` command takes all of the migration files and runs them against your database - synchronizing the changes you made to your models with the schema in the database.
    ```
    $ python manage.py migrate
    ```

- Show migrations:
The `showmigrations` command shows all migrations that have been applied or unapplied.
    ```
    $ python manage.py showmigrations
    ```

## Testing
### Unit Testing
The app tested with the `unittest` Django module.

- To run the tests:
    ```
    $ python manage.py test
    ```
- To run the tests from a specific app:
    ```
    $ python manage.py test <name of app>
    ```
- To run the tests from a specific file:
    ```
    $ python manage.py test <name of app>.test_<name of file>
    ```
### Coverage
Coverage is a tool that allows you to measure the percentage of code that is covered by your tests.

- Install `coverage`:
    ```
    $ pip install coverage
    ```
- To run the tests with coverage:
    ```
    $ coverage run --source=<name of app> manage.py test
    $ coverage report
    ```
- View the coverage report in the browser:
    ```
    $ coverage html
    ```

    _Open the `htmlcov/index.html` file in the browser_

## Deployment
### Heroku CLI

[Django-Heroku settings.py example](https://github.com/heroku/python-getting-started/blob/main/gettingstarted/settings.py)

- Install psycopg2 database adapter to use PostgreSQL with Django:
    ```
    $ pip install psycopg2-binary
    ```

    _Note: psycopg2-binary is a package that contains pre-built binaries of psycopg2. It is easier to install and requires fewer dependencies than psycopg2_

- Install gunicorn to replace the Django development server:
    ```
    $ pip install gunicorn
    ```
- Configure `staticfiles`:
    - Add the following to the `settings.py` file:
        ```
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        ```
    - Install [WhiteNoise](https://whitenoise.readthedocs.io/en/stable/django.html) to serve static files:
        ```
        $ pip install whitenoise
        ```
    - Add the following to the `settings.py` file:
        ```
        MIDDLEWARE = [
            # ...
            "whitenoise.middleware.WhiteNoiseMiddleware",
            # ...
        ]
        ```
- Create requirements file:
    ```
    $ pip freeze > requirements.txt
    ```
- Create a Heroku Procfile:
    ```
    $ touch Procfile
    ```
- Add the following to the Procfile:
    ```
    web: gunicorn <name of project>.wsgi:application
    # e.g: `web: gunicorn django_todo.wsgi:application`
    ```
- Login to Heroku:
    ```
    $ heroku login
    ```
- Create a Heroku app:
    ```
    $ heroku create <name of app> --region eu
    ```
- Set the environment variables in Heroku:
    ```
    $ heroku config:set <name of variable>=<value of variable>
    ```
- Add the Heroku app URL to the ALLOWED_HOSTS list in `settings.py`:
    ```
    ALLOWED_HOSTS = ['<name of app>.herokuapp.com']
    ```
- Commit and push the code to Heroku:
    ```
    $ git add .
    $ git commit -m "Setup Heroku files for deployment"
    $ git push heroku master
    ```
- Run the migrations on Heroku:
    ```
    $ heroku run python manage.py migrate
    ```


## Credits
Personal edition of the TODO webapp from the [Code institute](https://codeinstitute.net/) walkthrough project.

Favicon taken from [icons8](https://icons8.com/)