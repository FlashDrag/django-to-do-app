# TO DO


## Technologies Used
...

## Project Setup
- ### Virtual Environment
#### Set Up Virtualenv with Virtualenvwrapper on Ubuntu 22.04
1. **Create a virtual environment** (flag `-a` means to associate the virtual       environment with a project):
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

2. Create a Django project:
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
#### Migrations
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