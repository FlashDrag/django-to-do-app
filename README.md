# TO DO
Mini project to practice Django CRUD operations

Live Demo: https://to-do-app-django.herokuapp.com/

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
- [Cloudinary](https://cloudinary.com/)

## Project Setup
- ### Virtual Environment
#### Set Up Virtualenv with Virtualenvwrapper on Ubuntu 22.04
1. Create a virtual environment:
    ```
    $ cd <path to project>
    $ mkvirtualenv -a <path to project> <name of virtual environment>
    ```

    (flag `-a` means to associate the virtual environment with a project)

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

        - **Install dj-database-url: `pip install dj_database_url`**

        ```
        development = os.getenv('DEVELOPMENT', False)
        DEBUG = development

        if development:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        else:
            # Parse database configuration from $DATABASE_URL
            import dj_database_url
            DATABASES = {
                'default': dj_database_url.config(
                    default=os.getenv('DATABASE_URL')
                )
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
### Hosting static files - Cloudinary Setup
    Hosting static files on Heroku is not recommended for production apps. Instead, use a cloud storage service like Amazon S3, Cloudinary, Azure Blob etc. The version of the app with hosted static on the same Heroku server as the app you can find on the `local-static` branch.

    - Add the following to the `settings.py` file:
        ```
        # Cloudinary settings
        INSTALLED_APPS = [
            # ...
            'cloudinary_storage',  # Must be above `django.contrib.staticfiles`, to override default static storage
            'django.contrib.staticfiles',
            'cloudinary',
            # ...
        ]

        # STATIC FILES(CSS, JS, IMAGES)
        # Credentials for the cloudinary_storage. Can be found in the Cloudinary dashboard
        CLOUDINARY_STORAGE = {
            'CLOUDINARY_URL': os.getenv('CLOUDINARY_URL'),
        }
        # OR
        CLOUDINARY_STORAGE = {
            'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
            'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
            'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
        }

        # URL path for your static files.
        # This is the URL path where your static files will be served from.
        # Example path for cloudinary css file: `https://res.cloudinary.com/<cloud_name>/raw/upload/v1/static/django_todo/css/style.css`
        STATIC_URL = '/static/django_todo/'
        # Dir where your static files are stored locally during development
        STATICFILES_DIRS = [os.path.join(BASE_DIR, "todo/static"), ]
        # Dir where static files are stored during production, after running collectstatic
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        # Cloudinary's storage for static files with hashed names
        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

        # URL path for media files
        MEDIA_URL = '/media/django_todo/'
        # Media cloudinary storage
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        ```
    - Create a `media` and `static` and in the root directory of the project or in the app directories. The `media` folder will     contain all media files uploaded by users, and the `static` folder will contain all static files such as CSS, JS, and images.
    
    - Add to a `base.html` file in the `templates` folder the following:
        ```
        {% load static %}
        ```

    - Deploy the app on HEROKU or run the following command to collect static files if the command didn't run automatically:

        ```
        $ python manage.py collectstatic
        ```

    Usually the `$ python manage.py collectstatic` command runs automatically when deploying on HEROKU.

    If you don't use static files, you can prevent this command from running automatically during deployment on Heroku, by setting `DISABLE_COLLECTSTATIC` to `1` in the Heroku config vars. If you already run this command manually, you don't have to disable it on HEROKU, as it won't upload the files again if they didn't change.
        ```
        $ heroku config:set DISABLE_COLLECTSTATIC=1
        ```

    **Notes:**
    - In production, you must set `DEBUG` to `False` to fetch static files from Cloudinary. With `DEBUG` equal to `True`, Django `staticfiles` app will use your local files for easier and faster development (unless you use `cloudinary_static` template tag).

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