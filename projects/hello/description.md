# Hello, World

Create a single page with a greeting and your background information.

## Requirements

- Page `title`
  - Hello, CS330
- Page `body` structure
  - `header` and `main`
- Page `header` must contain an `h1` heading with the following properties:
  - `id`: "greeting"
  - text: "Greetings!"
- Page `main` part must contain 3 (three) paragraphs (`p`)
- First paragraph `class`
  - paragraph
- First paragraph text
  - I'm a student in **CS330**.
  - Notice **bold** text.
- Second paragraph `class`
  - paragraph
- Second paragraph text
  - I've taken *CS130*, *CS140*, and *CS160* already.
  - Notice *emphasized* text.
- Third paragraph `id`
  - bye
- Third paragraph `style`
  - `color` set to `rgb(0, 255, 255)`
- Third paragraph text
  - Bye!

## Testing

```bash
python3 -m pytest tests/hello/test_hello.py
```

## Demonstration

![Notes](hello.png)

## References

- [Fast and reliable end-to-end testing for modern web apps | Playwright Python](https://playwright.dev/python/)