# Pooyan Social Network :
### Discription :
This project contains two services. the first deals with user accounts and token (in pooyan network folder). the second one deals with apis related to posts, comments, likes, replies (in posts folder).

### Authentication Method :
Authentication method is jwt bearer token using djangorestframework-simplejwt library. Clients deal with Refresh and Access Token.

### Database :
Mongodb is prime Database in the project. it was better to use seperate databases for each service but i delibrately user one database for two services.(beacause my laptop whold crash running two instance of mongo at same time!!!). I used following command to run mongo:
```bash
docker run -p 27017:27017 --name pooyan -d mongo:latest
```
The db name is by default "pooyan" which can be changed by changing "MONGO_CLIENT" variable in setting.py in both services.

## Installation :
run the accounts service using:
```bash
python manage.py runserver 127.0.0.1:8000
```
run the accounts service using:
```bash
python manage.py runserver 127.0.0.1:5000
```
(ports are the same i used in Postman docs)

## Documentation :

i export postman collections and the are in each services. accounts.json in pooyan_network and posts.json in posts.