Driftrock Developer Test
========================

This is intended to run on Python 3, enter ``` make ``` in the console from the root folder to install the requirements (requires pip and python 3 to be installed)


## Usage
Returns the most sold item e.g:
``` >> python3 app.py most_sold ```
``` >> Heavy Duty Concrete Watch ```


Returns the total spend for a user (specified via email) e.g:
``` >> python3 app.py total_spend drift.rock@email.com ```
``` >> 22.98 ```

Returns the most loyal customer e.g:
``` >> python3 app.py most_loyal ```
``` >> drift.rock@email.com ```


## Tests

To run all tests, use  ```  >> make all_tests ```

Barebones unit tests ```  >> make unit_tests```

Barebones integrarion test ```  >> make integration_tests```

## Improvements
- Design pattern usage. e.g Strategy pattern to be used in the src/app.py to replace if-else logic. 
- More Encapsulation. e.g purchases calculations should be behaviour of the purchase class, this would take some redesign and refactoring.
- Lambdas - Alot of the calculations involve iterating over a collection. These operations could be more concise by using lambda functions.
- Test coverage, alot of methods are untested, and the existing ones are limited. More edge cases could be explored, and also integration tests with a Mock External API could be added.
- Custom exception handling for http requests.
- A generic base class for creating API handlers, this could be used for other APIs.
