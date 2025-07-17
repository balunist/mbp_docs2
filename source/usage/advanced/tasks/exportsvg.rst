.. _svgexport-label:

Export map to SVG
~~~~~~~~~~~~~~~~~

This task will export a flat panel design from the created map as a
multi~colored SVG file. The colors represent loops taken from the top view of
each component in the map. The colored loops include perimeter, insets or
pockets, and cutouts. You can also include component labels with part numbers,
descriptive name and dimensions. Insets has a  **Grayscale** color which when
set will produce a varying gray fill color, the lighter gray for deeper inset
pockets and the darker gray for shallow inset pockets. This enables creating
an infinite number of toolpaths based on depth. Be sure to select the
appropriate scale based on the application you plan to import it into.

The SVG output file will be scale to selected Dots Per Inch (DPI).

    - Scale to 96 DPI, the modern scale used by Inkscape and browsers.
    - Scale to 72 DPI, an older scale used by Adobe Illustrator.
    - Scale to 90 DPI, a retired scale used by Vectric VCarve Pro.

.. image:: /_static/images/exportsvg.jpg
    :width: 40 %
    :align: center

|
