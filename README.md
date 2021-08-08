# Basic Matcher

##### This repo is a Django app using REST framework for matching between jobs to candidates based on their skills.

# Permissions
#### Admin:
- username: adi
- password: 1234

#### Getting Started
Clone the project from the github repository
```sh
git clone https://github.com/Adiso-1/matcher-service.git
```
Recreate the virtual environment
```sh
python -m venv ./venv
```
Activate the virtual environment
```sh
venv/scripts/activate
```
Install the requirements
```sh
pip install -r requirements.txt
```
#### Run on loclhost:
```sh
python .\manage.py runserver
```
# Example - How to make a job request:
```sh
http://127.0.0.1:8000/jobs/candidates_finder/?job=frontend
```
This query will return a JSON format of the candidates who are suitable for the frontend positions' skills.
