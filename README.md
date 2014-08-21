flask-test-kata
===============

This is a python testing kata for a simple Flask web "service".

This project has the following skeleton:

    flask-test-kata
    ├── calculator
    │   ├── __init__.py
    │   ├── app.py
    │   ├── logic.py
    │   └── templates
    │       └── index.html
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    └── tests
        ├── __init__.py
        ├── base.py
        ├── integration
        |   ├── __init__.py
        |   └── test_views.py
        └── unit
            ├── __init__.py
            └── test_logic.py

The tasks at hand:

Unit Tests
----------

1. Implement `test_mul` unit test for the multiply method in `logic.Calculator`,
   then flesh out `logic.Calculator.mul` until test passes.

2. `test_mul` as a test is rather coarse. A better test would be in the form
   `test_function_satisfies_condition_after_pre-condition`. Implement the tests
   `test_mul_with_two_positive_numbers`, `test_mul_with_two_negative_numbers`,
   `test_mul_with_one_negative_one_positive_number`.

3. The constructor of `logic.Calculator` takes two arguments `min_value` and
   `max_value`. Change the class so that it's methods throw the exceptions
   in `logic.py` when confronted with numbers that are too high or too low.

4. `logic.Calculator` contains another method stub: `div`. This method should
   divide `a` by `b`, but it is just a stub now. Write corresponding tests for
   the method, as you've written for `logic.Calculator.mul`, then implement
   the method to pass your tests.

5. Division has more caveats than multiplication. ZeroDivisionError ?


The preferred way of testing whether exceptions are raised is to use
```
with pytest.raises(MyException):
    code...
```



Integration Tests
-----------------

1.
