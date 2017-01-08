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
