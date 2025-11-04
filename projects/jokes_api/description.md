# Build and Deploy an API

This application consists of two components, the server and the client.
The server is a Flask application that uses the `pyjokes` package to retrieve and return various jokes.
The client provides a way for humans to interact with the server using HTML control elements and JavaScript events.

## Server

## Application structure

The application must be implemented using a *factory* and a *blueprint*, with models, logic, and routes defined in separate files.
App configuration is specified in the *config.toml*.
App initialization should include the following steps:

1. Create a Flask app
2. Make sure the app can handle CORS requests
3. Read the app configuration
4. Initialize the dataset
5. Register routes

Run the application locally as follows:

```bash
cd server
flask --app joker run
```

## Models

Defined in the *models.py*.

Class *Joke* has the following members: `language`, `category`, and `text`.
Hint: Given the simplicity of this class, consider making it a `dataclass`.

## Logic

Defined in the *logic.py*.

Class `Joker` has the following `class` methods: `init_dataset`, `get_jokes`, and `get_the_joke`.
The dataset is a list of objects of class `Joke` that includes all jokes from the `pyjokes` package in the languages specified in the *config.toml*.

Jokes must be added to the common collection in the alphabetical order of their language **codes** (e.g. *es* before *eu* and not *Basque* before *Spanish*) as specified in the configuration file.
Neutral jokes in must be added before Chuck Norris jokes.

Method `get_jokes` takes the language, the category, and the number of jokes to return (0 to return all) as arguments and returns a random sample of jokes of the specified size.
The app raises a `ValueError` if the language is not in the list of configured languages or *any*.
The app raises a `ValueError` if the category is not in the list of valid categories (*any*, *neutral*, or *chuck*).

Method `get_the_joke` takes the joke id as an argument and returns a specific joke from the dataset.
The app raises a `ValueError` if the joke id is not in the range of valid values (0--952).

Hint: you should use `@cache` to improve the app performance, even if it conflicts with the randomization of the results.

## Routes

Defined in the *routes.py*.

The server returns the correct number of jokes in the specified language and category, or returns a `404 Not Found` error if the requested language or category does not exist.
Note that either language or category could be *any*.
The server returns all jokes in the specified language/category if the number of requested jokes is equal to *all*.

The server returns all the available jokes if the number of jokes requested is greater than the number of available jokes.
The server returns an empty list if the language/category exist but there are no jokes in that combination.

The server returns the specific joke if its `id` is provided or aborts with a `404 Not Found` error if the provided `id` is outside the range of available jokes.

Hint: the routes must rely on the logic of the application and catch errors instead of duplication that functionality and checking all the values.

The application must not crash.
Note that `404 Not Found` is a valid response, not a crash.
The server returns JSON only.
The server returns jokes as a list (even if it is an empty list) when language and category are specified but as a single `Joke` when the joke is requested by its `id`.
Errors are returned as strings.

The server is deployed on [PythonAnywhere](https://www.pythonanywhere.com/), [Render](https://render.com/), or similar platform.

See examples of successful requests and those resulting in an error below.

```bash
$ curl http://localhost:5000/api/v1/jokes/eu/any/all
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
$ curl http://localhost:5000/api/v1/jokes/zxx/any
{
"error": "404 Not Found: Language zxx does not exist."
}
```

```bash
$ curl http://localhost:5000/api/v1/jokes/eu/computer
{
"error": "404 Not Found: Category computer does not exist."
}
```

```bash
$ curl http://localhost:5000/api/v1/jokes/any/any/5
{
"jokes": [
    "El teclado de Chuck Norris no tiene tecla F1, es el ordenador el que le pide ayuda a él.",
    "Chuck Norris hat versucht Gewicht zu verlieren. Jedoch verliert Chuck niemals.",
    "You can't follow Chuck Norris on Twitter, because he follows you.",
    "Dlaczego Microsoft nazwał swoją wyszukiwarkę BING? Bo Indolentnie Naśladuje Google.",
    "Learning JavaScript is like looking both ways before you cross the street, and then getting hit by an airplane."
]
}
```

```bash
$ curl http://localhost:5000/api/v1/jokes/eu/any/2
{
"jokes": [
    "Matematika liburu batek bere buruaz beste egin zuen... zergatik? Problema asko zituelako.",
    "Aita, aita, aita!!! Utziko al didazu telebista ikusten? Bai! Baina pizten ez!"
]
}
```

```bash
$ curl http://localhost:5000/api/v1/jokes/any/any/1
{"jokes": ["Chuck Norris finished World of Warcraft."]}
```

```bash
$ curl http://localhost:5000/api/v1/jokes/en/computer/1
{"error": "404 Not Found: Category computer does not exist."}
```

```bash
$ curl http://localhost:5000/api/v1/jokes/330
{
"joke": ["A friend is in a band called 1023Mb. They haven't had a gig yet."]
}
```

```bash
$ curl http://localhost:5000/api/v1/jokes/3300
{
"error": "404 Not Found: Joke 3300 not found, try an id between 0 and 952"
}
```

## Client

### Application structure

The user-facing application is implemented using HTML, CSS, and JavaScript.
HTML includes four control elements: language selector, category selector, number selector, and the Joke id input.

The selection of languages matches the on the server plus *any* (default).
The selection of categories matches the on the server plus *any* (default).
The selection of numbers is limited up to 10 jokes plus *all* (default).
If joke ID is specified, all other input fields are ignored.

Bulma or another CSS framework is used for consistent styling.

JavaScript is used to retrieve data from server, display the results, and handle errors gracefully.

The client is deployed on [GitHub Pages](https://pages.github.com/) or similar platform.

Run the application locally as follows:

```bash
cd client
python -m http.server
```

## Grading

| Criterion                                                                    | Points  |
|------------------------------------------------------------------------------|---------|
| Server returns all jokes in the specified language/category                  | 10      |
| Server returns a specific number of jokes in the specified language/category | 10      |
| Server returns a specific joke by id                                         | 10      |
| Server returns 404 if there are no jokes in the specified language/category  | 10      |
| Server is deployed                                                           | 10      |
| Client allows language, category, and number selection                       | 10      |
| Client allows specifying joke id                                             | 10      |
| Client retrieves JSON and handles errors                                     | 10      |
| Client has consistent style                                                  | 10      |
| Client is deployed                                                           | 10      |
| **Total**                                                                    | **100** |

Unit tests are provided to verify the functionality of various components of the application.
It's recommended that you test your implementation in the following order:

1. Models
2. Logic
3. Routes
4. Client
5. App

## Demonstration

![Demo](demo.mp4)

## References

- [Best practices for REST API design - Stack Overflow Blog](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
- [RESTful API Design — Step By Step Guide | Hacker Noon](https://hackernoon.com/restful-api-design-step-by-step-guide-2f2c9f9fcdbf)
- [REST API Naming Conventions and Best Practices](https://restfulapi.net/resource-naming/)
- [API Design Guide — API Design Guide 0.1 documentation](https://apiguide.readthedocs.io/en/latest/)
- [Flask-CORS — Flask-Cors 3.0.7 documentation](https://flask-cors.readthedocs.io/en/latest/)
- [Using Fetch - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
