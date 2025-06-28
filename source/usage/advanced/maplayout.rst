.. _choosingmaplayout-label:

.. toctree::
   :maxdepth: 2

Choosing Map Layout
===================

    There are 12 ways to control the layout of boards in the created map. See image below. 
    The layout you choose may be a decision based on preference or a requirement to match your 
    manufacturing process. The settings you select can be set as defaults by selecting the 
    **Save as Default** button on the options tab.    

**Map Orientation****
    This should be set to match the **Z Up** or **Y Up** orientation of 
    your model. MBP will create the map in what would be the TOP view for the setting you have 
    selected. At the completion of map creation MBP will bring the TOP view into focus facing forward.  
    
**Board Orientation**
    By setting the board dimensions, width and length, you can have the board oriented as portrait or landscape.  
        **Width**  
            - size in the vertical Y direction
        **Length** 
            - size in the horizontal X direction

**Arrange from bottom up option**
    When this option is set the arranging of parts will begin from the bottom left corner. The
    default is to start the arrangement from the top left.

**Arrangement on Boards**
    The following settings are available with the **Arrange Type** option.

    Matching Widths Horizontally
        Component bodies are sorted by width and length in descending order.  
        Bodies of the same width will then fill the board horizontally.
        This can be used for rip cutting when a board`s longest dimension is 
        horizontal and cross cutting when the longest dimension is vertical.
        
    Matching Lengths Vertically
        Component bodies are sorted by length and width in descending order.  
        The board is then filled vertically top to bottom in columns from left to 
        right with bodies of the same length. This can be used for cross 
        cutting when a board`s longest dimension is horizontal and rip cutting 
        when the longest dimension is vertical.
        
    Fill Boards Diagonally
        Component bodies are sorted by length and width in descending order. 
        The board is alternately filled horizontally and vertically starting in 
        the top left corner of the boards. This should result with the most
        condensed layout. There is a random aspect to the fill pattern and 
        is therefore nice to try when you are looking for another option.

    .. list-table::
        :widths: 10 30 20 30 10

        * - 
          -  .. image:: /_static/images/FromTopLayout.png
                :width: 100 %
          -  **--> Arrange from Bottom -->**
          -  .. image:: /_static/images/FromBottomLayout.png
                :width: 100 %
          - 





