Functions
=========

Sources
-------

This lesson is partly based on the `Software Carpentry group's <http://software-carpentry.org/>`__ lessons on `Programming with Python <http://swcarpentry.github.io/python-novice-inflammation/>`__.

What is a function?
-------------------

A function is a block of organized, reusable code that can make your code more effective, clearer to read and easier to handle.
You can think functions as little self-contained programs that can perform a specific task which you can use repeatedly in your code.
One of the basic principles in good programming is "not to repeat yourself", i.e. you shouldn't have duplicate lines of code in your script.
Functions are a way to avoid such situations and they can save you a lot of time and effort as you don't need to retell the computer what to do every time it does a common task, such as converting temperatures from Fahrenheit to Celsius.

Anatomy of a function
----------------------

Let's consider again the task of converting temperatures from Fahrenheit to Celsius.
Such an operation is a fairly common task when dealing with temperature data.

1. Let's define our first function called ``celsius_to_fahr``:

   .. code:: python

       >>> def celsius_to_fahr(temp):
       ...    return 9/5 * temp + 32

   The function definition opens with the keyword ``def`` followed by the name of the function and a list of parameter names in parentheses.
   The body of the function — the statements that are executed when it runs — is indented below the definition line.

   When we call the function, the values we pass to it are assigned to the corresponding parameter variables so that we can use them inside the function (e.g., the variable ``temp`` in this function example).
   Inside the function, we use a return statement to define the value that should be given when the function is used.

Calling functions
-----------------

2. Let’s try running our function.
   Calling our self-defined function is no different from calling any other function such as ``print()``.
   You need to call it with its name and send your value to the required parameter(s) inside the parentheses:

   .. code:: python

       >>> freezing_point =  celsius_to_fahr(0)
       >>> print('Freezing point of water in Fahrenheit:', freezing_point)
       Freezing point of water in Fahrenheit: 32.0
       >>> print('Boiling point of water in Fahrenheit:', celsius_to_fahr(100))
       Boiling point of water in Fahrenheit: 212.0

3. Now that we know how to create a function to convert Celsius to Fahrenheit, let's create another function called
   ``kelvin_to_celsius``:

   .. code:: python

       >>> def kelvin_to_celsius(temp_k):
       ...    return temp_k - 273.15

4. And let's use it in a similar way as the earlier one:

   .. code:: python

       >>> absolute_zero = kelvin_to_celsius(temp_k=0)
       >>> print('Absolute zero in Celsius:', absolute_zero)
       Absolute zero in Celsius: -273.15

5. What about converting Kelvins to Fahrenheit?
   We could write out an own formula for it, but we don’t need to.
   Instead, we can compose it by using the two functions we have already created and calling those from the function we are now creating:

   .. code:: python

       >>> def kelvin_to_fahr(temp_k):
       ...    # Kelvin in celsius
       ...    temp_c = kelvin_to_celsius(temp_k)
       ...    # Celsius in Fahrenheit
       ...    temp_f = celsius_to_fahr(temp_c)
       ...    # Return the result
       ...    return temp_f

6. Let's use the function:

   .. code:: python

       >>> absolute_zero_f = kelvin_to_fahr(temp_k=0)
       >>> print('Absolute zero in Fahrenheit:', absolute_zero_f)
       Absolute zero in Fahrenheit: -459.66999999999996
