# Popcorn sale

Create a web application to replace the paper-based popcorn sale form.
The application should be used to collect data about each purchase, store it in the database, and review at the level of an individual seller and the pack leader (kernel).
Do not implement authorization, all routes could be publicly accessible using a seller's id (your choice of a number, name, guid, etc).
Note that _Heroes and Helpers_ is a donation, not the popcorn flavor.

## Functional requirements

### Sale form

A scout should be able to able to add a new _sale_ using a form that includes the following fields:

- date
- customer's name
- customer's phone
- customer's address
- customer's selection
- payment method (cash/check)
- comment

The form should be scalable and usable on a mobile device.

Assume all sales to be final and non-refundable.

### Seller's view

A scout should be able to view and edit individual sale as follows:

- Edit name, address, or comment
- Mark an order as delivered

A scout should be able to see all the sales in a tabular format that includes information from each sale and the following fields:

- total dollar amount per customer (calculated, read-only)
- total number of purchased items per type of popcorn (calculated, read-only)

The form should be printable and appear consistent on paper.

An _order_ is all sales made by the same scout.

### Pack leader's view

Pack leader should be able to see sales statistics from all members of the pack with the following functionality:

- See total orders (dollar amount and number of items) of the pack.
- See total number of purchased items by flavor.
- See total dollar amount per scout.
- Mark dollar amount collected by a scout as correct.
- Mark order as delivered to an individual scout.
- Leave an optional comment for any order.

## Technical requirements

While this project is open-ended and you can make certain assumptions about the requirements, some features _must_ be present.

Your application must access data from the **SQLite database** and generate content using **Jinja templates**.
Database schema must be generated and accessed using **SQLAlchemy**.
Some data (flavors and prices) must be **imported** into the database from the (provided) CSV file while other data will be added based on user input.

The application must include several **routes** (e.g. _add_, _edit_, _view_, _all_, _scout_, _kernel_, etc).

While authentication is not required for this project, you must differentiate between the scout's and the kernel's interfaces.
Use **Flask blueprints** with different prefixes (e.g. `/scout` and `/kernel`).

The interface must be **consistent** and **visually appealing**.

The application must be **stable** and **deployed** (publicly available).

| Requirement                                     | Points |
| ----------------------------------------------- | ------ |
| **General functionality**                       | 60     |
| Multiple routes                                 | 5      |
| Multiple Jinja templates used                   | 5      |
| Separate blueprints for scouts and kernels      | 5      |
| Scout: add a new sale                           | 5      |
| Scout: view an existing sale                    | 5      |
| Scout: edit an existing sale                    | 5      |
| Scout: view summary of their order              | 5      |
| Kernel: view all orders of the pack             | 5      |
| Kernel: view all orders by flavor               | 5      |
| Kernel: view summary of any scout's order       | 5      |
| Kernel: mark an order of any scout as delivered | 5      |
| Kernel: comment on an order of any scout        | 5      |
| **Database**                                    | 20     |
| Multiple tables present in the SQLite database  | 5      |
| Data imported from CSV                          | 5      |
| Data is updatable                               | 5      |
| SQLAlchemy is used                              | 5      |
| **User interface**                              | 10     |
| User interface is consistent                    | 5      |
| User interface is visually appealing            | 5      |
| **Deployment**                                  | 10     |
| Application is deployed                         | 5      |
| Application is stable                           | 5      |
| **Total**                                       | 100    |

## References

- [Fueling Adventures. Funding Futures. | Pecatonica River Popcorn](https://pecatonicariverpopcorn.com/)
