# Using Flask for Fun

## Description

Use `Flask` and [pyjokes](https://github.com/pyjokes/pyjokes) to build a web application that would allow users to select language and category of a joke and use Jinja2 to print the specified number of jokes from the selected category.

Do not use JavaScript in this exercise.

```python
>>> import pyjokes
>>> pyjokes.get_joke()
>>> pyjokes.get_jokes()
>>> pyjokes.get_jokes(language="de", category="neutral")
```

## Requirements

1. Use some HTML/CSS framework (e.g. Bulma) to style the app.
2. Populate `select` options using Jinja2 templates.
3. Allow users to select the joke language (Basque, Czech, English, French, Galician, German, Hungarian, Italian, Lithuanian, Polish, Spanish, or Swedish) using the `#selLang` selector.
4. Allow users to select the joke category (*all*, *neutral*, or *chuck*) using the `#selCat` selector.
5. Allow users to select the number of jokes (1-9) using the `#selNum` selector.
6. When button `#btnAmuse` is clicked a `POST` request must be sent to the Flask app.
7. Call `pyjokes.get_jokes()` to retrieve multiple jokes at once.
   1. If the number is not specified, return a single joke.
8. Handle the error (e.g. there are no jokes about Chuck Norris in some languages) gracefully.
9. Populate the `#jokes` container, making each joke a separate `article`.

## Testing

Use the provided tests (*tests/jokes*) to verify the correctness of implementation.
Note that there are hundreds of unit tests and those testing the fron-end implementation are taking a few minutes to complete, especially if they are failing. It is recommended that you implement and test your back-end first, then implement and test the front-end.

```bash
python3 -m pytest -v tests/jokes/test_jokes_back.py
python3 -m pytest -v tests/jokes/test_jokes_front.py
```

## Demo

![Demo](jokes.gif)
