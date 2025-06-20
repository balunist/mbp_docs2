.. _selection-label:

.. toctree::
   :maxdepth: 2

Selection Support
=================

    By default all component bodies are included in the created map. Alternatively 
    you can select which component bodies that you want included in the map. 

    Once MapBoard Pro is running select one or more component occurrences or a component bodies 
    from the browser tree or select bodies in the design view. The selected parts will be displayed in 
    a second selection table below the board types list. 

    The selections made are remenbered between invocations of MBP. This includes all related 
    options, quantity and rotation. 
    
    The following example shows two components selected of type Walnut allowing their quantities and grain direction to be 
    changed while still allowing the entire model to be included in the created map. 

    .. image:: /_static/images/Selection.png
        :width: 80 %
        :align: center

|

    In addition you can select a material from the list of board material types presented by MBP. The 
    following image shows the material type Mahogany selected adding 2 addition parts to the previous selection for a total of
    4 selected parts. All selected parts are highlighted in the model.  
|

    .. image:: /_static/images/SelectMaterial.png
        :Width: 80 %
        :align: center

|

    The following options are available when parts have been selected which have an affect when the map 
    is created.
    
        - **Include Entire Model** - When enabled then include all components in model along with 
          modifications made to the selected items. When disabled only the selected components 
          are included.
        - **Quantity** - The selected item's number of copies can be increased from the default of 
          one. Set quantity to zero to omit a part.
        - **Rotate** - When selected the component's grain will be rotated 90 degrees with respect 
          with the targeted board's grain direction. The component grain direction is determined by 
          either the longest dimension or the visual grain if a 3D appearance has been applied and 
          the Automatic Grain Alignment option is enabled. 

