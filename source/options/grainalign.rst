:orphan:

.. _autograinalign-label:

Automatic Grain Alignment
=========================


Setting this option will automatically rotate parts 90 degrees, if needed, to align the grain with the targeted board's grain
direction which can be configured to be horizontal or vertical. This will only affect parts that have 3D appearances applied 
such as appearances found in the  **Wood (Solid)** category.

Wood grain is often aligned along the longest edge length which matches MBP mapping. MBP will by default align the longest edge with the 
targeted board's grain direction. The Texture Map Controls, available by right-click on a select part, can be used to rotate the visible 
grain to make it more aesthetically pleasing. Shown here is Texture Map Controls being used to rotate the grain 90 degrees on a cabinet side
and the resulting map created for this side when this option is set. The side is vertically oriented but the grain is horizontal matching
the targeted board's grain which in this case was set to horizontal on the created map.   
      

**Note:** The parts must be contained in a fusion component in order for grain alignment to work reliably.  

    .. list-table::
        :widths: 2 33 30 33 2

        * - 
          -  .. image:: /_static/images/TextureMap.png
                :width: 100 %
          -  **---> Resulting Map --->**
          -  .. image:: /_static/images/CabinetSide.png
                :width: 120 %
          - 
