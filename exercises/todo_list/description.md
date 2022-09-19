# List design

Implement the following TODO List functionality using HTML, CSS, and JavaScript. Use of Bootstrap (from CDN) is required.

## Design

![TODO List](todo_list_demo.gif)

## Functionality

| Element     | Type     | Comment                                  |
| ----------- | -------- | ---------------------------------------- |
| Title       | text     | required                                 |
| Assigned to | select   | pre-populated in JS                      |
| Priority    | select   | pre-populated, determines color of a row |
| Due date    | date     | required                                 |
| Add task    | button   | validates the form and adds a new row    |
| Checkbox    | checkbox | removes a row from the table             |

You can hard-code the list of team members and priorities to populate the *Assigned to* and *Priority* drop-down menus respectively.

## Hints and ideas

1. Validate user input using Bootstrap to ensure valid values are entered
2. Use custom `style.css` to highlight tasks based on priority
3. HTML elements have been stripped of classes but you can add them back. Don't change the *id*.
4. Look at the *GPA Calculator* for the ways to populate `select` elements.

## References

- [Validation · Bootstrap v5.0](https://getbootstrap.com/docs/5.0/forms/validation/)
- [Bootstrap form validation - examples & tutorial. Basic & advanced usage - Material Design for Bootstrap](https://mdbootstrap.com/docs/jquery/forms/validation/)
- [Form data validation - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation)
- [javascript - Remove current row (tr) when checkbox is checked - Stack Overflow](https://stackoverflow.com/questions/26512386/remove-current-row-tr-when-checkbox-is-checked)
- [How to use JavaScript closures with confidence – Hacker Noon](https://hackernoon.com/how-to-use-javascript-closures-with-confidence-85cd1f841a6b)
- [javascript - querySelector to select closest ancestor without jQuery - Stack Overflow](https://stackoverflow.com/questions/50085510/queryselector-to-select-closest-ancestor-without-jquery)
- [jQuery](https://jquery.com/)
