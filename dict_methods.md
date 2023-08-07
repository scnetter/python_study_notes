# Common Dictionary Methods
* `.get()` - error safe method to access dictionary entries. Can also provide a default as the second parameter.
* `dict(key=value)` - create a new dictionary (don't put key in ''s if a string)
* `<key> in <dict>` - find a key in a dict
* `.keys()`
* `values()`
* `items()` - gets contents of a dict as a list of tuples.
* `clear()` - empties a dict. No return value.
* `copy()` - creates a copy of a dict.
* `pop(key)` - returns value at key and removes it from the dict
* `popitem()` - pops last item on dict (essentially random as it removes "some pair").
* `update()` - Takes a dict struct and updates the entry - if it doesn't exist, it creates it.