.. _arrange_type-label:

Arrange Type
============

.. role:: blue-bold

**Matching Widths Horizontally**
    Component bodies are sorted by width and length in descending order. Bodies of the
    same width will then fill the board horizontally. This can be used for rip cutting when a
    board`s longest dimension is horizontal and cross cutting when the longest dimension is
    vertical.

**Matching Lengths Vertically**
    Component bodies are sorted by length and width in descending order. The board is
    then filled vertically and top to bottom in columns from left to right with bodies of the
    same length. This can be used for cross cutting when a board`s longest dimension is
    horizontal and rip cutting when the longest dimension is vertical.

**Fill Boards Diagonally**
    Component bodies are sorted by length and width in descending order. The board is
    alternately filled horizontally and vertically, starting in the top left corner of the boards.
    This should produce the most condensed layout. There is a random aspect to the fill
    pattern and is therefore nice to try when you are looking for another option.

**Arrange using True Shapes of components (Plus version only)**
    Component bodies are arranged using Fusion 360's native arrange functionality to perform true
    nesting of components on boards. This option provides full rotation, part-on-part and the
    largest face down for the best possible material utilization. 


    .. note::
        - Component placement starts from the lower left corner of the board.  
        - Unlike the other arrangement types, grain direction is not considered when using this option.
        - Joints are not used therefore rearranging can be done using the native Fusion move command
        - If you wish to flip a component you can do so by using the post-mapping task 
          :blue-bold:`Rearrange Boards` 
