# Security

Use Flask **session** to store information about a logged in user. See the Flask Quickstart for details.

## Requirements

1. Your application must have 3 (three) routes: `/`, `/login`, and `/logout`.
2. If the username property is not found in the **session** object, redirect user to the *login* page.
3. Present user with a choice of 2 (two) usernames, *Alice* and *Bob*.
4. Use **session** object to store information about a user (their *username*).
5. Once logged in, a user should be greeted by name.
6. Authenticated users should be able to log out, their information removed from the **session** object.
7. Use Jinja2 templates to create *main* and *login* views of your application.

## References

* [Quickstart — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [python - Understanding environment variable with Flask secret key-creation process - Stack Overflow](https://stackoverflow.com/questions/34213977/understanding-environment-variable-with-flask-secret-key-creation-process)
