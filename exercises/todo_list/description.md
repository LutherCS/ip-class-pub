# Task manager

Develop a task management application (TODO list) using HTML, CSS, and JavaScript.
Use of Bulma is highly recommended since the provided test suite relies on Bulma classes (*help*, *is-danger*) but similar functionality can be achieved using another framework or custom CSS.

## Functionality

Each *task* must include the following properties:

- Title
- Worker (assigned to)
- Priority (Low, Normal, Important, Critical)
- Due date

Once user input is collected, add a new task as a table row with the task priority defining the row color (via CSS class).
The list of team members and priorities are provided and must be used to populate the *Assigned to* and *Priority* `select` elements.

| Element     | Type     | Comment                                    |
|-------------|----------|--------------------------------------------|
| Title       | text     | required                                   |
| Assigned to | select   | pre-populated in JS                        |
| Priority    | select   | pre-populated, determines color of a row   |
| Due date    | date     | required                                   |
| Add task    | button   | validates the form and adds a new row      |
| Clear all   | button   | removes all rows from the table            |
| Completed   | checkbox | removes a row from the table after timeout |

## Hints and ideas

1. Validate user input to ensure valid values are entered.
2. Use *help* `class` to bring user's attention to the missing value(s).
3. Use custom *site.css* to highlight tasks based on priority.
4. HTML elements have been stripped of classes but you can add them back. Don't change the `id`.

## Demonstration

![Demo](demo.webm)

## References

- [Form data validation - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation)
- [javascript - Remove current row (tr) when checkbox is checked - Stack Overflow](https://stackoverflow.com/questions/26512386/remove-current-row-tr-when-checkbox-is-checked)
- [How to use JavaScript closures with confidence – Hacker Noon](https://hackernoon.com/how-to-use-javascript-closures-with-confidence-85cd1f841a6b)
- [javascript - querySelector to select closest ancestor without jQuery - Stack Overflow](https://stackoverflow.com/questions/50085510/queryselector-to-select-closest-ancestor-without-jquery)
