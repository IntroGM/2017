
Stokes and continuity equations in 2D
=====================================

Stokes
------

The equation for the conservation of mass, for an incompressible fluid
with negligible inertial forces (in comparison to gravitational acceleration),
i.e. the Stokes equation, is

.. math::
   
   \frac{\partial \sigma'_{ij}}{\partial x_j} - \frac{\partial P}{\partial x_i} = -\rho g_i

In 2D, this gives us two equations, 

.. math::
   \begin{align}
   \frac{\partial \sigma'_{xx}}{\partial x} + \frac{\partial \sigma'_{xz}}{\partial z} - \frac{\partial P}{\partial x} & = -\rho g_x \\
   \frac{\partial \sigma'_{zz}}{\partial z} + \frac{\partial \sigma'_{zx}}{\partial x} - \frac{\partial P}{\partial z} & = -\rho g_z
   \end{align}
   :label: 2d-stokes

In the case of *incompressible fluid* a rheological law relates the deviatoric stress to
strain rate: 

.. math::
   \sigma'_{ij} = 2\eta\dot\epsilon_{ij}
   :label: newtonian-rheol

This is called the *Newtonian* viscous rheology, where the deviatoric stress
is linearly dependent on the strain rate. *Non-Newtonian* rheologies,
on the other hand, relate these with an exponent 
:math:`(\sigma'_{ij})^n = 2\eta\dot\epsilon_{ij}`.

The strain rate is defined as

.. math::
   \dot\epsilon_{ij} = \frac{1}{2}\left( \frac{\partial v_i}{\partial x_j} + \frac{\partial v_j}{\partial x_i} \right)
   :label: strain-rate

Applying :eq:`strain-rate` in :eq:`newtonian-rheol` gives

.. math::
   \sigma'_{ij} = \eta\left( \frac{\partial v_i}{\partial x_j} + \frac{\partial v_j}{\partial x_i} \right)

which can be plugged in the Stokes equations :eq:`2d-stokes` to get

.. math::
   \begin{align}
   \frac{\partial}{\partial x} \left( \eta\left( \frac{\partial v_x}{\partial x} + \frac{\partial v_x}{\partial x} \right) \right) + 
   \frac{\partial}{\partial z} \left( \eta\left( \frac{\partial v_x}{\partial z} + \frac{\partial v_z}{\partial x} \right) \right) - 
   \frac{\partial P}{\partial x} & = -\rho g_x \\
   \frac{\partial}{\partial z} \left( \eta\left( \frac{\partial v_z}{\partial z} + \frac{\partial v_z}{\partial z} \right) \right) + 
   \frac{\partial}{\partial x} \left( \eta\left( \frac{\partial v_z}{\partial x} + \frac{\partial v_x}{\partial z} \right) \right) - 
   \frac{\partial P}{\partial z} & = -\rho g_z
   \end{align}
   :label: 2d-stokes-open

If viscosity is constant in respect to :math:`x` and :math:`z`, this simplifies to

.. math::
   \begin{align}
   \eta\left( \frac{\partial^2 v_x}{\partial x^2} + \frac{\partial^2 v_x}{\partial z^2} \right) - \frac{\partial P}{\partial x} & = -\rho g_x \\
   \eta\left( \frac{\partial^2 v_z}{\partial z^2} + \frac{\partial^2 v_z}{\partial x^2} \right) - \frac{\partial P}{\partial z} & = -\rho g_z
   \end{align}
   :label: stokes-const-eta

As can be seen here, the Stokes equation relates fluid velocity to pressure gradients
and body forces (gravitational forces); the flow is driven by either one or both.

.. topic:: Exercise

   In what geological process would the fluid (rock) flow be driven
   by 

   - gravitational forces
   - pressure gradients?

.. topic:: Exercise

   Discretize equation :eq:`stokes-const-eta`.

   - What are the unknowns in the equation?
   - Can you rearrange the equations to solve for
     those unknowns explicitly?

Continuity
----------

The continuity equation states that for an infinitesimally small volume
of material, the incoming flux of new material is balanced by same
amount of material going out. This applies for incompressible fluids.

.. math::
   \frac{\partial v_x}{\partial x} + \frac{\partial v_z}{\partial z} = 0
   :label: continuity

.. topic:: Exercise 

   Discretize equation :eq:`continuity`.

   - What are the unknowns in the equation?
   - Can you rearrange the equation to solve for those
     unknowns explicitly?

Stokes and continuity
---------------------

In two-dimensional problems we have two Stokes equations (so called
x-Stokes and z-Stokes here), and one continuity equation. So for
each grid point we can formulate three equations. With these 
three equations we can solve for the three unknowns using
an implicit formulation.

Note that the Stokes/continuity equations do not include time:
they are used to find out the velocity field caused by density 
differences and external forcing (pressure gradients). If one
knows the velocity and has chosen a :math:`\Delta t`, one
can calculate where the material would advect during the
next time step.

.. topic:: Exercise

   Looking at the two Stokes equations :eq:`stokes-const-eta` and
   the continuity equation :eq:`continuity`, and their discretized
   versions,

   - how many boundary conditions do you need to solve them?
   - what would the coefficients for the implicit solution
     look like (matrix :math:`\mathbf{M}`)? How large
     would :math:`\mathbf{M}` be?

Boundary conditions
-------------------

Similarly to a constant temperature boundary condition for
the heat equation, one can define constant velocity boundary 
conditions for the Stokes equation

.. math::
   \begin{align}
   v_x = \textrm{constant} & \quad \textrm{and} \\
   v_z = \textrm{constant} &  
   \end{align}

This is so called "no-slip" boundary condition. Another
often used boundary condition is so called
free-slip. E.g. at boundary
:math:`x=x_0` this would be stated as

.. math::
   \begin{align}
   v_x = 0 & \quad \textrm{and} \\
   \frac{\partial v_z}{\partial x} = 0
   \end{align}

If the velocity perpendicular to the boundary does not change
across the boundary, the boundary condition is so
called "stress free" boundary condition:

.. math::
   \frac{\partial v_x}{\partial x} = 0

This would permit the outflow and inflow of material
across the boundary.
