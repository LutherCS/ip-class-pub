# CORS Proxy

It's possible to have a proxy server to solve the CORS issue.
The server would take a request and forward it to the target site (Fruityvice).
The response from the target would then be returned to the application.

## Running the app

Open a secondary terminal and start the proxy server (a Flask app).
This proxy is hardcoded to send requests to Fruityvice but can be changed to work with other APIs.
Note that you need Falsk and Flask-CORS installed for this proxy to work.

```bash
flask run
```

Run the application as usual.

```bash
python -m http.server -d notes/10-proxy
```
