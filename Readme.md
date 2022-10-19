# Tulip : Tuition Management System

## Project Requirements:
1. Creation of Students, Teachers, and assignments should be supported from the Django admin site to create update, and delete.
2. Create an API that can Get a JWT token when a valid username and password are present.
3. Create an API GET student details :
(Note: Based on token if the user is a student)

## Methodology:
1. Created custom user for whom roles can be assigned.
2. Here is roles map:
        ```
        {
            "student":1,
            "teacher":2,
            "admin":3  # unused as of now
        }
        ```
3. created custom permissions to check the user roles. permissions.py file in tulip_api_app.
4. Configured authetication for DRF
5. Created Models for Subjects , Teachers, Students.
6. Created Required Views and added configurations.
7. Did a lot of googling 😄.

I am sure i have missed a lot of steps in Methodology.

## Exposed  Api Endpoints

1. To get authentication token http://127.0.0.1:8000/token/  [POST]:
   
    To get JWT token accepts username and password as Form Data.
    Output : ``` {"token":"f467897dc6e9970ef16db947644ada12eabbd537"} ```
2. To get details of perticular user (if suthenticated as user) http://127.0.0.1:8000/api/student/details [GET] :

    OUTPUT: 
    ```
    {"id": 2,
    "student_name": "Vivek Pathade",
    "username": "vivek",
    "student_teachers": [
    {
      "id": 1,
      "teacher_name": "Mukund",
      "teacher_subjects": [
        {
          "id": 1,
          "subject_name": "Science"
        },
        {
          "id": 2,
          "subject_name": "History"
        },
        {
          "id": 3,
          "subject_name": "Mathematics"
        }
      ]
    },
    {
      "id": 2,
      "teacher_name": "Pranav Pathade",
      "teacher_subjects": [
        {
          "id": 1,
          "subject_name": "Science"
        },
        {
          "id": 2,
          "subject_name": "History"
        }
      ]
    },
      ]
    }
  ]
}
    ```

3. To update subjects for Teacher (if authenticated as teacher)  [PATCH]:  
    Example JSON BODY:
    ```
        {
            "teacher_subjects":
            [
                {
                    "id":1,
                    "subject_name":"Mathematics"
                    }
            ]
        }
    ```

## Other Endpoints
1. To get report of all students (Authentication not required)
    http://127.0.0.1:8000/api/students/report  [GET]

    OUTPUT:
    | ID | Student Name | Teachers | Subjects|
    |----|--------------|----------|---------|
    |1   |Vivek Pathade |Mukund Pathade, Xyz| Science, History
    |2   |Soham Pathade |Mukund Pathade, Xyz| Science, Geology


## Requirements to run this project
1. Python 3.9.5
2. Django
3. Django Rest Framework
 
## How to run
1. Create virtual environment ```$ python3 -m venv  venv  ```
2. Activate Virtual Environment.
3. Install Dependancies  ```$ (venv) pip install -r requirements.txt ```
4. Create migrations ```$ (venv) python manage.py makemigrations  ```
4. Apply migrations ```$ (venv) python manage.py migrate  ```
5. Run ```$ (venv) python  manage.py runserver ```

Please let me know your suggetions/ improvements on : pmukund1997@gmail.com



