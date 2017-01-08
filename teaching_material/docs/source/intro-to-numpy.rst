Introduction to NumPy
=====================

Introducing NumPy
-----------------

NumPy is a library for Python designed for efficient scientific (numerical) computing.
It is an essential library in Python that is used under the hood in many other modules.
Here, we willl get a sense of a few things NumPy can do.

1. To start using the NumPy library we will need to ``import`` it.

   .. code:: python

       >>> import numpy as np

   The ``import library as`` syntax can be used to give the library a different name in memory.
   Since we may want to use NumPy many time, shortening ``numpy`` to ``np`` is helpful.

2. A common NumPy task is to create your own arrays to make a variable that has a range from one value to another.
   If we wanted to calculate the ``sin()`` of a variable ``x`` at 10 points from zero to 2 \* pi, we could do the following.

   .. code:: python

       >>> x = np.linspace(0., 2 * np.pi, 10)
       >>> print(x)
       [ 0.          0.6981317   1.3962634   2.0943951   2.7925268   3.4906585     4.1887902   4.88692191  5.58505361  6.28318531]   >>> y = np.sin(x)   >>> print(y)   [  0.00000000e+00   6.42787610e-01   9.84807753e-01   8.66025404e-01      3.42020143e-01  -3.42020143e-01  -8.66025404e-01  -9.84807753e-01     -6.42787610e-01  -2.44929360e-16]

   In this case, ``x`` starts at zero and goes to 2 \* pi in 10 increments.
   Alternatively, if we wanted to specify the size of the increments for a
   new variable ``x2``, we could use the ``np.arange()`` function.

   .. code:: python

       >>> x2 = np.arange(0.0, 2 * np.pi, 0.5)
       >>> print(x2)
       [ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6. ]

   In this case, ``x2`` starts at zero and goes to the largest value that is smaller than 2 \* pi by increments of 0.5.
   Both of these types of array options are useful in different situations.

3. As before, we can check out the type of data in our arrays ``x`` and ``x2`` using the ``type()`` function or the ``%whos`` magic command in IPython.

   .. code:: python

       >>> type(x)
       numpy.ndarray

   OK, so we have something new here.
   NumPy has its own data types that are part of the module.
   In this case, our data is stored in an NumPy *n*-dimensional array.

4. How much data do we have in our ``x`` variable?

   .. code:: python

       >>> print(x.shape)
       (10,)

   10 rows of data, 1 column. In this case the single column value is suppressed.
   ``shape`` is a *member* or *attribute* of ``x``, and is part of any NumPy ``ndarray``.
   Printing ``x.shape`` tells us the size of the array.

5. We can also check the data type of our data columns by using ``x.dtype``

   .. code:: python

       >>> print(x.dtype)
       float64

   OK, so it seems that all the data in our file is float data type, i.e., decimal numbers (stored with a precision of 64 bytes).

6. Like lists, we can find any value in an array by using it's *indices*.
   We can also extract parts of an array using *index slicing*.
   Perhaps we only want the first three values out of array ``x``.

   .. code:: python

       >>> x[0:3]
       array([ 0.       ,  0.6981317,  1.3962634])

   Nice! Note that in this case, the range of index values for the first 3 rows is 0-3.
   The data extracted will start at ``0`` and go up to, but not include ``3``.

Useful functions 
-----------------

7. Like normal variables, array variables can also be used for various mathematical operations.

   .. code:: python

       >>> doublex = x * 2.0
       >>> print(doublex)
       [  0.           1.3962634    2.7925268    4.1887902    5.58505361      6.98131701   8.37758041   9.77384381  11.17010721  12.56637061]

8. In addition to the *attributes* we saw prevously for NumPy ``ndarray`` variables, there are also many *methods* that are part of the ``ndarray`` data type.

   .. code:: python

       >>> print(x.mean())
       3.14159265359
       >>> print(doublex.mean())
       6.28318530718

   No surprises here. If we think of *variables* as nouns, *methods* are verbs, actions for the variable values.
   **NOTE**: When using methods, you always include the parentheses ``()`` to be clear we are referring to a *method* and not an *attribute*.
   There are many other useful ``ndarray`` methods, such as ``x.min()``, ``x.max()``, and ``x.std()`` (standard deviation).

9. *Methods* can also act on part of an array.

   .. code:: python

       >>> print(x[0:5].mean())
       1.3962634016
