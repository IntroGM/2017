.. Finite differences method section

Finite differences formulation of the heat conduction problem
=============================================================

The full heat conduction-advection-production equation seen before
can be stated in 1D as 

.. math::
   \rho(x) C_p(x) \left( \frac{\delta T}{\delta t} + v_x \frac{\delta T}{\delta x} \right) = \frac{\delta}{\delta x} \left( \alpha(x) \frac{\delta T}{\delta x} \right) + H(x)
   :label: heat_eq_full

We can simplify equation :eq:`heat_eq_full` by assuming that there is no 
advection of heat and that all the physical properties are constant:

.. math::
   \rho C_p \frac{\delta T}{\delta t} = \alpha \frac{\delta^2 T}{\delta x^2} + H
   :label: heat_eq_noadv_const


.. topic:: Exercise

   Discretize the equation :eq:`heat_eq_noadv_const`. Use forward difference
   approximation in time (:math:`t`) and central difference approximation 
   in space (:math:`x`). 


