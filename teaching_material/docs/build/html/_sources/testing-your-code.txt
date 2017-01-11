.. testing your code / benchmarking section

Testing your code and benchmarking
==================================

As we have seen yesterday_, it is possible to use the finite difference method to solve equations, and if we use a sufficiently high resolution we can get a very precise solution.
But is it correct?
It can be difficult to know without directly comparing our solutions to known correct values.
This process will be the focus of this lesson.

Sources of error
----------------

We have focussed thus far on using the finite difference method to approximate solutions to equations that we cannot directly integrate.
As we have seen, the definition of a derivative is 

.. math::
   \frac{\mathrm{d}f}{\mathrm{d}x}\rvert_{x=x_0} = \lim_{\Delta x \rightarrow 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} ,
   :label: testing_derivative

which we can approximate in a number of forms by removing the limit :math:`\Delta x \rightarrow 0`.
For example, we have seen that for forward differences we can state

.. math::
   \frac{\mathrm{d}f}{\mathrm{d}x}\rvert_{x=x_0} \approx \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} .
   :label: testing_fd

And again, as long as :math:`\Delta x` is "small enough", the error that is introduced in this approximation is insignificant.
So the question is, how do we know when :math:`\Delta x` is small enough?
Before we can answer that question, we need to say a few things about the sources of error in any computer-based calculation and how we can caluclate these errors.

In computations there are essentially three different sources of error we can consider:

- **Gross error**: A mistake in the program itself, a bug.
- **Truncation error**: Error introduced by approximating the solution to a problem, such as using a finite-difference solution rather than direct integration of an equation.
- **Roundoff error**: Error related to the computers inability to exactly represent floating point numbers.

Although all three of these sources of error can appear in our programs, we mainly will focus on issues related to truncation error in our discussion in the following sections.

Calculating error
-----------------

Now that we have a sense of the different types of error we might encounter, we can turn our focus to how error can be calculated.
Simply put, the **error** in a calculation is simply the difference between the calculated value and the actual value.
In other words,

.. math::
   E = \bar{x} - x
   :label: testing_error

where :math:`E` is the error in the calculated value :math:`x` compared to its true value :math:`\bar{x}`.
Another common way in which error is represented is as **relative error** :math:`(RE)`, which is simply the error divided by the true value,

.. math::
   RE = \frac{E}{\bar{x}}
   :label: testing_rerror

For our purposes we will mainly consider the **percent error** :math:`(PE)`, which is just the relative error multiplied by 100 [#testing_pct]_,

.. math::
   PE = 100 RE .
   :label: testing_pcterror

How do you know when your solution is "correct"?
------------------------------------------------

In order to determine whether or not we need to be concerned with errors in our estimates, we need to compare our estimate to the true values as seen above.
This process is often referred to as **benchmarking** or **stability testing**.
How do we do this in practice?
We recommend the following procedure:

1. Start with using an approximate solution for which a true value can be calculated.
   It is obviously not possible to make a comparison if you don't know the true values.
2. Assuming you have an equation the will allow you to calculate true values at any location within the domain of your problem, begin by calculating the estimated values and true values at the same spatial (and/or temporal) locations.
3. For each estimate and corresponding true value, calculate the percent error and store its value.
4. Review the output in a form that makes sense to you.
   Possibilities include
   
   - Calculating the mean percent error, or its maximum
   - Plotting the percent error along with the estimated values
   - Summing the percent error

.. topic:: Exercise - Spatial errors in heat conduction

   Now that we hopefully have a working solution to the heat conduction equation in one dimension we can assess the magnitude of error we introduce when poorly discretizing the problem in space.
   In other words, how bad do things get when we only estimate temperatures at distant points?
   For this exercise, you can use either your existing solution to the 1D heat conduction equation, or the solution for that exercise, heat_diff_const_answer.py_.
   
   **Tasks**:
   
   1. Modify the calculation of the analytical solution (true value) that is performed near the end of the code so that the true values are calculated at the same spatial locations :math:`x` as the finite difference calculation.
   2. Starting with the default parameter values in the code (:code:`nx = 6`, :code:`nt = 2000`), calculate the percent error in the calculated temperature for each location of :math:`x`.
   3. Add two lines to the code near the end to print out the minimum and maximum percent error to the screen using the :code:`print()` function.

   **Questions**:
   
   - If you vary the values for :code:`nx`, approximately how many points are required for the percent error to be less than 0.05%?
   - Does the percent error continue to decrease as you increase :code:`nx`, or does it a appear to reach a minimum at some point?
   
   **Notes**:
   
   - Although it is possible to perform step 2 directly in NumPy and without a :code:`for` loop, you are advised to use a :code:`for` loop for calculating the percent error.
   - You may want to skip over calculating the percent error for the first temperature point since the true value at the surface is equal to zero, and calculating percent error at the location will result in division by zero.

.. topic:: Exercise - Visualizing error

   In the previous exercise we observed error by outputting the minimum and maximum to the screen using the :code:`print()` function.
   However, it is often nice to not only see the range of error, but also how it varies in your calculation.
   In other words, it is nice to see where the error is largest, not just how large it may be.
   In this exercise we will add a plot to those displayed in the heat conduction script to see both the temperatures and percent error side by side.
   
   **Tasks**:
   
   1. Taking your code from the previous exercise, you will need to make some changes to the plotting at the end of the script to be able to display two plots side by side.
   You can start by making the changes below in your code:
   
   .. code:: python

       fig, (ax1, ax2) = plt.subplots(1,2) 
       ax1.plot(T[:, nt-1], -x/1e3, '.--')
       ax1.plot(T_analytical, -x_analytical/1e3, '-')
       ax1.set_xlabel("Temperature (C)")
       ax1.set_ylabel("Depth (km)")
       # Plot percent error below
       ax2.plot()
       ax2.set_xlabel("")
       plt.show()

   The main changes above are (1) changing the :code:`plt.subplots()` function to produce 1 row of plots with 2 columns of plots, and referring to those as :code:`ax1` and :code:`ax2`, (2) replacing the :code:`plt.xlabel()` and :code:`plt.ylabel()` with their equivalent commands for each plot, and (3) adding the second plot as :code:`ax2`.
   2. With the changes above, insert the variables you want to plot on the *x* and *y* axes of the second plot in the :code:`ax2.plot()` function, using the plot format :code:`'-*'`.
   3. Add a label for the *x* axis for the second plot.
   
   **Questions**:
   
   - If you perform a similar analysis to that done in the previous exercise (changing :code:`nx` and viewing the resulting error), does this seem more helpful than simply looking at the minimum and maximum error values?
   - Do you see any changes in terms of where the error occurs, or its magnitude at different depths when you change :code:`nx`?

Stability
---------

So far we have observed that changing the spatial resolution (distance between calculation points) can affect the error in our finite difference solutions.
Specifically, larger distances between points tends to increase error.
However, we have not observed any problems with the **stability** of our solutions.
The stability of a solution refers to whether or not a small change in the parameters of the system results in unstable growth of errors.
For problems involving time, a stable solution should either show a decrease in error with time or errors that do not change with time.
An unstable solution will show growth of errors with time that do not become bounded, and often grow increasingly.

There are a variety of methods by which stability of a given problem can be determined, and the range of parameters that result in stable behavior can be established.
For example, it is common to use the calculation of the Courant–Friedrichs–Lewy (or CFL) condition in problems that involve advection.
The CFL condition states that the distance material is advected should not exceed the distance between points in the solution grid.
In mathematical terms, the CFL condition is

.. math::
   C = \frac{u \Delta t}{\Delta x} \leq C_{\mathrm{max}}
   :label: testing_cfl

where :math:`u` is the velocity of advection, :math:`\Delta t` is the time step, and :math:`\Delta x` is the spatial distance between grid points.
We expect a stable solution as long as :math:`C_{\mathrm{max}} \leq 1.0`.
In fact, many people use a value of :math:`C_{\mathrm{max}} \leq 0.5` to ensure a stable solution.
Another common method for determining solution stability is von Neumann stability analysis.

.. topic:: Exercise - The time bomb

   We'll now take a look and an example of how a solution might become unstable.
   We will again use our plate cooling code from the past two exercises, this time exploring the effect of changes in time step.
   If you take the code from the last exercise, you do not need to make any significant modifications to the script to complete this exercise.

   **Questions**:

   - Using a spatial grid resolution of :code:`nx = 100`, what do you observe as you decrease the number of time grid points from :code:`nt = 1000` to smaller values? Run a series of simulations where you decrease :code:`nt` in increments of 100.
   - Do you observe any surprising changes in the error?
   - Why do you think this might occur?

.. rubric::Footnotes

.. [#testing_pct] It is common to use the absolute value of :eq:`testing_pcterror` for its determination, since that will give the magnitude of the error.
   However, I prefer to use the percent error calculation without the absolute value to be able to see whether the estimate is an underestimate or overestimate of the true value.

.. _yesterday: finite_differences_1.html
.. _heat_diff_const_answer.py: _static/heat_diff_const_answer.py
