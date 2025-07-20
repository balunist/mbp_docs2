.. _additive_manufacturing-label:

Additive Manufacturing
**********************

Using Fusion 360's additive manufacturing is made easy with the addition
of the post-mapping task **Manufacturing Model**.  This task will create or
switch to an existing manufacturing model (MM) with setup.  Using a MM
provides the convenience of shadowing any changes made to a mapped board in
the design workspace.

If you plan to use the Fusion additive manufacturing workspace to complete the
cutting with a CNC Router the following steps are suggested for a starting
point.  I would also suggest to always try the default options for toolpaths
with simulation first.

- Create a map with a :ref:`map_type-label` of Component Bodies
- Right-click on the map object in the browser tree and execute the
  **Manufacturing Model** task
- Select which board you want exported
- Check the **Create Setup** and a **WCS Origin** that matches your CNC
  machine setup origin then press OK
- Create one or more toolpaths then simulate to validate

.. note::
  For a simple body cutouts the **2D Contour** toolpath is a good choice.
  See :ref:`Manufacturing Model <manufacturing_model-label>` which shows how to create
  this toolpath using the default setup created by the Manufacturing Model
  task.

