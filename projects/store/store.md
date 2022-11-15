# Corner Store

Create a web app that would serve as a front for a local shop. There should be a way for the store owner to add (create) a new item and for customers to see (list) available items. You don't have to implement API to connect front and to the back end.

This project brings together the last couple of weeks of class content, notably working with the databases and deployment.

## Requirements

* (30 pts) Admin (owner) interface
  * (10 pts) Ability to add an item to the inventory
  * (10 pts) Route `/add`, template `add.html`
  * (10 pts) Input form must be validated
* (30 pts) Customer interface
  * (10 pts) Ability to see inventory
  * (10 pts) Route `/list`, template `list.html`
  * (10 pts) Should not crash even if DB is empty
* (20 pts) Store inventory must use a database
  * (10 pts) Item must have at least three fields (columns): *name*, *category*, and *price*
  * (10 pts) SQLite or Postgresql (enable Postgresql add-on for your Heroku app, if necessary)
* (10 pts) Bootstrap or similar framework used to style the application
* (10 pts) Project must be deployed

## Demonstration

May be posted later.