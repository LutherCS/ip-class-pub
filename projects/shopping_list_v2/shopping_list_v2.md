# Shopping List: Storage

Implement the following Shopping List functionality using HTML, CSS, and JavaScript. Use of Bootstrap is encouraged.

# Design

![Shopping List Storage](shopping_list_v2.png)

Buttons *Add*, *Save list*, *Remove purchased*, and *Remove all* must perform the following tasks:

* *Add* collects values from the input fields and create a new row in the table with those values.

* *Save list* saves current state of the list using *local storage*. The list should be regenerated upon page refresh.

* *Remove purchased* removes purchased items from the list.

* *Remove all* clears the list completely.

## Implementation

* Use **Model-View-Controller** pattern

* Use **Publish-subscribe** pattern to connect model and view

* Use **local storage** to store the shopping list as JSON
