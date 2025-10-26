About MapBoards Pro
*******************

MapBoards Pro is a Fusion 360 add-in which focuses on preparing your model for
manufacturing.

The goal of this section is to give you a quick overview of what MapBoards Pro is and how you
might use it.

MapBoards Pro (MBP) allows you to create maps, which are arrangements of component bodies
in a model on one or more boards or layouts. The arrangements are done by creating components
containing copies of the bodies in your model, leaving your original model intact. Placement
is based on a tight rectangular bounding box around each body, providing quick results and
reasonable nesting.

The map layout can be customized to match your preferences or manufacturing requirements
then saved as default. See :ref:`map_layout-label` for details.

**Try something simple…** Begin by selecting a simple design with only a few components to
become familiar with the options available. When you launch MBP, it will evaluate your model
and display a list of **board types described by material types and thicknesses**. With each board
type there are two dimensions, width and length, which will be used as the default board size
when creating a map. The first time a material type is encountered these values will be set large
enough to accommodate the largest component of that board type. You can set these
dimensions to be whatever you prefer for that target board size and it will remember and use
those dimensions the next time that material type is encountered.

When executing MBP make sure the option Map Output Type is set to **Component Bodies**,
which is the default. This selection will create and display a map of the components in your
model on their corresponding board types.

Creating a map of component bodies results in a single entry in the UnDo list labeled 
**UnDo MapBoards Pro**. This enables you to run MBP multiple times and create maps with different
options, which you can roll back and forth through using commands UnDo (Cmd-Z) and ReDo
(Shift Cmd-Z).

To Create a map you simply click the OK button. Popup messages will keep you informed of the
progress. When completed one or more mapped boards are displayed in the Top View and the
screen will be resized to view both your model and the created map. The view may be rotated
if there are multiple boards to fill your screen in more of a landscape view.

One or more maps are created under the component **maps**. To save a map, hide it by turning off
the visibility icon. See :ref:`multiple_maps-label` for details.

If you are using or plan to include linked components and assemblies in your model, see 
:ref:`linked-label` for details.

You can display all components of a particular board type with their dimensions by selecting a
board type from the list. See :ref:`selection-label` for details.

The dimensions you enter in the lumber tab represent the default board size that will be used
when mapping. Once you become comfortable creating maps, you may want to use 
:ref:`material_management-label` to create and manage a list of board sizes available for each 
material type, which can be shared across multiple design projects.

Don’t worry, MBP will not modify your model. A map is created as a subcomponent of the
maps component at the root of the browser tree and cleared with each run of MBP . You can
remove the map by pressing Cmd-Z (UnDo MapBoards Pro) or rerunning MBP and pressing ESC
then OK to delete.

Experiment with the following options to get the results you desire:
  - :ref:`arrange_type-label` - choose from 4 optional arrangement types
  - :ref:`rotate-label` - permit 90 degree component rotation for best fit
  - :ref:`selection-label` - selected components can be rotated or duplicated

For a complete list of options with descriptions, see :ref:`options-label`. You can also 
reference this options list from the table of contents.


.. note::
    Unlock the full capabilities of Fusion 360 and MapBoards Pro by adhering to these best practices:

    - Always start by creating a component to house your 3D body and associated
      resources like sketches. Never place 3D bodies directly at the root, outside of
      a component.
    - Include only one body per component.
    - Provide your components with meaningful names, which will help navigate your model
      when it becomes more complicated.


Introduction Videos
===================

Watch this video for an overview of MapBoards Pro features and options, which is a
somewhat outdated but useful introduction.

.. raw:: html

    <iframe width="800" height="650" src="https://www.youtube.com/embed/BmuxxvIU2XA"></iframe>

|

The following video, from Corbin Dunn's YouTube channel
`Corbin's Workshop <https://www.youtube.com/@CorbinDunn>`_, demonstrates a
woodworking project utilizing MapBoards Pro.  The following new features have
been added since this video was created:

  - :ref:`multiple_maps-label` providing full support for multiple maps
  - :ref:`manufacturing_model-label` creates a manufacturing model for a
    selected mapped board with setup

.. raw:: html

    <iframe width="800" height="600" src="https://www.youtube.com/embed/a34LtVAbZdM" frameborder="0" allowfullscreen></iframe>

