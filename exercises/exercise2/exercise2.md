# JavaScript and OOP

Create a new directory **exercise2**.

Create the following JavaScript files and put them in the directory **js** of **exercise2**.

## model.js

This file must contain 2 classes, *Item* and *ShoppingList*.

### Item

Class *Item* must have a constructor that takes 6 parameters:

* name
* quantity
* price
* store
* section
* priority

The constructor of class *Item* must set property *_purchased* to **false**. Class *Item* must have a getter and a setter for the property *_purchased*.

### ShoppingList

Class *shoppingList* must have a constructor and three methods: *addItem*, *cleanList*, and *emptyList*.

Constructor takes no arguments and creates a new empty list, *items*.

*cleanList* takes no arguments and removes all purchased items from the list. Hint: use function `splice`.

*emptyList* sets *items* to an empty list.

## view.js

Create a class *ShoppingView* with a constructor and two methods, *redrawList* and *addRow*. Leave those empty for now, we'll get back to them later.

## controller.js

Tis file must contain functionality to interact with your HTML. You should be ready to use code from the **Shopping List** project here but it's OK to leave it blank for now.