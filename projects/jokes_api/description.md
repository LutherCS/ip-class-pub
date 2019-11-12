# Build and deploy an API

## Server side

1. Deploy on [Cloud Application Platform | Heroku](https://www.heroku.com/)
1. When accessed at URL <https://username.herokuapp.com/api/v1/jokes> your service must return a **random** joke from the `pyjokes` collection
1. When accessed at URL <https://username.herokuapp.com/api/v1/jokes/id> (where **id** is an integer), your service must return the **specified** joke from the `pyjokes` collection
1. Return valid JSON
1. The application must not crash. Note that *404 Not Found* is a valid response, not a crash.

## Client side

1. Deploy on <http://knuth.luther.edu/>
1. A combination of HTML nd JavaScript
1. The interface is a single button
1. On button click the request is sent to the server and the response is processed
1. Use Bootstrap for consistent styling

## References

* [API Design Guide — API Design Guide 0.1 documentation](https://apiguide.readthedocs.io/en/latest/)
* [Flask-CORS — Flask-Cors 3.0.7 documentation](https://flask-cors.readthedocs.io/en/latest/)
* [Using Fetch - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
* [Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
