Heat conduction in 2D
=====================

The heat equation in two dimensions (without advection) can be
stated as 

.. math::
   \rho C_p \frac{\partial T}{\partial t} = \alpha \left( \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} \right) + H
   :label: heat-diff2d

The only addition compared to the one-dimensional case is the second order
derivative with respect to :math:`y` on the right hand side of the
equation.

.. topic:: Exercise

   Discretize equation :eq:`heat-diff2d`. Use the implicit
   discretization, i.e. calculate temperature for time step :math:`i` using
   temperature values from time step :math:`i` on the right hand
   side.

   - How many indices do you need?
   - How many boundary conditions do you need?
   - Draw a stencil to illustrate the spatial grid



.. math::

   \rho Cp \frac{T_{n,k}^i - T_{n,k}^{i-1}}{\Delta t} = 
   \alpha \left(
      \frac{T_{n+1,k}^i - 2T_{n,k}^i + T_{n-1,k}^i}{\Delta x^2} +
      \frac{T_{n,k+1}^i - 2T_{n,k}^i + T_{n,k-1}^i}{\Delta y^2} 
   \right) + H

which can be reorganized to find the coefficients of the unknown
temperature values:

.. math::
   T_{n-1,k}^i  \left( \frac{-\alpha}{\Delta x^2} \right) + 
   T_{n+1,k}^i  \left( \frac{-\alpha}{\Delta x^2} \right) + 
   T_{n,k}^i    \left( \frac{2\alpha}{\Delta x^2} + \frac{2\alpha}{\Delta y^2} + \frac{\rho C_p}{\Delta t} \right) +
   T_{n,k+1}^i  \left( \frac{-\alpha}{\Delta y^2} \right) + 
   T_{n,k-1}^i  \left( \frac{-\alpha}{\Delta y^2} \right) 
   =  H + T_{n,k}^{i-1} \rho C_p / \Delta t

This can again be shortened by assigning :math:`A = \frac{-\alpha}{\Delta x^2}`,
:math:`C = \frac{-\alpha}{\Delta y^2}`
and :math:`B = \frac{2\alpha}{\Delta x^2} + \frac{2\alpha}{\Delta y^2} + \frac{\rho C_p}{\Delta t}`,
leading to

.. math::
   A T_{n-1,k}^i   +
   A T_{n+1,k}^i   +
   B T_{n,k}^i     +
   C T_{n,k+1}^i   +
   C T_{n,k-1}^i   
   =  H + T_{n,k}^{i-1} \rho C_p / \Delta t


We have one of such equation for each spatial grid point (i.e.
if there are :math:`N=3` grid points in :math:`x` direction and
:math:`K=4` grid points in :math:`y` direction, there are total of twenty
of these equation). Some of the equation have to
be replaced by boundary conditions.

We can use the method shown in "Finite difference method, part II" to 
solve these equations. However, this time the indexing of the coefficient
array :math:`\mathbf{M}` is a bit more complicated.

Since we have :math:`N \times K` unknowns, and equally
many equations, :math:`\mathbf{M}` has :math:`N \times K` rows and
:math:`N \times K` columns. With 3 grid points in :math:`x`
direction and 4 grid points in :math:`y` direction, this means
that the size of :math:`\mathbf{M}` is :math:`12 \times 12`.
For each unique pair of :math:`n` and :math:`k`, i.e.
for each spatial grid point, there is
one row in the coefficient matrix.

When calculating the value of :math:`T_{n,k}^i`, one
fills the coefficients of the :math:`T` s (as separated
above) at row :math:`n \times K + k` (assuming we start 
counting from zero!). This number is called the
*global index* of the grid point and is a unique
number for each grid point in both (all) directions.

For example, when filling in coefficients of the equation
that calculate :math:`T` at :math:`n = 1` and :math:`k = 2`
the row in :math:`\mathbf{M}` we are looking at
row :math:`1 \times 4 + 2`. *On this row*, the coefficients
of the uknown temperatures will go to columns determined 
with the same rule: The coefficient for :math:`T_{n-1,k}^i`
(which is :math:`A`) will go to column :math:`(n-1)\times 4 + k`,
i.e. :math:`(1-1)\times 4 + 2`.

The whole right hand side of the discretized expression
(that has only temperature values from the previous time steps)
will go to the right hand side vector, row :math:`n \times K + k`.

If one wants to fill in a boundary condition :math:`T_{1,0}^i`
(i.e. the location :math:`y=0`) the coefficient matrix will
have a value of one at row :math:`1\times 4 + 0 = 4`, columnt
:math:`1\times 4 + 0 = 4`.


.. topic:: Exercise

   Script heat_diff2d_simple_implicit.py_ is an example of how to 
   calculate *one* time step using the implicit finite difference 
   method, in two spatial dimensions.

   - Read through the script and make sure you understand it.

   - Run the script in IPython (:code:`%run scriptname.py`) and
     then print arrays like :code:`M` or :code:`Tnew` at your IPython
     prompt. How do they look like?

   - Make the script calculate multiple time steps instead
     of only one:
     
         + Modify the script so that you add an :code:`for` loop
           around the two existing loops (for this, you need to 
           define :code:`nt` in your code)

         + Note that the temperature array only records the
           current known temperature field: it does not store
           the previous time steps within it like in the
           previous, 1D cases. 

         + At the end of the time loop, you need to copy (:code:`np.copy()`)
           the new temperature array :code:`Tnew` to be the known,
           "old" temperature array :code:`T`

--
^^

.. _heat_diff2d_simple_implicit.py: _static/heat_diff2d_simple_implicit.py

