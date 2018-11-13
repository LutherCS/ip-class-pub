# Shopping List: Server Side

This is a continuation of the Shopping List project.

Use Flask to save a user's shopping list on the server side (use of a database is **optional**) and return this list to a client when asked.

It is not required to use Jinja2 templates for this project, you may reuse the existing structure. Hint: use `send_from_directory` and/or `static_url_path`.

Refer to *notes/flask_api_server* for details of the server-side API implementation.

## Flask Routes

* `/`: redirect to */static/shopping_list.html*

* `/save`: save the content of `request.data` to a file on the server (or a database, if you want a challenge). Accepted method: *POST*.

* `/get`: retrieve the content of the previously created file and return it as *application/json* (set proper response header). Consider a case of a the file not being created yet and handle it properly. Accepted method: *GET*.

* Use proper routes to server static content (html, js, css).

## JavaScript Update

If you have the *Model-View-Controlled* pattern properly implemented, then you only need to make changes to the *controller*.

Function *save_list* (or similar) should send a *POST* request to `/save` with the shopping list items as `body`.

Function *populate_list* (or similar) should send *GET* request to `/get` and use the returned JSON to populate the shopping list (table).

## References

* [Using Fetch - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

* [python - Flask Response vs Flask make_response - Stack Overflow](https://stackoverflow.com/questions/40217464/flask-response-vs-flask-make-response)
