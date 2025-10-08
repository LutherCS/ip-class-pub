# JavaScript Promises

Develop an application that interacts with [Open Trivia DB](https://opentdb.com/) and retrieves the specified number of questions in the chosen category.

## Task

1. Create a page with a `select` element (with `id` *categorySelect*), a `number` input (with `id` *numberInput*), and a `button` (with `id` *getQuestionsBtn*). When the button is clicked, read the category and the number, send a request to [Open Trivia DB: Free to use, user-contributed trivia question database.](https://opentdb.com/), and generate page content based on the data received.
   1. Users must be able to pick one of 4 categories: *Science: Computers*, *Mythology*, *Geography*, and *History*.
   2. Users must be able to specify the number of questions between 1 and 10 (inclusive). A missing number should prompt a help message (`class` *is-warning*) to appear below the input.
   3. Users won't be able to specify difficulty, type, or encoding of the questions. You should fetch multiple-choice questions of any difficulty using the default encoding settings.
2. The results must be added as [Bulma cards](https://bulma.io/documentation/components/card/) to the existing `div` (with `id` *questionsDiv*) as follows:
   1. Question itself is the card `title`.
   2. Candidate answers are the card `content` (ordered list).
   3. Question *category*, *difficulty*, and a button revealing the correct answer as parts of the card `footer`.
   4. Question *difficulty* must determine the color of the card using CSS class (*easy*, *medium*, or *hard*).
3. Clicking the **reveal** button must highlight the correct answer to the specific question by setting its CSS class to *correct_answer*.
4. Use JavaScript promises to send requests and parse the JSON response to generate HTML content.
5. Use Bulma to style your application.

## Testing

```bash
python -m pytest -v tests/trivia/test_trivia.py
```

## References

- [JavaScript Promises: an Introduction  |  Web Fundamentals  |  Google Developers](https://developers.google.com/web/fundamentals/primers/promises)
- [Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Using Fetch - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Promise](https://javascript.info/promise-basics)
- [Master the JavaScript Interview: What is a Promise?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-promise-27fc71e77261)
- [Understanding promises in JavaScript – Hacker Noon](https://hackernoon.com/understanding-promises-in-javascript-13d99df067c1)
- [asynchronous - How to wait for a JavaScript Promise to resolve before resuming function? - Stack Overflow](https://stackoverflow.com/questions/28921127/how-to-wait-for-a-javascript-promise-to-resolve-before-resuming-function)
- [Open Trivia DB: Free to use, user-contributed trivia question database.](https://opentdb.com/api_config.php)
