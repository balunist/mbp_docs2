.. _sketchmap-label:

Sketch Map
~~~~~~~~~~


The  **Sketch Map** task will create perimeter, cutout and inset sketches of
the components as they are placed in the map. The perimeter and cutout
sketches are useful when creating a 2D Contour toolpaths in additive
manufacturing. The sketches created can be found in sketches under each Board
component in Map on the browser tree. You can select these sketches when
adding to geometry for toolpath creation. The resulting sketches can be hidden
or shown. If you are planning to use additive manufacturing you may want to
select hide. This leaves the board and components visible which are needed
when creating the setup. The **Tabs** option, when selected, will modify the
perimeter sketch to include tabs which are represented as breaks in perimeter
loops. The size of the breaks and distance apart are based on the provided
options  **Width** and  **Distance** respectively. The  **Height** option,
when not set to zero, will result in an additional tabs sketch being created.
This could be useful with CNC users wanting to include tabs of a certain
height.

.. image:: /_static/images/sketchmap.png
    :width: 40 %
    :align: center

