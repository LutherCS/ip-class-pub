# Final Project

Your final project must be written using the **Flask** framework with properly designed user interface. It can be a project based around almost anything as long as it meets the following criteria in terms of the use of **Flask**.

## Option C
*This is a low risk / low reward path.*

For a **maximum grade of C (&approx;73%)** you can follow steps 1-11 (skipping 10, email) of Miguel Grinberg's [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

By following the tutorial you should be able to build a simple micro-blogging service using Flask and related technologies.

You application must be functional and have consistent user interface.

This option is available to **individual students** only. A team must choose another option.

## Option B
*This is a path of applying existing skills.*

For a **maximum grade of B (&approx;83%)** you must develop an original web application. It must include the following components:

* At least three **controllers** (routes)

* At least three **views** (templates)

* Make use of **persistent data** - something must be stored and accessed from the database. 
    * Use *psycopg2*, *records*, or another Python DB API
    * Use *SQLite3* or *PostgreSQL* DBMS
    * Only **1 (one)** table is required

* Some type of form processing so that your application is **interactive**
    * Use *GET* and *POST* methods

* Aesthetically appealing and consistent user interface
    * Use *Bootstrap*


## Option A
*This is a path of creativity and challenge.*

For a **maximum grade of A (&approx; 93%)** your application must meet all the requirements of **Option B** and have additional complexity. It must meet the following **additional** requirements:

* Make use of **persistent data** - something must be stored and accessed from the database. 
    * At least **3 (three)** tables are required

* Aesthetically appealing and consistent user interface
    * Use *Vue* or another JavaScript framework

* Develop AJAX API for some aspect of the project that you use in your web pages.

## Option A+
*This is a path of learning.*

For a **maximum grade of A+ (100%)** your application must meet all the requirements of **Option A** and have at least 1 (one) additional component/technology. Note that you may have to learn that technology yourself.

* Access [Amazon Voice](https://developer.amazon.com/alexa-voice-service) API

* Use [WTForms](https://wtforms.readthedocs.io/en/stable/) module for form processing

* Use [SQLAlchemy](https://www.sqlalchemy.org/) toolkit

* Use [Open Source Document Database | MongoDB](https://www.mongodb.com/) instead of a relational database

* Use [NGINX | High Performance Load Balancer, Web Server, & Reverse Proxy](https://www.nginx.com/) instead of the Flask's built-in server

* Deploy on [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

* Something else (vetted by me)

## Grading Criteria

Grading scale for **original** projects.

Criterion | Option C<sup>1</sup> | Option B | Option A | Option A+
---|---|---|---|---
Working application | 15 | 15 | 15 | 15
Original idea || 20 | 20 | 20
Single route | 10 | 10 | 10 | 10
Additional routes | 5 | 5 | 5 | 5
Single template | 10 | 10 | 10 | 10
Additional templates | 5 | 5 | 5 | 5
Python DB API | 10 | 10 | 10 | 10
DBMS | 10 | 10 | 10 | 10
Single table | 10 | 10 | 10 | 10
Additional tables | 5 | | 5 | 5
Form | 10 | 10 | 10 | 10
*GET* method | 10 | 10 | 10 | 10
*POST* method | 5 | 5 | 5 | 5
Bootstrap | 5 | 5 | 5 | 5
Front-end framework ||| 5 | 5
Custom API ||| 5 | 5
New technology |||| 10
||||
**Total** | **110** | **125** | **140** | **150**

[1] Point breakdown for **Option C** is approximate.

## References

* [LutherCS/ip-class-pub: CS330 public repository](https://github.com/LutherCS/ip-class-pub)
