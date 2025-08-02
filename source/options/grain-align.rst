.. _auto_grain_align-label:

Automatic Grain Alignment
=========================


Setting this option will automatically rotate components, if needed, to align the visual
grain's 3D appearance with the targeted board’s grain direction. The component rotation
can only be made aligned or perpendicular to the board’s grain direction. . This will only
affect components that have 3D appearances applied, such as those found in the **Wood
(Solid)** category.

Wood grain is often aligned along the longest edge length matching the MBP mapping.
MBP will align the longest edge with the targeted board’s grain direction by default.
When a component has a 3D appearance applied the Texture Map Controls, available by
right-clicking on a selected component, can be used to rotate the visible grain to make it
more aesthetically pleasing. This rotation will only be recognized if it is aligned or
perpendicular with the component’s long edge. Shown here are Texture Map Controls
being used to rotate the grain to be perpendicular to its long edge on a cabinet side and
the resulting map created for this side when this option is set. The side is vertically
oriented but the grain is horizontal, matching the targeted board’s grain which in this
case was set to horizontal on the created map.


**Note:** The components must be contained in a fusion component in order for grain
alignment to work reliably.


.. list-table::
  :widths: 10 30 20 30 10

  * -
    -  .. image:: /_static/images/TextureMap.png
          :width: 100 %
    -  .. image:: /_static/images/GrainAlign.png
          :width: 100 %
    -  .. image:: /_static/images/CabinetSide.png
          :width: 120 %
    -
