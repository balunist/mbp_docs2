.. _linked-label:

Linked Assemblies
*****************

    In Fusion 360, linked components and assemblies are used to manage complex designs
    efficiently, allowing for reusable parts and streamlined workflows. Linked components enable
    modifications to be reflected across multiple instances, while assemblies provide a structured
    way to organize and manage interconnected parts.

    Creating models by linking external components and assemblies is how Fusion 360 supports a
    Bottom-Up design approach.

    Models which include **linked** components and assemblies **are** supported. Rare but possible
    limitations exist. If encountered, you will be notified with a popup such as the following:

    .. image:: /_static/images/LinkedError.jpg
        :scale: 40 %
        :align: center

|

    This can be corrected in one of three ways.

    - Break the one or more links in the model that MBP is being run on then
      rerun MBP (the easiest)

    - Or, derive a shadow model and run MBP on that derived model. See
      :ref:`Creating derived model <derived-label>` for details.

    - Or, In the assembly or component being linked to, name all components and do NOT
      use Fusion’s automatic component names, such as Component**XX**. Instead,
      provide your own unique names.

.. note::
    - The model containing linked components or assemblies must be a saved model, and
      not an unsaved “Untitled” model, or the above error will occur.
    - Creating a derived model is quick and easy. If you choose to save that derived model,
      all changes in the source model will be reflected in the derived model, allowing you
      to rerun MBP with changes to the original model.
    - Always ensure that you have removed maps created by MBP from assemblies being
      linked into another model. Clear the maps by first making them visible, turning on
      the visibility icon, then invoking MBP and pressing Cancel.
    - Remember to save any updates you make to the assembly and refresh the model
      where it is linked.

