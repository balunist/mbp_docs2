.. _laser_kerf-label:

Laser Kerf
==========

.. role:: blue

Laser Kerf will adjust one half of laser kerf value outside each component
perimeter and one half of laser kerf inside inner cutouts.  The name laser
implies it is for laser manufacturing but it could also be user when working
with CNC to account for a router bit diameter.

The value of this setting is a floating point number in the current default
units. This option is available for map exports of SVG or DXF as a flat panel.

Showed here is an Export Map to SVG task with a :blue:`Laser Kerf` of 0.01 mm.

.. image:: /_static/images/laserkerf.png
    :width: 40%
    :align: center
