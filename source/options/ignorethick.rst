:orphan:

.. _ignorethick-label:

Ignore Thickness
================

.. role:: blue

This option controls what unique board types are listed in Lumber tab.

When :blue:`Ignore Thickness` is set unique board types are determined using the material type only ignoring 
thickness.  All parts with the same material type or appearance, depending on the :blue:`Use appearance` setting, 
will be mapped to the same board type with a single thickness equal to the thickest of all parts of that material 
type. 

Shown here is a mapped board created with three part with 3 different thicknesses and :blue:`Ignore Thickness`
set.  This example has the :blue:`Create Board as Glass` option set for effect.   

.. image:: /_static/images/ignorethick.png
    :width: 60%
    :align: center
