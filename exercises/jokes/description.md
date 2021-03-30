# Using Flask for Fun

## Description

Use Flask and [pyjokes](https://github.com/pyjokes/pyjokes) to build a web application that would allow users to select language and category of a joke and use Jinja2 to print the specified number of jokes from the selected category.

```python
>>> import pyjokes
>>> pyjokes.get_joke()
>>> pyjokes.get_jokes()
>>> pyjokes.get_jokes(language="de", category="neutral")
```

## Requirements

1. Use some HTML/CSS framework to style the app
2. Allow users to select the joke language (_en_, _es_, or _de_)
3. Allow users to select the joke category (_all_, _neutral_, or _Chuck Norris_)
4. Allow users to select the number of jokes (e.g. 1, 5, 10)
5. Populate `select` elements using Jinja2 templates
   1. Do not use JavaScript in this exercise
6. Call `pyjokes.get_joke()` with the specified category and language to retrieve a _random_ joke or `pyjokes.get_jokes()` to retrieve multiple jokes at once
7. Handle the error (no jokes about Chuck Norris in Spanish) gracefully

## Testing

Use the provided tests (_tests/jokes_) to verify the correctness of implementation.

```bash
python3 -m pytest -v tests/jokes/test_jokes_back.py
python3 -m pytest -v tests/jokes/test_jokes_front.py
```

## Demo

I used [MUI](https://www.muicss.com/) but you may continue using [Bootstrap](https://getbootstrap.com/).

![Demo](jokes.gif)
