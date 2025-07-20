.. _deepnest-label:

Deepnest
========

Deepnest is an open source nesting application, great for laser cutters,
plasma cutters, and other CNC machines. Deepnest packs your parts into a
compact area to save material and time. It automatically merges common lines
so the laser doesn't cut the same path twice. MapBoards Pro can export the map
it creates as an SVG file image.


Selecting the  **Format for Deepnest** when exporting an SVG file will enhance
the image intended for Deepnest in the following ways.

    - The mapped board perimeter will be included separate from components it
      contains so it can be used with Deepnest as target container
    - Provides the option  :ref:`explode_labels-label` which will include
      labels in a format recognized by Deepnest

Note: If the MBP created map already has labels created the SVG export will
use the created labels and not create new labels or present the label options.
Creating labels before the export can be very powerful since you can modify
the label sketch to be whatever you like. It is a sketch on top of each mapped
board named  **Component Labels**. It can be text or any valid sketch type and
as long as it is contained within the part perimeter Deepnest will move the
image with the parts when it is rearranging the mapped board.

    `Getting started with Deepnest <https://deepnest.io/#quickstart>`__
