
.. _creatingmultiplemaps-label:

.. toctree::
   :maxdepth: 2

Creating Multiple Maps
======================

.. role:: blue-bold

Maps are created under the component :blue-bold:`maps` in the browser tree.
With each run of MBP the existing visible map is deleted. You can hide a map to prevent it 
from being deleted by turning off the visibility icon allowing multiple maps to be saved 
with the model. The default map name is :blue-bold:`map` which can be rename to identify it's content, 
i.e. a material type or an assembly name.

The additional maps are saved when the model is saved. You can remove a map by turning on the 
visibility icon before you rerun MBP. All post-mapping tasks are available on the saved maps 
and changes to each map are saved when the model is saved.  

A new Manufacturing Model task will create a separate manufacturing model for the map it is launched on.
Rearranging components on the map within or between boards will be reflected in the created manufacturing model.

You can switched between saved maps using the visibility icon next to each map component.

|    

.. image:: /_static/images/savemap.png
    :width: 40 %
    :align: center 

|

An alternate way to create and view different maps is to use Fusion's Undo list.

With each created map a single entry is created in the Undo list, **Undo MapBoards Pro**.   
You can roll back-and-forth through the different maps by doing an Undo (Cmd-Z), Redo (Shift Cmd-Z), ...

|

.. image:: /_static/images/Undo.png
    :width: 40 %
    :align: center

|




    

