Heat conduction with advection
==============================

We now have all the tools to implement a "full" one-dimensional
heat transfer equation where we consider

- heat conduction,
- heat advection, 
- heat generation, and
- variable physical paramaters.

.. math::
   \rho(x) C_p(x) \left( \frac{\partial T}{\partial t} + v_x \frac{\partial T}{\partial x} \right) = \frac{\partial}{\partial x} \left( \alpha(x) \frac{\partial T}{\partial x} \right) + H
   :label: heat-diff-adv-gen

.. topic:: Exercise

   Discretize equation :eq:`heat-diff-adv-gen`.

   Again, use forward difference in time and central difference in space
   for the diffusion term. For the advection term, however, you can
   try using either forward, backward or even central difference. This
   choice is easy to change later once your code is working.

We will implement a crustal scale heat transfer model, where 
we consider the heat diffusion from the moho towards the surface,
heat generation within the crust, and upward heat advection caused by the removal
of crustal material at the surface by erosion.

.. topic:: Exercise

   Take your solution to the one of the previous exercises where
   we solved the heat equation with variable physical parameters but 
   without heat advection (heat_diff_var.py_ or start from the
   already working script heat_diff_var_answer.py_). Save this file with
   a new name (e.g. :code:`heat_diff_adv.py`).

   Modify the script to include heat advection:

   1. Define a variable :code:`vx` that holds the advection velocity.
   2. Modify the line :code:`T[ix, it] = ...` so that you include the
      advection term. Use the following discretized version of the
      equation

      .. math::
         T_n^{i} = \left( 
                        \left.
                        \left( 
                              \alpha_n \frac{T_{n+1}^{i-1} - T_n^{i-1}}{\Delta x^2} - \alpha_{n-1} \frac{T_n^{i-1} - T_{n-1}^{i-1}}{\Delta x^2} + H_n
                        \right)
                        \middle/
                        \rho_n C_{p,n} 
                        \right.
                        - v_x \frac{T_{n+1}^{i-1} - T_{n-1}^{i-1}}{2 \Delta x}
                     \right) \Delta t + T_n^{i-1}

  
.. COMMENTED OUT: 
   As a remainder, 
   .. math::
      \frac{\partial}{\partial x} \left( \alpha(x)\frac{\partial T}{\partial x} \right)_{x=x_n,~t=t^i}
      \approx 
      \left. 
         \left( \alpha_n \frac{T_{n+1}^i - T_n^i}{\Delta x} - \alpha_{n-1} \frac{T_n^i - T_{n-1}^i}{\Delta x} \right)
      \middle / \Delta x
      \right.
   .. math::
      T_n^{i} = \left( 
                     \left.
                     \left( 
                           \alpha_n \frac{T_{n+1}^{i-1} - T_n^{i-1}}{\Delta x^2} - \alpha_{n-1} \frac{T_n^{i-1} - T_{n-1}^{i-1}}{\Delta x^2} + H_n
                     \right)
                     \middle/
                     \rho_n C_{p,n} 
                     \right.
                     - v_x \frac{T_{n+1}^{i-1} - T_{n-1}^{i-1}}{2 \Delta x}
                  \right) \Delta t + T_n^{i-1}

.. _heat_diff_var.py: _static/heat_diff_var.py
.. _heat_diff_var_answer.py: _static/heat_diff_var_answer.py

--
^^
