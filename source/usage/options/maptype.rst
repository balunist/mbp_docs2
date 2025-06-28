.. _maptype-label:


Map Output Type
===============

Component Bodies
    - Includes copies of component bodies in the created map.  The output types 
      SVG File, DXF File and Report are available as Post-Mapping tasks described here
      :ref:`Post-Mapping Tasks <tasks-label>`.
Sketch
    - Creates sketches of the map as view from the top. It includes perimeter,
      cutouts, insets, labels and Bottom Insets.
DXF File
    - Creates a layered DXF file of the map as view from the top. It includes perimeter,
      cutouts, insets, and labels. Inset layers will describe either a depth or depth range
      for a faces with varying depths.

      The following additional options are available for this map type.

        - :ref:`laserkerf-label`,  
        - :ref:`colors-label`,  
        - :ref:`fileboard-label`,  
        - :ref:`includeprofs-label`

SVG File
    - Creates a color coded SVG file of the map as view from the top. The default line 
      colors includes perimeter (Blue), cutouts (Red), insets (Yellow, Green, Cyan, Magenta), 
      and labels (Grey). The line color for insets of different depths will cycle through
      four different colors.

      The following additional options are available for this map type.

        - :ref:`laserkerf-label`,  
        - :ref:`lineweight-label`,  
        - :ref:`colors-label`,  
        - :ref:`fileboard-label`, 
        - :ref:`svgscale-label`,  
        - :ref:`includeprofs-label`,  
        - :ref:`deepnest-label`


