
.. _multiple_maps-label:

Creating Multiple Maps
**********************

.. role:: blue-bold

Maps are created under the component :blue-bold:`maps` in the browser tree. With each run of MBP , the
existing visible map is deleted. To prevent a map from being deleted, you can hide it by turning
off the visibility icon. This allows multiple maps to be saved with the model. The default map
name is :blue-bold:`map`, which can be renamed to identify its content, such as material type or an
assembly name.

The additional maps are saved when the model is saved to the Fusion cloud. You can remove a
map by turning on the visibility icon before you rerun MBP . All post-mapping tasks are available
on the saved maps, and changes to each map are saved when the model is saved.

The Manufacturing Model task will create a separate manufacturing model for the map it is
launched on. Rearranged components on the map within or between boards in the design
workspace will be reflected in the created manufacturing model.

You can switch between saved maps using the visibility icon next to each map component.

.. image:: /_static/images/save_map.png
    :width: 35 %
    :align: center

|

An alternative way to create and view different maps is to use Fusion’s Undo list.

With each created map, a single entry is created in the Undo list labeled **Undo MapBoards Pro**.
You can roll back-and-forth through the different maps using commands Undo (Cmd-Z) and
Redo (Shift Cmd-Z), …

.. image:: /_static/images/Undo.png
    :width: 35 %
    :align: center

|

