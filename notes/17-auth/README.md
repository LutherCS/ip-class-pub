# User management

## Goals

Develop a small application that uses `Flask-Login`, `Flask-SQLAlchemy`, and `Flask-WTF` to maintain user sessions and protect some resources within the application.

## Outcomes

An application with the following functionality:

- List of tech companies Companys with cities hidden for anonymous users.
- Registration (signup) and authentication (login) forms and routes.

## Demo

```sql
CREATE TABLE IF NOT EXISTS company (
        id INTEGER autoincrement,
        name TEXT NOT NULL,
        revenue FLOAT,
        employees INTEGER,
        country TEXT,
        headquarters TEXT,
        PRIMARY KEY (id)
);
CREATE TABLE user (
        id INTEGER NOT NULL, 
        email VARCHAR NOT NULL, 
        name VARCHAR, 
        password VARCHAR, 
        PRIMARY KEY (id), 
        UNIQUE (email)
);
CREATE TABLE favorite (
        id INTEGER NOT NULL, 
        user_id INTEGER, 
        company_id INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(user_id) REFERENCES user (id), 
        FOREIGN KEY(company_id) REFERENCES company (id)
);
```

Use the following command to run the application:

```bash
flask --app navigator run
```

## References

- [Flask-Login — Flask-Login 0.6.3 documentation](https://flask-login.readthedocs.io/en/0.6.3/)
- [Flask-WTF — Flask-WTF Documentation (1.2.x)](https://flask-wtf.readthedocs.io/en/1.2.x/)
- [WTForms — WTForms Documentation (3.1.x)](https://wtforms.readthedocs.io/en/3.1.x/)
- [Quick Start — Flask-SQLAlchemy Documentation (3.1.x)](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/)
- [How To Add Authentication to Your App with Flask-Login | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
- [How to Perform User Authentication with Flask-Login — SitePoint](https://www.sitepoint.com/flask-login-user-authentication/)
