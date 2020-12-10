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

## Operations

### Definitions

```javascript
> let a = 10
undefined
> let b = 6
undefined
> let c = 0
undefined
> a.toString(2)
"1010"
> b.toString(2).padStart(4, "0")
"0110"
> c.toString(2).padStart(4, "0")
"0000"
```

### Logical AND

Evaluates all operands and returns the last one.

```javascript
> a && b
6
> b && a
10
> Boolean(a && b)
true
> a && b && c
0
```

### Logical OR

Evaluates operands using shortcut evaluation and returns the last evaluated.

```javascript
> a || b
10
> b || a
6
> Boolean(a || b)
true
> a || b || c
10
> c || b || a
6
```

### Bitwise AND

The result is AND applied to every pair of bits in the operands.

```javascript
> a & b
2
> b & a
2
> (a & b).toString(2).padStart(4, "0")
"0010"
> a & b & c
0
```

### Bitwise OR

The result is OR applied to every pair of bits in the operands.

```javascript
> a | b
14
> b | a
14
> (a | b).toString(2).padStart(4, "0")
"1110"
> a | b | c
14
```

### Bitwise XOR

The result is XOR applied to every pair of bits in the operands.

```javascript
> a ^ b
12
> b ^ a
12
> (a ^ b).toString(2).padStart(4, "0")
"1100"
> a ^ b ^ c
12
```
