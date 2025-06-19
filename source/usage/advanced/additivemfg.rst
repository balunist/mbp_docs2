.. _additivemfg-label:

Additive Manufacturing
======================

Using Fusion 360's additive manufacturing is now made easy with the addition of the post-mapping 
task **Manufacturing Model**.  This task will create or switch to an existing
manufacturing model (MM) with setup.  Using a MM provides the convenience of shadowing any changes
made to a mapped board in the design workspace.   

If you plan to use the Fusion additive manufacturing workspace to complete the cutting with 
a CNC Router the following steps are suggested for a starting point.  I would also 
suggest to always try the default options for toolpaths with simulation first.

- Create a map with a :ref:`maptype-label` of Component Bodies and the option Create boards 
  **As Glass** turned off
- Right-click on the map object in the browser tree and execute the **Manufacturing Model** task
- Check the **Create Setup** and an **WCS Origin** that matches you CNC 
  machine setup then press OK
- Create one or more toolpaths then simulate to validate

Note: For simple body cutouts the 2D Contour toolpath is a good choice.
See :ref:`Manufacturing Model <mfgmodel-label>` which shows how to create this toolpath using the 
default setup created by the Manufacturing Model task.    

|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

