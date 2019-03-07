# Shopping List

Implement the following Shopping List functionality using HTML, CSS, and JavaScript. You may modify the provided files as long as your application meets the criteria. You must not change the directory structure and should be able to access your list by visiting `http://localhost:8000/static/`.

# Design

![Shopping List Storage](shopping_list.png)

Buttons *Add*, *Save list*, *Remove purchased*, and *Remove all* must perform the following tasks:

* *Add* collects values from the input fields and create a new row in the table with those values.
* *Save list* saves current state of the list using *local storage*. The list should be regenerated upon page refresh.
* *Remove purchased* removes **purchased** items from the list.
* *Remove all* clears the list completely.

## Implementation

* Use model-view-controller approach
* Use local storage
* Use Bootstrap

## Grading criteria

1. Use Model-View-Controller pattern
1. On page load, retrieve the shopping list from local storage, if possible
1. Save the shopping list to local storage on button click
1. Remove all items marked as **purchased** from the shopping list on button click
1. Remove **all** items from the shopping list on button click
1. Add a new item to the shopping list on button click
1. Validate input fields and do not accept empty values
1. Use checkbox to mark an item as purchased
1. Row color is determined by item priority
1. Consistent design using Bootstrap
