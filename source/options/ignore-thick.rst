.. _ignore_thick-label:

Ignore Thickness
================

.. role:: blue

This option controls which unique board types are listed in the Lumber tab.

When :blue:`Ignore Thickness` is set, unique board types are determined using the material
type only, ignoring thickness. All components with the same material type or
appearance, depending on the :blue:`Use Appearance` setting, will be mapped to the same
board type with a single thickness equal to the thickest component of that material type.

Shown here is a mapped board created with three components of the same material
type, with 3 different thicknesses, and :blue:`Ignore Thickness` set. This example has the 
:blue:`Create Board as Glass` option set for effect.

.. image:: /_static/images/ignorethick.png
    :width: 40%
    :align: center

|


