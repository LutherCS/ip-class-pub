# JavaScript

* Install [nodejs](https://nodejs.org/en/download/package-manager/) to run JavaScript scripts locally

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

* Install *jshint* (don't forget to install jshint extension in VS Code)

```bash
sudo npm install -g jshint
```

* Include the following in your JavaScript file:

```javascript
/* jshint esversion: 6 */
/* jshint node: true */
'use strict';
```

* Run `hello.js` in terminal using *nodejs*

```bash
node hello.js
```

* Include JavaScript in HTML

```html
<head>
<script src='hello.js'></script>
</head>
```

* Start the server

```bash
python3 -m http.server
```

* Open `hello.html` in a browser

```bash
http://localhost:8000/hello.html
```

## Scope

*Hoisting* - declarations are moved to the top of the **scope**

Modifier | Scope | Hoisted | ES Version
---|---|---|---
let | block | no | 2015
var | function / global | | 1
const | block | no | 2015
none | global | | 1
