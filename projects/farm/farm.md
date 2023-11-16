# Farm to Table

Create a web app that would serve as a front for a local farm selling pork (and other products).

There should be a way for the farm owner to modify the inventory as follows:

- add a new item (including an image, a short description, availability, and price)
- edit existing item (e.g. change price)
- remove an item (or change its availability status)

Customers must be able to see available inventory and add items to their shopping cart. The cart should be modifiable as well.

There is no need to implement a formal checkout process, you can assume that the customer and the owner will conduct their business outside of the application.

## Requirements

- Admin (owner) interface with the following functionality:
  - add a new item
  - edit existing item
  - remove an item
- Customer interface with the following functionality:
  - see available items (or all items, with those unavailable clearly marked as such)
  - add item to the cart
  - make changes to the cart
- Use Jinja2 templates
- HTML/CSS framework used to style the application
- Use database (SQLite or Postgresql) to store inventory
- Application must be deployed

## Optional features

- Use SQLAlchemy to access the database
