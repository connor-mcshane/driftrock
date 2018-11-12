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

## Design Process
1. A class was first developed for retrieving data from the driftrock API (driftrock_api.py). I decided that the class should return a list of Purchase or User instances instead of raw JSON data (so the logic is not dependent on external code formatting).
2. A calculation model was then created, it peforms its calculations on Purchase or User instances.
3. The main file app.py was then created, its role to parse commands from the commandline and choose which methods to call.

## In Retrospect
I tried to avoid spending too much time on the development of this (as the recommendation was that it would take a couple hours of work). In retrospect, I would have changed the following:
- Create PurchaseList class. This class could have functions such as ```most_sold_item(...)```, ```total_spend_for_user(...)``` and ```most_loyal_user(...)```. This would have helped prevent code duplication in the calc_methods module.

- Create a UserList class. This class would have functions such as ```get_user_by_email(...)``` and ```get_email_for_user()```. This also would have helped prevent code.


## Improvements
- Design pattern usage. e.g Strategy pattern to be used in the src/app.py to replace if-else logic. 
- More Encapsulation. e.g purchases calculations should be behaviour of the purchase class, this would take some redesign and refactoring.
- Lambdas - Alot of the calculations involve iterating over a collection. These operations could be more concise by using lambda functions.
- Test coverage, alot of methods are untested, and the existing ones are limited. More edge cases could be explored, and also integration tests with a Mock External API could be added.
