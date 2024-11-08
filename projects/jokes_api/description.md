# Build and deploy an API

## Server side

1. Deploy on [PythonAnywhere](https://www.pythonanywhere.com/), [Render](https://render.com/), or another platform of your choice.
2. Your API should return all the jokes in the specified language/category or return a `404 Not Found` error if the requested language or category does not exist. See examples of successfull requests and those resulting in an error below.

    ```bash
    $ curl http://localhost:5000/api/v1/jokes/eu/all
    {
    "jokes": [
        "Zer dira 8 Bocabits? BocaByte bat",
        "Zer esaten dio bit batek besteari? Busean ikusten gara!",
        "Zer da terapeuta bat? - 1024 Gigapeuta",
        "Aita, aita, aita!!! Utziko al didazu telebista ikusten? Bai! Baina pizten ez!",
        "Matematika liburu batek bere buruaz beste egin zuen... zergatik? Problema asko zituelako."
    ]
    }
    ```

    ```bash
    $ curl http://localhost:5000/api/v1/jokes/aa/all
    {
    "error": "404 Not Found: Language aa does not exist."
    }
    ```

    ```bash
    $ curl http://localhost:5000/api/v1/jokes/eu/computer
    {
    "error": "404 Not Found: Category computer does not exist."
    }
    ```

3. Your API should return the exact number of *random* jokes in the specified language/category or return a `404 Not Found` error if the requested language or category does not exist. See examples of successfull requests and those resulting in an error below.

    ```bash
    $ curl http://localhost:5000/api/v1/jokes/eu/all/2
    {
    "jokes": [
        "Matematika liburu batek bere buruaz beste egin zuen... zergatik? Problema asko zituelako.",
        "Aita, aita, aita!!! Utziko al didazu telebista ikusten? Bai! Baina pizten ez!"
    ]
    }
    ```

4. Your API should return the specific joke if its `id` is provided or return a `404 Not Found` error if the provided `id` is outside the range of available jokes.

    ```bash
    $ curl http://localhost:5000/api/v1/jokes/330
    {
    "jokes": "A friend is in a band called 1023Mb. They haven't had a gig yet."
    }
    ```

    ```bash
    $ curl http://localhost:5000/api/v1/jokes/3300
    {
    "error": "404 Not Found: Joke 3300 not found, try an id between 0 and 952"
    }
    ```

5. The application must not crash. Note that `404 Not Found` is a valid response, not a crash.

## Client side

1. Deploy on <http://knuth.luther.edu/>, [GitHub Pages](https://pages.github.com/), or another platform of your choice.
2. User should be able to select different language, category, and number of jokes (including *all*).
3. User should be able to request a specific joke. If joke ID is specified, all other input fields should be ignored.
4. Use JavaScript to retrieve data from your deployed API.
5. Use Bulma or another CSS framework for consistent styling.

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
