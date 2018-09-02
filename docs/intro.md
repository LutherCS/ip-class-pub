# Client-server architechture

Client-side technologies (non-exclusive list)

* HTML
* CSS
* JavaScript

Server-side technologies (non-exclusive list)

* CGI
* PHP
* Python
* Flask
* Templates

Storage-related technologies (non-exclusive list)

* Databases
* SQLAlchemy
* Cookies
* Local storage

## Web terminology

* Client (Browser)
* Server
* Protocol
    * [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
    * [SSH](https://en.wikipedia.org/wiki/Secure_Shell)
    * [DNS](https://en.wikipedia.org/wiki/Domain_Name_System)
    * [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
    * [HTTPS](https://en.wikipedia.org/wiki/HTTPS)    
* IP address
    * localhost: 127.0.0.1
    * any: 0.0.0.0
* Port
    * FTP: 21
    * SSH: 22
    * DNS: 22
    * HTTP: 80
    * HTTPS: 443
* HTTP methods
    * POST (submit/create)
    * GET (retrieve)
    * PUT (update)
    * DELETE (delete)
* HTTP status codes
    * Successful: __2xx__
    * Redirection: __3xx__
    * Client error: __4xx__
    * Server error: __5xx__

Using `telnet` to retrieve web resources interactively

```
telnet luther.edu 80
Trying 174.129.25.170...
Connected to luther.edu.
Escape character is '^]'.
GET /index.html
<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.12.2</center>
</body>
</html>
Connection closed by foreign host.

```

Specify HTTP version (1.1) and host for a detailed response.
```
telnet luther.edu 80
Trying 174.129.25.170...
Connected to luther.edu.
Escape character is '^]'.
GET /index.html HTTP/1.1
Host: luther.edu

HTTP/1.1 301 Moved Permanently
Server: nginx/1.12.2
Date: Sun, 02 Sep 2018 20:51:05 GMT
Content-Type: text/html
Content-Length: 185
Connection: keep-alive
Location: http://www.luther.edu/index.html

<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.12.2</center>
</body>
</html>
Connection closed by foreign host.
```
