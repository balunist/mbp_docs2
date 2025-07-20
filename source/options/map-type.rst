.. _map_type-label:


Map Output Type
===============

Component Bodies
    - Includes copies of component bodies in the created map.  The output types
      SVG File, DXF File and Report are available as Post-Mapping tasks
      described here :ref:`Post-Mapping Tasks <tasks-label>`.

DXF File
    - Creates a layered DXF file of the map as view from the top. It includes
      perimeter, cutouts, insets, and labels. Inset layers will describe
      either a depth or depth range for a faces with varying depths.

      The following additional options are available for this map type.

        - :ref:`laser_kerf-label`,
        - :ref:`colors-label`,
        - :ref:`file_board-label`,
        - :ref:`include_profs-label`

SVG File
    - Creates a color coded SVG file of the map as view from the top. The
      default line colors includes perimeter (Blue), cutouts (Red), insets
      (Yellow, Green, Cyan, Magenta), and labels (Grey). The line color for
      insets of different depths will cycle through four different colors.

      The following additional options are available for this map output type.

        - :ref:`laser_kerf-label`,
        - :ref:`line_weight-label`,
        - :ref:`colors-label`,
        - :ref:`file_board-label`,
        - :ref:`svg_scale-label`,
        - :ref:`include_profs-label`,
        - :ref:`deepnest-label`

Report Output
      Creates an HTML document which will be viewed in the default browser
      when the View option is selected.

      The following additional options are available for this map output type.

        - :ref:`colors-label`,
        - :ref:`include_profs-label`,
