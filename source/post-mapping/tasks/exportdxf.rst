.. _dxfexport-label:

Export map to DXF
*****************


This task will export a flat panel design from the created map as a multi-layered DXF file.
The layers created will represent a top view of each component in the map. The layers
include perimeter, insets or pockets, cutouts, and labels with descriptive layer names,
which include the depth relative to the top and a diameter for holes specified in default
units. For inset features such as chambers, a depth range is provided. The **Tabs** option,
when selected, will modify the perimeter in the DXF export to include tabs, which are
represented as breaks in the perimeter loops. The size of and distance between the
breaks are based on the provided options **Width** and **Distance** respectively.
The **Height** option, when not set to zero, will create an additional tabs layer. This could
be useful for CNC users wanting to include tabs of a certain height.


.. image:: /_static/images/exportdxf.png
    :width: 40 %
    :align: center

