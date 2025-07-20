About MapBoards Pro
*******************

MapBoards Pro is a Fusion 360 Plug-In which focuses on preparing your model for
manufacturing.

The goal of this section is to give you a quick overview of what
MapBoards Pro is and how you might use it.

MapBoards Pro (MBP) will create a map which is the arrangement of component
bodies in a model on one or more boards or layout. The arrangement is done
with copies of the bodies leaving the model intact. Placement of the bodies
is based on a tight rectangular bounding box for the bodies. This provides
quick results and reasonable nesting.

When executing MBP the default option for Map Output Type is Component Bodies
which will arrange copies of the bodies in your model onto one or more boards
matching the material type and thickness.

The map layout can be customized to match your preference or manufacturing
requirements then saved as default. See :ref:`map_layout-label` for details.

Try something simple… Select a simple design at first with only a few
components to become familiar with the options available. When you launch MBP
it will evaluate your model and display a list of material types (material type
and thickness). The first time a material type is encountered it will provide
the minimum Width and Length which will fit the largest part of that type. You
can provide default dimensions you prefer and it will remember and use those
dimensions the next time this material type is encountered.

Creating a map with bodies results in a single entry in the UnDo list, UnDo
MapBoards Pro. This enables you to run MBP multiple times creating maps with
different options and roll back-and-forth through the different maps by doing
an UnDo (Cmd-Z), ReDo (Shift Cmd-Z), …

One or more maps are created under the component maps. In order to save a map
you just need to hide it by turning of the visibility icon. See
:ref:`multiple_maps-label` for details.

If you are using or plan to include linked components and assemblies in your
model than see :ref:`linked-label` for details.

You can display all parts found for a material type with their dimensions by
selecting a material type in the list. See :ref:`selection-label` for details.

The dimensions you enter on the lumber tab represent the default boards size
that will be used when mapping. Once you become familiar with creating maps
you may want to use :ref:`material_management-label` to create and manage a
list of board sizes available for each material type which can be shared across
multiple design projects.

Don't worry, MBP will not modify your model. The map created is a separate
component named map found in the browser tree at the root which is cleared with
each run of MBP. You can remove the map by pressing Cmd-Z (UnDo MapBoards Pro)
or rerun MBP and pressing ESC then OK to delete.

Experiment with the following option to get the results you desire.
  - :ref:`arrange_type-label` - choose from 3 optional arrangement types
  - :ref:`rotate-label` - permit 90 degree component rotation for best fit
  - :ref:`selection-label` - selected components can be rotated or duplicated

For a complete list of options with descriptions see :ref:`options-label`. You
can also reference this options list from the context tree.

Introduction Video
==================

For an overview of MapBoards Pro features and options watch this video which
is old and missing many enhancements but useful.

.. raw:: html

    <iframe width="800" height="650" src="https://www.youtube.com/embed/BmuxxvIU2XA"></iframe>

.. leave out for not
  .. note::
    The terms Occurrence, Component, Component Body, Body and Parts are used
    interchangeably throughout this document are generally referring to one or
    more 3D bodies found in your model.

