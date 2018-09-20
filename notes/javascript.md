# JavaScript

* Install [nodejs](https://nodejs.org/en/download/package-manager/) to run JavaScript scripts locally

```
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

* Install jshint (don't forget to install jshint extension in VS Code)

```
sudo npm install -g jshint
```

* Include the following in your JavaScript file:

```
/* jshint esversion: 6 */
'use strict';
```

* Include JavaScript in HTML

```
<head>
<script src='somescript.js'></script>
</head>
```
