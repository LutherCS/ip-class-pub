# Build and deploy an API

## Server side

1. Deploy on [PythonAnywhere](https://www.pythonanywhere.com/), [Heroku](https://www.heroku.com/), or another platform of your choice.
2. Your API must return the exact number of random jokes in the specified language/category. It is up to you how to structure the URL, read the provided references for ideas. The provided examples are mutually exclusive, implement either of them (or something else entirely).
   1. Example 1: when accessed at URL `/api/v1/jokes?category=chuck&language=de&number=10` your service must return 10 Chuck Norris jokes in German from the `pyjokes` collection as a JSON object (array of dictionaries).
   2. Example 2: when accessed at URL `/api/v1/jokes/es/neutral/5` your service must return 5 neutral jokes in Spanish from the `pyjokes` collection as a JSON object (array of dictionaries).
3. Your API must return the specific joke if its `id` is provided. It is up to you how to structure the URL, read the provided references for ideas. The provided examples are mutually exclusive, implement either of them (or something else entirely).
   1. Example 1: when accessed at URL `/api/v1/jokes?category=chuck&language=de&id=33` your service must return the specified (`id` is `33`) Chuck Norris joke in German from the `pyjokes` collection as a JSON object (dictionary).
   1. Example 2: when accessed at URL `/api/v1/jokes/es/neutral/1/5` your service must return the specified (`id` is `5`) neutral joke in Spanish from the `pyjokes` collection as a JSON object (dictionary).
4. Return a valid `404 Not Found` HTTP response if the `id` value is outside of range `0..size` where `size` is a total number of jokes in the collection. Use `len(pyjokes.get_jokes(category=[all,chuck,neutral], language=[en,es,de]))` to find out the number of jokes in each category/language.
5. The application must not crash. Note that `404 Not Found` is a valid response, not a crash.

## Client side

1. Deploy on GitHub pages, Netlify, or another platform of your choice
2. User should be able to select different language, category, and number of jokes
3. User should be able to request a specific joke.
4. Use JavaScript to retrieve data from your deployed API.
5. Use Bootstrap or another CSS framework for consistent styling.

## Grading

| Criterion                                 | Points  |
| ----------------------------------------- | ------- |
| Server is deployed                        | 10      |
| Server returns random joke(s)             | 10      |
| Server returns a specific joke            | 10      |
| Server returns 404                        | 10      |
| Server does not crash                     | 10      |
| Client is deployed                        | 10      |
| Language, category, and number drop-downs | 10      |
| Specific joke id input field              | 10      |
| Client retrieves JSON                     | 10      |
| Style                                     | 10      |
| **Total**                                 | **100** |

## References

- [Best practices for REST API design - Stack Overflow Blog](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
- [RESTful API Design — Step By Step Guide | Hacker Noon](https://hackernoon.com/restful-api-design-step-by-step-guide-2f2c9f9fcdbf)
- [REST API Naming Conventions and Best Practices](https://restfulapi.net/resource-naming/)
- [API Design Guide — API Design Guide 0.1 documentation](https://apiguide.readthedocs.io/en/latest/)
- [Flask-CORS — Flask-Cors 3.0.7 documentation](https://flask-cors.readthedocs.io/en/latest/)
- [Using Fetch - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
