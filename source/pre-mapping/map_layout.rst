.. _map_layout-label:

Choosing Map Layout
*******************

    There are 12 ways to control the layout of boards in the created map. See image below. The
    layout you choose may be a decision based on preference or a requirement of your
    manufacturing process. The settings you select can be set as defaults by selecting the 
    **Save as Default** button on the options tab.

**Map Orientation**
    This should be set to match the **Z Up** or **Y Up** orientation of your model. MBP will create the
    map in what would be the TOP view for the setting you have selected. At the completion of map
    creation, MBP will bring the TOP view into focus facing forward.

**Board Orientation**
    By setting the board type dimensions, Width and Length, you can have the board oriented in
    either portrait or landscape. **Width** is the size in the vertical Y direction and **Length** 
    is the size in the horizontal X direction.

**Arrange from bottom up option**
    When this option is set, the arranging of components will begin from the bottom left corner.
    Otherwise, the default is to start the arrangement from the top left.

**Arrangement on Boards**
    The **Arrange Type** option has the following settings:

    **Matching Widths Horizontally**
        Components are sorted by width and length in descending order. Components of the
        same width will then fill the board horizontally. This can be used for rip cutting when a
        board`s longest dimension is horizontal and cross cutting when the longest dimension is
        vertical.

    **Matching Lengths Vertically**
        Components are sorted by length and width in descending order. The board is then filled
        vertically from top to bottom in columns from left to right with components of the same
        length. This can be used for cross cutting when a board`s longest dimension is horizontal
        and rip cutting when the longest dimension is vertical.

    **Fill Boards Diagonally**
        Components are sorted by length and width in descending order. The board is
        alternately filled horizontally and vertically starting in the top left corner of the boards.
        This should result in the most condensed layout. There is a random aspect to the fill
        pattern and is therefore nice to try when you are looking for another option.

    .. list-table::
        :widths: 8 30 24 30 8

        * -
          -  .. image:: /_static/images/FromTopLayout.png
                :width: 100 %
          -  .. image:: /_static/images/ArrangeText.png
                :width: 100 %
          -  .. image:: /_static/images/FromBottomLayout.png
                :width: 100 %
          -





