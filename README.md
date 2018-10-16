Driftrock Developer Test
========================

This is intended to run on Python 3, enter ``` make ``` in the console from the root folder to install the requirements (requires pip and python 3 to be installed)





## Tests


To run all tests, use  ```  >> make all_tests ```

Barebones unit tests ```  >> make unit_tests```

Barebones integrarion test ```  >> make integration_tests```

## Possbile Improvements
- Test coverage, alot of methods are untested, and the existing ones are limited. More edge cases could be explored, and also integration tests with a Mock External API could be added.
- Custom exception handling for http requests.
- A generic base class for creating API handlers, this could be used for other APIS.
