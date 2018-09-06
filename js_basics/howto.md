# Working with simple JavaScript

1. Start the server

    ```
    python3 -m http.server

    ```

1. Install [nodejs](https://nodejs.org/en/download/package-manager/) to run JavaScript scripts locally

    ```
    curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    sudo apt-get install -y nodejs

    ```

* Install jshint (don't forget to install jshint extension in VS Code)

    ```
    sudo npm install -g jshint
    ```

1. Run `overview.js` in terminal using nodejs

    ```
    node overview.js

    ```

* Include the following in your JavaScript file:

    ```
    /* jshint esversion: 6 */
    /* jshint node: true */
    'use strict';

    ```

* Include JavaScript in HTML

    ```
    <head>
    <script src='overview.js'></script>
    </head>

    ```

1. Open static `overview.html` in a browser

    ```
    http://localhost:8000/overview.html
    
    ```