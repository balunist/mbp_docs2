.. _overview-label:

Overview
========

MapBoards Pro (MBP) will create a map which is the arrangement of component bodies 
in a model on one or more boards or layout. The arrangement is done with 
copies of the bodies leaving the model intact. Placement of the bodies
is based on a tight rectangular bounding box for the bodies.  This provides
quick results and reasonable nesting.

When executing MBP the default option for **Map Output Type** is 
**Component Bodies** which will arrange copies of the bodies in your 
model onto one or more boards matching the material type and thickness.

The map layout can be customized to match your preference or manufacturing 
requirements then saved as default. See :ref:`choosingmaplayout-label` for details.
    
**Try something simple...**
Select a simple design at first with only a few components to become familiar with the 
options available.  When you launch MBP it will evaluate your model and display a list
of material types (material type and thickness).  The first time a material type is 
encountered it will provide the minimum Width and Length which will fit the largest
part of that type.  You can provide default dimensions you prefer and it will remember
and use those dimensions the next time this material type is encountered.

Creating a map with bodies results in a single entry in the UnDo list, **UnDo MapBoards Pro**.
This enables you to run MBP multiple times creating maps with different options and roll back-and-forth 
through the different maps by doing an UnDo (Cmd-Z), ReDo (Shift Cmd-Z), ...

One or more maps are created under the component **maps**.  In order to save a map you 
just need to hide it by turning of the visibility icon.
See :ref:`creatingmultiplemaps-label` for details.
    
If you are using or plan to include linked components and assemblies in your model than 
see :ref:`linked-label` for details. 
        
You can display all parts found for a material type with their dimensions by selecting
a material type in the list.  See :ref:`selection-label` for details.

The dimensions you enter represent the default boards size that will be used when mapping.  
Once you become familiar with creating maps you may want to use :ref:`materialmgt-label` 
to create and manage a list of board sizes available for each material type which can be 
shared across multiple design projects.

Don't worry, MBP will **not** modify your model.  The map created is a separate 
component named **map** found in the browser tree at the root which is cleared with each 
run of MBP.  You can remove the map by pressing Cmd-Z (UnDo MapBoards Pro) or rerun MBP and 
pressing ESC then OK to delete.

Experiment with the following option to get the results you desire.
- Arrange method  - :ref:`arrangetype-label`
- Allow rotation  - :ref:`rotate-label`
- Select components to rotate or duplicate - :ref:`selection-label`

Exporting the created map
--------------------------

There are several alternative **Map Output Type** options that will export the created 
map in one step finishing without leaving the map in the model.  This include DXF file, SVG files or Report 
Output.  You may however wish to keep the map in order to use it in the Fusion's manufacturing workspace to
create toolpaths to produce your model.  The same exports can be done after the map has been created.
This allow the model to be rearranged if desired before an export is performed. 
        
There are a number of post-mapping tasks that can be performed on the created map object.  It is
more efficient and recommended to create the map first then execute tasks on that map.  
The tasks available include labeling, exports of SVG, DXF, Cutlist, Report and the recently added
Manufacturing Model.  A description of the tasks can be found here. 
:ref:`tasks-label`
Be sure to try the Report task which will create an html file that includes a view of the map, 
cut-list, required materials and the MBP options selected to create the map.  Report also provides 
an output type Print which allows the report to be saved as a PDF or even rotate boards for better viewing.</p>

There are a number of options available in the Options tab.  See  `Options <https://icarussoftlandings.com/app/options/mapboardspro/>`__ 
            
Notes:
    - The arrangements accounts for the amount of **component spacing** and **trim on board** 
      specified in options.  Minimize their size for tighter arrangements.
    - You can move components within or between boards in the resulting arranged map.
      :ref:`rearrangemap-label` 
    - Rearranged maps can be relabeled or exported with the Post-Mapping tasks

**Fusion 360 additive manufacturing** 

Using Fusion 360's additive manufacturing is now made easy with the addition of the post-mapping 
task **Manufacturing Model**.  This task will create or switch to an existing
manufacturing model (MM) with setup.  Using a MM provides the convenience of shadowing any changes
made to a mapped board in the design workspace.   

If you plan to use the Fusion additive manufacturing workspace to complete the cutting with 
a CNC Router the following steps are suggested for a starting point.  I would also 
suggest to always try the default options for toolpaths with simulation first.

- Create a map with a Map Output Type of Component Bodies and the option Create boards 
  **As Glass** turned off
- Right-click on the map object in the browser tree and execute the **Manufacturing Model** task
- Check the **Create Setup** and an **WCS Origin** that matches you CNC 
  machine setup then press OK
- Create one or more toolpaths then simulate to validate

Note: For simple body cutouts the 2D Contour toolpath is a good choice.
See :ref:`mfgmodel-label` which shows how to create this toolpath using the default setup created 
by the Manufacturing Model task.    

For an overview of MapBoards Pro features and options watch this video.  It is old and missing many 
enhancements but still useful in providing a general idea of the function provided.

.. raw:: html

    <iframe width="800" height="700" src="https://www.youtube.com/embed/BmuxxvIU2XA"></iframe>        

