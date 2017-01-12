``for`` loops
=============

Sources
-------

This lesson is based on the `Software Carpentry group's <http://software-carpentry.org/>`__ lessons on `Programming with Python <http://swcarpentry.github.io/python-novice-inflammation/>`__.

Basics of ``for`` loops
-----------------------

1. Loops allow parts of code to be repeated over some number of times.
   One of the simple loop options in Python is the ``for`` loop.

   .. code:: python

       >>> word = 'rock'
       >>> for char in word:
       ...    print(char)
       ...
       r
       o
       c
       k

2. ``for`` loops in Python have the general form below.

   .. code:: python

       for variable in collection:
           do things with variable

   The ``variable`` can be any name you like, and the statement of the ``for`` loop must end with a ``:``.
   The code that should be executed as part of the loop must be indented beneath the ``for`` loop, and the typical indentation is 4 spaces.
   There is not additional special word needed to end the loop, just change the indentation back to normal.

3. Let's consider another example.

   .. code:: python

       >>> length = 0
       >>> for letter in 'earthquake':
       ...    length = length + 1
       ...
       >>> print('There are', length, 'letters')
       There are 10 letters

   Note that the variable used in the loop, ``letter`` is just a normal variable and still exists after the loop has completed with the final value given to letter.
   
   .. code:: python

       >>> print('After the loop, letter is', letter)
       e

4. A loop can be used to iterate over any list of values in Python.
   So far we have considered only character strings, but we could also write a loop that performs a calculation a specified number of times.

   .. code:: python

       >>> for number in range(5):
       ...     print(number)
       ...
       0
       1
       2
       3
       4

   What happens here?
   Well, in this case, we use a special function called ``range()`` to give us a list of 5 numbers ``[0, 1, 2, 3, 4]`` and then print each number in the list to the screen.
   When given an integer (whole number) as an argument, ``range()`` will produce a list of numbers with a length equal to the specified number.
   The list starts at zero and ends with number-1.

5. Often when you use ``for`` loops, you are looping over the values in
   a list and either calculating a new value or modifying the existing
   values. Let's consider an example.

   .. code:: python

       >>> mylist = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
       >>> print(mylist)
       [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
       >>> for i in range(6):
       ...     mylist[i] = mylist[i] + i
       ...
       >>> print(mylist)
       [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]

   So, what happened?
   We first create a list of 6 numbers.
   Then, we loop over 6 values using the ``range()`` function and add each value to the existing location in ``mylist``.

6. One of the drawbacks in the example above is that we need to know the length of the list before running that ``for`` loop example.
   However, we already know how to find the length of a list using the ``len()`` function, and we can take advantage of this knowledge to make our ``for`` loop more flexible.

   .. code:: python

       >>> for i in range(len(mylist)):
       ...     mylist[i] = mylist[i] + i
       ...
       >>> print(mylist)
       [0.0, 3.0, 6.0, 9.0, 12.0, 15.0]

   Using the ``len()`` function with ``range()`` to perform calcluations
   using list or array values is an *extremely* common operation in
   Python.

.. topic:: Exercise - Putting it together

   - Create a new NumPy array called ``numbers`` that starts at 1 and goes to 100 in increments of 1
   - Create a new NumPy array of zeros called ``squared`` that is the same size as ``numbers``
   - Using a ``for`` loop, calculate the square of each value in ``numbers`` and store it in the corresponding location in ``squared``
   
.. topic:: Exercise - Let's get functional

   - Take your code above and use it to create a new Python function ``square()`` that accepts a NumPy array and returns an array of squared values
   - Do you get the expected results when using your function?
   - Can you break your function (get it to give an error message)? If so, how?

.. topic:: Exercise - Drag race

   IPython has a magic function called ``%timeit`` that you can use to calculate how long it takes a line of code (or program) to execute.

   .. code:: python

       >>> %timeit np.ones(100000000).mean()
       loop, best of 3: 427 ms per loop

   We can use this now to compare the performance of your new ``square()`` function with calculating the square of values directly in NumPy

   - Create a new NumPy array called ``input`` that goes from 1 to 10 in increments of 0.0000001
   - Use ``%timeit`` with your function above to calculate the square of ``input``, storing the output in an array called ``out1``
   - Compare the performance of your function to simply squaring the ``input`` array directly and storing its output as ``out2``
   - Can you see any benefits to using NumPy?
