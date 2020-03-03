# Storing Stuff

Implement the following List functionality using HTML, CSS, and JavaScript. Use Bootstrap for styling of the elements. The example is of the *shopping list* but you should choose your own theme.

## Design

![List Example](example.png)

Buttons *Add*, *Save*, *Remove*, and *Clear* must perform the following tasks:

* *Add*: collect values from the input fields and create a new row in the table with those values.
* *Save*: save current state of the list using *local storage*.
* *Remove*: remove checked items from the list.
* *Clear*: remove all items from the list.

## Implementation

* Use model-view-controller approach.
* Use local storage to store and retrieve data.
* Regenerate the list upon page refresh.

## Grading criteria

1. Use Model-View-Controller pattern
2. Load the list from local storage, if present
3. Add new item to the shopping list on button click
4. Save the list to local storage on button click
5. Remove all **checked** items from the shopping list on button click
6. Remove **all** items from the list on button click
7. Validate input fields. Do not accept empty values
8. Use checkbox and an item title to mark an item as checked
9. Consistent design using Bootstrap
10. Code is error-free
