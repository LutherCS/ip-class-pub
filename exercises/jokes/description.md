# Using Flask for Fun

## Description

Use `Flask` and [pyjokes](https://github.com/pyjokes/pyjokes) to build a web application that would allow users to select language and category of a joke and use Jinja to print the specified number of jokes from the selected category.

Do not use JavaScript in this exercise.

```python
>>> import pyjokes
>>> pyjokes.get_joke()
>>> pyjokes.get_jokes()
>>> pyjokes.get_jokes(language="de", category="neutral")
```

## Requirements

1. Consistent and appealing user interface; use of some HTML/CSS framework (e.g. Bulma) is recommended.
   1. The provided *smile.png* is used as an icon.
2. Options of the HTML `select` elements populated using Jinja templates.
3. Jokes language (Basque, Czech, English, French, Galician, German, Hungarian, Italian, Lithuanian, Polish, Spanish, or Swedish) is selectable using the `#selLang` selector.
   1. Language name is shown even if language code is used internally.
4. Jokes category (All, Neutral, or Chuck) is selectable using the `#selCat` selector.
   1. Category name shown to users is capitalized even if the lowercase value is used py `pyjokes`.
5. The number of jokes (1--9) is selectable using the `#selNum` selector.
6. A `POST` request is sent to the Flask app when button `#btnAmuse` is clicked.
   1. The server responds with a "418 I'm a teapot" status code if an empty request is submitted.
7. `pyjokes.get_jokes()` is used to retrieve multiple jokes at once.
   1. If the number is not specified, a single joke is returned.
8. Errors (e.g. there are no jokes about Chuck Norris in some languages) are handled gracefully.
   1. A list of a single item, "No kidding!" is returned if `PyjikesError` exception is raised.
9. Jokes are shown inside the `#jokes` container, each joke as a separate `article`.
10. All events are handled using HTML form and HTTP methods without JavaScript.

## Testing

Use the provided tests (*tests/jokes*) to verify the correctness of implementation.

```bash
python3 -m pytest -v tests/jokes/test_jokes_back.py
python3 -m pytest -v tests/jokes/test_jokes_front.py
```

You can test a specific combination of selected options instead of running the whole suite, which is particularly useful when testing the fron-end of the application.

```bash
python -m pytest -v tests/jokes/test_jokes_front.py -k click_button
python -m pytest -v tests/jokes/test_jokes_front.py -k a_joke
python -m pytest -v tests/jokes/test_jokes_front.py -k n_jokes
python -m pytest -v tests/jokes/test_jokes_front.py -k fewer_jokes
python -m pytest -v tests/jokes/test_jokes_front.py -k chuck_error
```

## Demo

![Demo](jokes.gif)
