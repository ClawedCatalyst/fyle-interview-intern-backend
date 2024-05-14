# Fyle Backend Challenge

- [X] Added Missing Missing APIs
- [X] Improved the Test Coverage to 95%
- [X] Dockerised the Application with Dockerfile and docker-compose.yml
<img width="1396" alt="image" src="https://github.com/ClawedCatalyst/fyle-interview-intern-backend/assets/97229491/6889b8bc-a18e-49d9-80db-808a9377f9a0">

## Installation

### Run using Docker

To run the docker on local machine simply run the following command:

```
docker-compose up -d
```

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```


# About Me:

Hello! I’m Suhail!
I am a passionate and dedicated backend developer based in Delhi, India. Throughout my career, I have honed my skills in various programming languages, including C/C++ and Python. I have expertise in developing robust and scalable web applications using frameworks such as FastAPI, Django, and Django Rest Framework. I have hands-on experience with databases such as SQLite and PostgreSQL. Moreover, I am familiar with tools and technologies like VSCode, Git, Docker, AWS, MS Azure, Redis, Gunicorn, and Nginx.

Hackathons hold a special place in my heart; they are where I truly thrive. Over the years, I’ve actively participated in hackathons. I secured the 1st Runner-Up position in “Paradigm,” a national-level hackathon held at Shiv Nadar University (SNU), Greater Noida. Notably, I achieved the coveted “Finalist” position in a national-level hackathon hosted by the prestigious Indian Institute of Technology (IIT) Guwahati.

### Medium Artciles: 
[Lightning-Fast Search with MeiliSearch and Python](https://medium.com/@suhail2021.25/lightning-fast-search-with-meilisearch-and-python-5aba7d92ad81)
<br>
[Lightning-Fast Search with MeiliSearch and Python (Part 2)](https://medium.com/@suhail2021.25/lightning-fast-search-with-meilisearch-and-python-part-2-9b682546d176)

