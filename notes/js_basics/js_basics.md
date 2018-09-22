# JavaScript

* Install [nodejs](https://nodejs.org/en/download/package-manager/) to run JavaScript scripts locally

```
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

* Install *jshint* (don't forget to install jshint extension in VS Code)

```
sudo npm install -g jshint
```

* Include the following in your JavaScript file:

```
/* jshint esversion: 6 */
/* jshint node: true */
'use strict';
```

* Run `hello.js` in terminal using *nodejs*

```
node hello.js
```

* Include JavaScript in HTML

```
<head>
<script src='hello.js'></script>
</head>
```

* Start the server

```
python3 -m http.server
```

* Open `hello.html` in a browser

```
http://localhost:8000/hello.html
```
