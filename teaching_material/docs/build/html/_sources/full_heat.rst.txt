Heat conduction with advection
==============================

We now have all the tools to implement a "full" one-dimensional
heat transfer equation where we consider

- heat conduction,
- heat advection, 
- heat generation, and
- variable physical paramaters.

.. math::
   \rho(x) C_p(x) \left( \frac{\partial T}{\partial t} + v_x \frac{\partial T}{\partial x} \right) = \frac{\partial}{\partial x} \left( \alpha(x) \frac{\partial T}{\partial x} \right) + H(x)
   :label: heat-diff-adv-gen

.. topic:: Exercise

   Discretize equation :eq:`heat-diff-adv-gen`.

   - Again, use forward difference in time and central difference in space
     for the diffusion term. For the advection term, however, you can
     try using either forward, backward or even central difference. 
   
      + This choice is easy to change later once your code is working.

   - Use the *staggered grid* approach: 
     
      + Let :math:`T` itself together with :math:`\rho`, :math:`C_p` and 
        :math:`H` to be defined at the main grid points
      + Let :math:`\alpha` be defined in the mid-point grid where grid points 
        are located half-way between main grid grid points 

   - Draw a stencil covering grid points in space and in time, for 
     the whole model domain (use small grid sizes, e.g. 5 spatial grid points,
     4 time step)

      + Mark grid points covered by initial and boundary conditions

   - Adjust your discretized equation so that the indices for :math:`\alpha`
     are correct and has no "half-indices"

We will implement a crustal scale heat transfer model, where 
we consider the heat diffusion from the moho towards the surface,
heat generation within the crust, and upward heat advection caused by the 
removal of crustal material at the surface by erosion.

Let us construct a model with following parameters:

   - Model size: :math:`L=35~\mathrm{km}` (crust)
   - Fixed temperature boundary conditions: :math:`T=T_{\mathrm{surf}}`
     at :math:`x=0`; :math:`T=T_{\mathrm{bott}}` at :math:`x=L`
