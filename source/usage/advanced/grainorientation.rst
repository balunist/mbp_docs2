.. _grainorientation-label:

.. |hozizon| image:: /_static/images/Horizontal.png
                    :height: 2.5ex
                    :class: no-scaled-link

.. |vert| image:: /_static/images/Vertical.png
                    :height: 2.5ex
                    :class: no-scaled-link


.. toctree::
   :maxdepth: 2

Grain Orientation on Boards
===========================
    
    
    By default the component's grain is determined by it's longest edge. This can be overridden by applying a 3D 
    appearance and enabling :ref:`autograinalign-label`. The Component grain determined by either method can be rotated 
    90 degrees by choosing **Rotate** when a component has been selected as shown below. 
    See :ref:`Selection Support <selection-label>` for details.

    .. image:: /_static/images/SelectionRotate.png
        :width: 75 %
        :align: center

|

    The component's grain will be aligned with the grain on the targeted board. Grain direction 
    on the targeted board is selectable by toggling the double-arrowed icon horizontal (X) |hozizon|
    or vertical (Y) |vert| for board types on the lumber tab or when optionally entering stock lumber.
    
|

    .. list-table::
        :widths: 2 47 2 47 2
        :header-rows: 1

        * -
          -  Board Types
          - 
          -  Entering Stock Lumber
          - 
        * - 
          -  .. image:: /_static/images/LumberGrain.png
                :width: 100 %
          - 
          -  .. image:: /_static/images/StockGrain.png
                :width: 100 %
          - 



