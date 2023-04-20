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
2. Configuration:
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
    - Move sensitive information from `<settings.py>` to `<.env>` file.

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

- Create a Django app:
    ```
    $ python manage.py startapp <name of app>
    ```
