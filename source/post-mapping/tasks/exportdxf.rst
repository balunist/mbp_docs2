.. _dxfexport-label:

Export map to DXF
*****************


This task will export a flat panel design from the created map as a multi-layered DXF file.
The layers created will represent a top view of each component in the map. The layers
include **Perimeter**, **Insets**, or **Cutouts**. The Insets layer includes features such 
as pockets, rebates, dados, and holes. The layer names include the depth relative to the top 
or diameter for holes specified in default units. These profiles will be included as solid 
lines in the color specified in the color options.

A separate profile selection **Edge Treatments**, when selected, will include features such 
as edge chambers and round overs in a separate layer.  The layer name will include a depth range 
in default units.  These profile features will be included as **dashed** lines in the color 
specified in the color options.

The **Bottom Insets** option, when selected, will include the bottom insets as **dashed** lines 
in the color specified in the color options.

The **Tabs** option, when selected, will modify the perimeter in the DXF export to include 
tabs, which are represented as breaks in the perimeter loops. The size of and distance between 
the breaks are based on the provided options **Width** and **Distance** respectively.
The **Height** option, when not set to zero, will create an additional tabs layer. This could
be useful for CNC users wanting to include tabs of a certain height.

The option **Splines to Polylines** has been added.  When selected, splines are replaced with
polylines in all layers of the DXF output. Polylines may be required by some software when creating
toolpaths if spline handling is an issue.

.. image:: /_static/images/exportdxf.jpg
    :width: 40 %
    :align: center

