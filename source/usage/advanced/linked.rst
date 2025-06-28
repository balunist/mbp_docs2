.. _linked-label:

Linked Assemblies
=================

    Models which include **linked** components and assemblies **are** supported. A rare but possible 
    limitations exist. If encountered you will be notified with a popup such as the following.

    .. image:: /_static/images/LinkedError.jpg
        :scale: 40 %
        :align: center

|

    This can be corrected in one of three ways.

    - Break the one or more links in the model that MBP is being run on then rerun MBP (the easiest)
    - or Derive a shadow model then run MBP on that derived model  See :ref:`Creating derived model <derived-label>` 
      for details.
    - or In the assembly or component being linked to, name all component and do NOT use Fusion's 
      automatically created component names, i.e. Component**XX**.  Instead 
      provide your own unique names.

.. note::
    - The model containing a linked component or assembly must be a saved model and not an unsaved 
      "Untitled" model or the above error will occur when creating a map with MBP
    - Creating a derived model is quick and easy and if you choose to save that derived model 
      all changes in the source model will be reflected in the derived model allowing 
      you to rerun MBP with changes to the original model.
    - Always ensure that you have removed maps created by MBP from assemblies being linked into 
      another model. Clear the maps by first making them visible, turning on the visibility icon, then 
      invoking MBP and pressing Cancel.
    - Remember to save any updates you make to the assembly and refresh the model where it is linked.

