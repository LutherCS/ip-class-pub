# JavaScript basics

Review the *script.js* file and make sure you understand how various JavaScript operations work.

Install [Node.js](https://nodejs.org/en/download/current) on your platform and use it to run the script.
Assuming you are in the top directory of the class repository, run the following:

```bash
node notes/02-js/script.js
```

## DOM manipulation

Use Python's built-in HTTP server to serve the *02-js* directory:

```bash
python -m http.server -d notes/02-js
```

Lines 70--81 in the *script.js* are an example of a simple DOM manipulation.
Once the `window` object is loaded, an anonymous function changes the content of the paragraph with `id` "greeting" from "Hello" to "Go home".

Look up and read about the following methods of the `document` object:

- `querySelector`
- `createElement`

Once you have an element's handle you can use the following methods and properties:

- `innerText`
- `innerHTML`
- `parentElement`
- `appendChild`

See the linked document for an example of DOM manipulation.

## References

- [DOM scripting introduction - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)
