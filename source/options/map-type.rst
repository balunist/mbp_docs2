.. _map_type-label:


Map Output Type
===============

Component Bodies
    - Includes copies of component bodies in the created map. The output types SVG File,
      DXF File and Report are available as Post-Mapping tasks described in
      :ref:`Post-Mapping Tasks <tasks-label>`.

DXF File
    - Creates a layered DXF file of the map as a view from the top. It includes perimeter,
      cutouts, insets, and labels. Inset layer names will describe either a depth or, for
      faces with varying depths, a depth range.

      The following additional options are available for this map type:

        - :ref:`laser_kerf-label`,
        - :ref:`colors-label`,
        - :ref:`file_board-label`,
        - :ref:`include_profs-label`

SVG File
    - Creates a color-coded SVG file of the map as a view from the top. It will include
      perimeter, cutouts, insets, and labels in selectable colors.

      The following additional options are available for this map output type:

        - :ref:`laser_kerf-label`,
        - :ref:`line_weight-label`,
        - :ref:`colors-label`,
        - :ref:`file_board-label`,
        - :ref:`svg_scale-label`,
        - :ref:`include_profs-label`,
        - :ref:`deepnest-label`

Report Output
      This option creates an HTML document which can be viewed in your default browser
      when the View option is selected.

      The following additional options are available for this map output type:

        - :ref:`colors-label`,
        - :ref:`include_profs-label`,
