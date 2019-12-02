# Final Project

Your final project must be a web application with the following major components:

* **Flask** framework
* **SQLite** or **PostgreSQL** database
* Consistent and appealing user interface
* RESTful API

## Technical specification

* Multiple routes

* Multiple templates

* Make use of **persistent data** - something must be stored and accessed from the database
  * Use *psycopg2*, *records*, or another Python DB API
  * Use DBMS (*SQLite3* is fine but *PostgreSQL* is better)
  * **1-3** tables required

* Some type of form processing so that your application is **interactive**
  * Use *GET* and *POST* methods

* Aesthetically appealing and consistent user interface
  * Use *Bootstrap* or another framework
  * *Vue* or another JavaScript framework

* Use and provide an API:
  * Access your app's API using JavaScript

* Deploy your application on the web
  * Heroku
  * pythonanywhere

* At least 1 (one) additional **new** component/technology. Note that you may have to learn that technology yourself.

  * *requests* to communicate with an external API
  * Use [MongoDB](https://www.mongodb.com/) instead of a relational database
  * Something else (vetted by me)

## Grading Criteria

**Tentative** grading scale for projects.

Criterion | Points
---|---
Original idea | 10
Working application | 10
Deployed application | 10
Single route | 5
Additional routes | 10
Single template | 5
Additional templates | 10
DBMS used (i.e. SQLite3) | 5
DBMS remote (i.e. PostgreSQL on Heroku) | 10
Single DB table | 5
Additional DB tables | 10
GET method | 5
POST method | 10
Bootstrap used | 5
Vue or similar used | 10
API provided | 10
API used to update the DB | 10
New technology | 10
|
**Total** | **150**

## References

* [LutherCS/ip-class-pub: CS330 public repository](https://github.com/LutherCS/ip-class-pub)
* [Creating Web APIs with Python and Flask | Programming Historian](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
* [API Design Guide — API Design Guide 0.1 documentation](https://apiguide.readthedocs.io/en/latest/index.html)
* [Developing a Single Page App with Flask and Vue.js | TestDriven.io](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/)
