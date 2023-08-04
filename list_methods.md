# List Methods

* `append()` - add an element to the end of a list.
* `insert()` - use index, object to place a new value in an existing list at a specific location (index)
* `extend()` - takes a list [] for an argument and extends the existing list by appending.
* `pop()` - remove the last entry and return the value. If given a an index, removes the entry at that index.
* `remove()` - removes the value given as an argument.
* `clear()` - removes all entries from a list.
* `index()` - get index of a value in a list. Can also provide index bounds for the search.
* `(value in list)` - search for value in the specific list.
* `count()` - returns number of times a value occurs in the list.
* `sort()` - sorts list in place.
  * `sortec(list)` - returns a sorted copy - does not modify original.
* `list[:]` or `copy()` - return a copy of tha list.
* `reverse()` - reverses list values in place.

## Common List Patterns

* Reverse by slice `my_list[::-1]` - creates a reversed copy of the original list.
* `my_list(list(range(100)))` - Create a list of sequential values  from a range
* `' '.join(["new", "Sentence"])` create a string from a list.
* List unpacking:
```python
a, b, c, *other, d = [1, 2 ,3, 4, 5, 6]
```
