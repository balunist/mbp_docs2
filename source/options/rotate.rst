
.. _rotate-label:

Can Rotate
==========

.. role:: blue

When this option is selected, a component may have its long edge rotated perpendicular
to the targeted board grain direction. This will only occur if it would better utilize space
or if none of the remaining components would fit an available space based on the 
:blue:`arrangement type` selected.

.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - Arrangement Type
    - Selection Process
  * - Matching Width Horizontally
    - Select the next component which best matches the width of the last component placed, either rotated or not.
  * - Matching Length Vertically
    - Select the next component which best matches the length of the last component placed, either rotated or not.
  * - Fill Boards Diagonally
    - Select the next component which best matches the length of the last component placed, either rotated or not,
      as it alternately progresses horizontally and vertically.

