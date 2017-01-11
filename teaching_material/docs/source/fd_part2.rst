Finite difference method, part II
=================================

All previous applications of finite difference
methods to our problems have relied on the fact
that we could reorganize the discretized equations
in to form where the left

.. math::
   T_n^{i} = \textrm{some expression of } T^{i-1}

This is because we have chosen to discretize the
equation with forward difference in time. For example
with the simple heat diffusion equation (no advection):

.. math::
   \rho C_p \frac{T_n^{i} - T_n^{i-1}}{\Delta t} = 
   \alpha \frac{T_{n+1}^{i-1} - 2T_n^{i-1} + T_{n-1}^{i-1}}{\Delta x^2} + H

We can, however, formulate the same heat equation with
a backward difference in time (which is often beneficial
for the *stability* of the solution):

.. math::
   \rho C_p \frac{T_n^{i} - T_n^{i-1}}{\Delta t} = 
   \alpha \frac{T_{n+1}^i - 2T_n^i + T_{n-1}^i}{\Delta x^2} + H
   :label: heat_diff_backward

Now, in order to calculate the new value :math:`T_n^i`
we need to know the new values next to it, :math:`T_{n\pm 1}^i`.
Clearly, this we are not able to use the new values to 
calculate those exact new values!

The way around this problem is to solve the system
of linear equations formed by the difference equations. Every time
we want to calculate the new values of :math:`T` for the
next time step, we have :math:`N` equations, one for
each grid point (:math:`x_0`, :math:`x_1`, :math:`x_2`, ..., :math:`x_{N-1}`)
Since this is also the number of unknown values of :math:`T` s
(:math:`T_0`, :math:`T_1`, :math:`T_2`, ..., :math:`T_{N-1}`),
we can solve all the values of :math:`T` on one go.

Consider eq. :eq:`heat_diff_backward`. If we reorganize
the equation to find all the coefficients for each :math:`T`,
we get

.. math::
   T_{n-1}^i \left(\frac{-\alpha}{\Delta x^2}\right) +
   T_n^i \left(\frac{\rho C_p}{\Delta t} + \frac{2\alpha}{\Delta x^2}\right) +
   T_{n+1}^i \left(\frac{-\alpha}{\Delta x^2}\right) 
   = T_n^{i-1} \rho C_p / \Delta t + H

Here, the coefficients for all the :math:`T` s on the
left hand side are known, and so is the whole
right hand side, too. If we mark, for convenience,
:math:`A=-\alpha/\Delta x^2` and :math:`B=\frac{\rho C_p}{\Delta t} + \frac{2\alpha}{\Delta x^2}`,
we can write 

.. math::
   T_{n-1}^i A +
   T_n^i B + 
   T_{n+1}^i A
   = T_n^{i-1} \rho C_p / \Delta t + H

For each spatial grid point :math:`n` there
exists one such equation. If we have four grid points
in :math:`x` direction, this leads a system of equations like

.. math::
   \begin{eqnarray}
   T_{-1}^i A  +&  T_0^i B  +&  T_1^i A  &           &           &           &  =  &  T_0^{i-1} \rho C_p / \Delta t + H \\
                &  T_0^i A  +&  T_1^i B  +&  T_2^i A  +&           &           &  =  &  T_1^{i-1} \rho C_p / \Delta t + H \\
                &            &  T_1^i A  +&  T_2^i B  +&  T_3^i A  &           &  =  &  T_2^{i-1} \rho C_p / \Delta t + H \\
                &            &           &  T_2^i A  +&  T_3^i B  +&  T_4^i A  &  =  &  T_3^{i-1} \rho C_p / \Delta t + H 
   \end{eqnarray}

Since our grid has four points, there are no points :math:`n=4`
or :math:`n=-1`. So the first and last equation are not valid.
We have to replace them by something given by the boundary conditions.
If we have fixed surface temperature and fixed bottom temperature,
we get following system:

.. math::
   \begin{eqnarray}
     T_0^i     &           &           &             &  =  &  T_{\mathrm{surf}}                 \\
     T_0^i A  +&  T_1^i B  +&  T_2^i A  +&           &  =  &  T_1^{i-1} \rho C_p / \Delta t + H \\
               &  T_1^i A  +&  T_2^i B  +&  T_3^i A  &  =  &  T_2^{i-1} \rho C_p / \Delta t + H \\
               &           &            &  T_3^i     &  =  &  T_{\mathrm{bott}}                 
   \end{eqnarray}

In matrix notation, we can state the same as

.. math::
   \begin{bmatrix}
     1 &   &   &   \\
     A & B & A &   \\
       & A & B & A \\
       &   &   & 1 
   \end{bmatrix}
   \begin{bmatrix}
     T_0^i \\
     T_1^i \\
     T_2^i \\
     T_3^i 
   \end{bmatrix}
   =
   \begin{bmatrix}
     T_{\mathrm{surf}} \\
     T_1^{i-1} \rho C_p / \Delta t + H \\
     T_2^{i-1} \rho C_p / \Delta t + H \\
     T_{\mathrm{bott}} 
   \end{bmatrix}

or, in shorter notation

.. math::
   \mathbf{M}\mathbf{T}^i = \mathbf{b}

where :math:`\mathbf{M}` is the coefficient matrix
(values of which are known), 
:math:`\mathbf{T}^i` is the temperature vector of
unknown values (i.e. those we want to solve), and
:math:`\mathbf{b}` is the right hand side with
known values.

In order to solve the unknown :math:`\mathbf{T}^i`
we can multiply the equation by the inverse of 
the matrix :math:`\mathbf{M}`.

.. math::
   \begin{eqnarray}
   \mathbf{M}^{-1} \mathbf{M} \mathbf{T}^i & = & \mathbf{M}^{-1} \mathbf{b} \\
   \mathbf{T}^i & = & \mathbf{M}^{-1} \mathbf{b}
   \end{eqnarray}

In Python (NumPy), there is a more direct way to achieve this,
a function called :code:`np.linalg.solve()`.

.. code:: python
   T = np.linalg.solve(M, rhs)

See script heat_diff_simple_implicit.py_ for an example how to use
it.

.. topic:: Exercise
   
   Take the script template heat_diff_const_implicit.py_ and fill in the missing
   lines. Use heat_diff_simple_implicit.py_ as an example, if needed.
   This code will then calculate the cooling lithosphere problem
   using an implicit finite difference method.

   Experiment with the size of time step (or, number of time steps taken):
   Can you make it "explode" like with the heat diffusion code with
   explicit formulation used previously?

.. _heat_diff_simple_implicit.py: _static/heat_diff_simple_implicit.py
.. _heat_diff_const_implicit.py: _static/heat_diff_const_implicit.py


