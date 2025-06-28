.. |edit_button| image:: /_static/images/edit_button.png
    :height: 2.5ex
    :class: no-scaled-link

.. _materialmgt-label:

.. toctree::
   :maxdepth: 2

Material Management
===================
    The lumber tab presents a list of materials and their thicknesses seen in the model. With each material type 
    you should provide a Width and Length to be used as the default size when mapping.

    .. image:: /_static/images/edit_scraps.png
        :width: 80 %
        :align: center

|

    **Optionally**, you can create and manage an inventory list of alternate board sizes to be used 
    **before** the default size is used. To create the inventory, select the edit button |edit_button|
    next to the material type under the title **Stock**.       
    
    .. image:: /_static/images/scrap_list.png
        :width: 80 %
        :align: center

|

    The material list you create has the following properties:
        - defines the inventory of this material type that can be used across multiple models
        - can be commercially available board sizes you have or plan to use
        - can be scraps and offcuts of various sizes
        - defines the order material will be used, smallest first is recommended
        - defines a finite number of boards to be used before an infinite number of default size boards


