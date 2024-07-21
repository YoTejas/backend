# backend

## About the Project

This is a django application containing APIs for Vista Residency's Website.  

## Installation Steps

To install the following app on your local system follow the steps given below:

- Install Python 3.10.7

- Install virtualenv

- Clone the repository:

    ```
    git clone https://github.com/Vista-Residency/backend.git
    ```

- Change directory to newly cloned repository:

    ```
    cd backend
    ```

- Create a virtual environment: 

    ```
    virtualenv env
    ```
 
- Switch to the newly created environment:

    ```
    cd env/Scripts
    ```

    ```
    ./activate
    ```

- Return Back to the parent directory:

    ```
    cd ../../
    ```

- Build the environment using the given requirements:

    ```
    pip install -r requirements.txt
    ```

- Start the django server:

    ```
    python manage.py runserver
    ```

- Access Django Admin at:
    ```
    URL: http://localhost:8000/admin
    username: admin
    password: admin
    ```

- This application is hosted on Azure App Service
