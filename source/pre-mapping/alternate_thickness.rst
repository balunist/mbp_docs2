.. _alternate_thickness-label:

Alternate Thickness
*******************

.. role:: blue-bold

All components are grouped by their material type and thickness which will be the target
board type in a created map.  Each unique group results in a board type being added to
the board type list presented on the lumber tab.

While creating the board type list additional checking is done to determine if a targeted
board type with a thickness matching the component group's width could be used as an 
alternate thickness. If valid the width will be provided as an alternate thickness in a
dropdown list for the :blue-bold:`Height`. If not, the Height remains fixed with the
original smallest dimension for a thickness.

The effect of selecting the alternate, width, as a thickness in the resulting map is that the
components will be rolled over 90 degrees so that the width becomes the new thickness (height)
and the thickness becomes the new width. The length remains the same.

The following example shows a board type with a dropdown for :blue-bold:`Height` showing the
alternate 1.190 selected.  This alternate height comes from the width of the matching 
components in the group.  The original thickness of 0.905 is still available in the dropdown 
list enabling reverting back to the default.  This selection will persist and be shown the 
next time MBP is invoked.

    .. image:: /_static/images/alternatethick.png
        :width: 80 %
        :align: center

|

The following images show the effect of using the default height selection versus an alternate,
width, as the height.

|

    .. list-table::
        :widths: 10 30 30

        * -
          -  .. image:: /_static/images/default_height.png
                :width: 70 %
          -  .. image:: /_static/images/alternate_height.png
                :width: 65 %


