.. _holes-as-point:

Holes as Point
**************

With DXF export, when holes are encountered exporting cutouts or insets, a separate layer will 
be created for each unique hole type.  The layer name describes the hole type with its diameter 
and depth in default units. For example, "Hole DIAM 10.000 D 5.000" would represent a hole with 
a diameter of 10 units and a depth of 5 units.

The option, **Holes as Point**, has been added. When selected, holes are represented as points rather 
than full circular profiles in the DXF output. This can be useful for software that prefers point 
representations for drilling operations.  

.. image:: /_static/images/holesaspoint.jpg
    :width: 40 %
    :align: center