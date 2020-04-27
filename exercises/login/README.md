# Security

Use Flask **session** to store information about a logged in user. See the Flask Quickstart for details.

## Requirements

1. Your application must have 3 (three) routes: `/`, `/login`, and `/logout`.
2. If the username property is not found in the **session** object, redirect user to the *login* page.
3. Present user with a way to specify their usernames (buttons, text, drop-down etc).
4. Use **session** object to store information about a user (their *username*).
5. Once logged in, a user should be greeted by name.
6. Authenticated users should be able to log out, their information removed from the **session** object.
7. Use Jinja2 templates to create *index* and *login* views of your application.
8. Use MUI to style user interface.

## References

* [Quickstart — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
