# Shopping List: Server Side

This is a continuation of the Shopping List project.

Use Flask to save a user's shopping list on the server side (use of a database is **optional**) and return this list to a client when asked.

It is not required to use Jinja2 templates for this project, you may reuse the existing structure. Hint: put your JavaScript, CSS, and HTML files in the directory named `static` or use `send_from_directory` to server files from `js` and `css` directories. See references for details.

Refer to *notes/flask_api_server* for details of the server-side API implementation.

Read all the referenced materials carefully.

## Flask Routes

* `/`: redirect to */static/shopping_list.html*

* `/save`: receive data from the client and save the content of `request.data` to a file on the server (or a database, if you want a challenge). Accepted method: *POST*.

* `/get`: return the content of the previously created file as *application/json* (set proper response header). Consider a case of a the file not being created yet and handle it properly. Accepted method: *GET*.

* Use proper routes to server static content (html, js, css).

## JavaScript Update

If you have the *Model-View-Controlled* pattern properly implemented, then you only need to make changes to the *controller*.

Function *save_list* (or similar) should send a *POST* request to `/save` with the shopping list items as `body`.

Function *populate_list* (or similar) should send *GET* request to `/get` and use the returned JSON to populate the shopping list (table).

## References

* [Using Fetch - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

* [Static files — Explore Flask 1.0 documentation](http://exploreflask.com/en/latest/static.html)

* [python - Flask Response vs Flask make_response - Stack Overflow](https://stackoverflow.com/questions/40217464/flask-response-vs-flask-make-response)

* [python - How to serve static files in Flask - Stack Overflow](https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask)
