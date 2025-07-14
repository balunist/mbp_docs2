.. _getting_started-label:

.. |horizontal| image:: /_static/images/Horizontal.png
                    :height: 2.5ex
                    :class: no-scaled-link

.. |vertical| image:: /_static/images/Vertical.png
                    :height: 2.5ex
                    :class: no-scaled-link

.. |cube| image:: /_static/images/OrientationCube.png
    :height: 3.5ex
    :class: no-scaled-link


.. role:: blue-bold

.. toctree::
   :maxdepth: 2

===============
Getting Started
===============

MapBoards Pro is a *Fusion 360 Plug-In* which focuses on preparing your model
for manufacturing.

The goal of this section is to give you a quick overview of what MapBoards Pro
is and how you might use it.

.. note::
  The terms Occurrence, Component, Component Body, Body and Parts are used
  interchangeably throughout this document are generally referring to one or
  more 3D bodies found in your model.

Settings
--------

When MapBoards Pro (MBP) is first installed there are defaults settings. When
you invoke MapBoards Pro on a model the Lumber tabs will display a list of
:blue-bold:`Board Types` found in the model.  A board type is the pairing of
material type and board thickness.  Material type is either the physical
material or appearance base on the setting :blue-bold:`Use Appearance` found
on the options tab. The first time MapBoards Pro is invoked on a model the
dimensions will be set large enough to accommodate the largest part of that
material type and the :blue-bold:`Options tab` will reveal these default
settings.  If you make any changes to these default dimensions or settings it
will persist for the next time you invoke MBP on this model.

If you like the current settings to be the default on all models being opened
for the first time you can press the :blue-bold:`Save as Default` button on
the Options tab.  In addition to making the settings on the option tab the
default it will also make the default board type dimensions the default for
the respective board types.

Board Dimensions
----------------

The dimension settings for each board type, Width (vertical Y direction) and
Length (the horizontal X direction) define the default targeted boards
dimensions.  When MBP is run it will create as many boards with these
dimensions to accommodate all the parts matching the board types that are
selected or the entire model when :blue-bold:`Use Entire Model` is selected.

You should match orientation, portrait mode (larger Width) or landscape mode
(larger Length) to match the targeted machine you will be manufacturing your
model on.

Using just these default board dimensions is a good starting point and may be
all you will ever need.  There is however the ability to create multiple
dimensions for a board type.   Using :blue-bold:`Material Management` you can
create a finite list of dimensional boards for each board type that can be
shared across all models.

Board Arrangements
------------------

Board are arranged using one of three available arrangement types using the
:blue-bold:`Arrange Type` option. This allows you to match your needs for rip
cut, cross cut or diagonally which is a bit more random. These arrangements
are :blue-bold:`NOT` true nesting but they are optimal for most users and
performed reasonably fast. The placement is done using a tight bounding box
around each part with options for part spacing and a reserved edge on boards.

Grain Direction
---------------

MBP deals with :blue-bold:`Grain Direction` in a number of ways.  Firstly the
target boards type dimensions include a directional button to toggle between
the vertical Y direction |vertical| or the horizontal X direction
|horizontal|. Besides the board types list on the lumber tab you can also
optionally create and manage stock using :blue-bold:`Material Management`.
These lumber lists also have a selectable grain direction for each board
defined.

When MBP is arranging the parts on a board it will align the long edge of a
part with the targeted board grain direction by default with a few exceptions.

- If the option :ref:`Can Rotate <rotate-label>` is selected a part may have
  it's long edge rotated 90 degrees to the grain direction if it would better
  utilize space or if none of the remaining parts would fix an available space
  with aligned long edge and board grain.

- When the parts being mapped are selected they are displayed in a selection
  table with the option to rotate the selected part. When selected this will
  force the part to be placed 90 degree rotate long edge to board grain
  direction.

- When the :blue-bold:`Automatic Grain Alignment` option is set, parts with a
  3D appearance will have the part 3D grain align with the target board grain.
  When modeling you can rotate the 3D grain as desired and the corresponding
  part will be mapped to the target board aligning it with it's grain.

Modifying Created Map
---------------------

A part can be flipped by selecting then right clicking and selecting
:blue-bold:`Flip` from the context menu. This will flip the part in place
aligning the long edge with the board grain direction.

Modifying the location and rotation of the parts within or between boards can
be done a couple of ways once the map is created.

- Click on the :blue-bold:`Top` face of the orientation cube |cube| in the
  upper right window to align the map facing forward. You can then slide the
  parts to the desired location within or between boards. Rotation is not
  possible using this method.

  or

- Click on the :blue-bold:`Top` face of the orientation cube |cube| then
  select the part you want to move, right click and select Unsurpassed Joint,
  double click on the displayed joint, move and rotate the part to the desired
  location. Then select the part again, right click and select Suppress Joint.

Tasks on Created Map
--------------------

It is recommended that you always create a map with parts first then take
advantage of these post mapping tasks on the created map.  Performing these
post-mapping tasks is more efficient performance wise and provides you with
more options such as working with modified maps as described above.

After creating or modifying a created map you may want to

- Label or re-label the map to align the labeling text with the moved parts.
- Create a report which displays the map, parts list and required material in
  the browser with the :blue-bold:`Show` option.
- Create a Manufacturing Model with setup for one or more created boards to
  continue the with the manufacturing process creating tool paths, simulating
  then exporting the tool paths to drive your machine setup.
- Exporting the created maps as flat panels in either DXF or SVG files to be
  used in other software or machine setups

Multiple Maps
-------------

You may want to create and keep more than one map. Maps are created under the
top level component :blue-bold:`maps` in the browser tree. To create and keep
two or more maps you must first hide the exist map by turning off the
visibility icon before rerunning MBP. Having more than one map allows you to
subdivide you model into separate maps to simplify the manufacturing process.
For example you may want to create a map for each board type. To simplify this
you can use :blue-bold:`Selection Support`. To do this you uncheck the
:blue-bold:`Include Entire Model` and either select the individual part or
branches in the browser tree or just select a board type in the list of board
types. When MBP is run it will only include those selected parts to be mapped.

What's Next
-----------

That is the general overview.  Try things out on some simple models. There is
much more functionality available. You can browse the table of contents in
this document or use the :blue-bold:`Quick Search` option to find a
description of an option or a topic of interest. See
:ref:`Overview <overview-label>` in the Advanced Topics section for more
details.

