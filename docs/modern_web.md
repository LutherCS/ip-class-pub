# Modern Web Applications

```
Client -> Web Server
          /    | 
     Static---App---DB   
```

## Common Gateway Interface

CGI allows you to generate dynamic sites using any language (Perl, C++, Python) at the back-end. Tedious and time-consuming process, 

Start the Python built-in http server in the current directory. By default it listens on port 8000 but a specific port can be provided as an argument.

```
python3 -m http.server [port]
```
    
Serve output of everything in *cgi-bin* as html

```
python3 -m http.server --cgi
```

Let's generate a page using CGI and Python

```
mkdir cgi-bin
cd cgi-bin
echo #!/usr/bin/env python3 > hello.py
vi hello.py
...
chmod +x hello.py
```

Retrieve the resource

In the browser

```
http://localhost:8000/cgi-bin/hello.py
```

Using `telnet`

```
telnet localhost 8000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET /cgi-bin/hello.py HTTP/1.1

HTTP/1.0 200 Script output follows
Server: SimpleHTTP/0.6 Python/3.5.2
Date: Tue, 04 Sep 2018 02:12:03 GMT
Content-type: text/html

<html>
<head><title>2018-09-03 21:12:03.760729</title></head>
<body>Hello from Python</body>
</html>
Connection closed by foreign host.

```

## LAMP Stack

* Linux
* Apache / nginx
* MySQL / Postgresql
* PHP / Python

Beyond LAMP

* Ruby on Rails (Ruby)
* Django / Pyramid / **Flask** (Python)
* Tomcat (Java)

## MEAN Stack

* MongoDB (DB)
* Express.js (server)
* AngularJS (language)
* Node.js (OS, kind of)

## SPA

Single-page application
