# JavaScript promises

## Callback

*Callback* is a way for one (higher order) function to call another (callback) and make sure it (another function) doesn’t execute until after the first one is done.

```javascript
function eat(food, f) {
    console.log(`Eating ${food}`);
    f();
}
eat("veggies", function() {
    console.log("Done eating");
});
```

## Closures

*Closures* are functions that refer to independent variables. The function defined in the closure **remembers** the environment in which it was created ()

```javascript
function done(activity, noun) {
    return function() {
        console.log(`Done ${activity} ${noun}`);
    }
}
```

## async/await

## Promise

## References

* [JavaScript Promises: an Introduction  |  Web Fundamentals](https://developers.google.com/web/fundamentals/primers/promises)
* [Using Promises - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
* [Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
* [async function - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
* [Declaring and Using Callbacks - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/js-ctypes/Using_js-ctypes/Declaring_and_Using_Callbacks)
* [Closures - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* [JavaScript: What the heck is a Callback? - codeburst](https://codeburst.io/javascript-what-the-heck-is-a-callback-aba4da2deced)
* [Passing arguments to callback functions](https://www.jstips.co/en/javascript/passing-arguments-to-callback-functions/)
