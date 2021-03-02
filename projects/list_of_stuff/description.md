# Storing Stuff

Implement the following List functionality using HTML, CSS, and JavaScript. Use Bootstrap or similar framework for styling of the elements. The example is of the _shopping list_ but you should choose your own theme.

**Do not create a shopping list or a task list for this project!**

## Design

![List Example](example.png)

Buttons _Add_, _Save_, _Remove_, and _Clear_ are required and must perform the following tasks:

- _Add_: collect values from the input fields and create a new row in the table with those values.
- _Save_: save current state of the list using _local storage_. If you save the list as part of the _add_ step, this button is _optional_.
- _Remove_ or _Remove purchased_: remove checked items from the list and the local storage. If you remove an item on checkbox click, this button is _optional_.
- _Clear_ or _Remove all_: remove all items from the list and the local storage.

## Implementation

- Use model-view-controller pattern.
- Use JSON and local storage to store and retrieve data.
- Reload the list from local storage upon page refresh.

## Grading criteria

1. Use Model-View-Controller pattern
2. Load the list from local storage, if present
3. Add new item to the list on button click
4. Save the list as JSON to local storage
5. Remove _checked_ items from the list
6. Remove _all_ items from the list on button click
7. Validate input fields. Do not accept empty values
8. Use checkbox to mark an item for removal
9. Consistent design using Bootstrap or similar framework
10. Code is error-free
