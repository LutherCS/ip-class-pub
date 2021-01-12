# Build and deploy an API

## Server side

1. Deploy on [PythonAnywhere](https://www.pythonanywhere.com/) or [Heroku](https://www.heroku.com/)
1. When accessed at URL <https://service.com/api/v1/jokes> your service must return a _random_ joke from the `pyjokes` collection
1. When accessed at URL <https://username.herokuapp.com/api/v1/jokes/id> (where _id_ is an integer), your service must return the _specified_ joke from the `pyjokes` collection, even if _id_ is greater than the number of jokes in the collection.
1. Return valid JSON for all requests.
1. The application must not crash. Note that _404 Not Found_ is a valid response, not a crash.

## Client side

1. Deploy on <http://knuth.luther.edu/>.
1. A combination of HTML and JavaScript.
1. The interface should be able to differentiate between requests for random and specific jokes.
1. On button click the request is sent to the server and the response is processed.
1. Use Bootstrap or another CSS framework for consistent styling.

## Grading

| Criterion                      | Points |
| ------------------------------ | ------ |
| Server is deployed             | 10     |
| Server returns JSON            | 10     |
| Server returns 404             | 10     |
| Server returns a random joke   | 10     |
| Server returns a specific joke | 10     |
| Client is deployed             | 10     |
| Client retrieves JSON          | 20     |
| Input form works               | 20     |
| Total                          | 100    |

## References

- [API Design Guide — API Design Guide 0.1 documentation](https://apiguide.readthedocs.io/en/latest/)
- [Flask-CORS — Flask-Cors 3.0.7 documentation](https://flask-cors.readthedocs.io/en/latest/)
- [Using Fetch - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
