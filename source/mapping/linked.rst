.. _linked-label:

Linked Assemblies
*****************

    In Fusion 360, linked components and assemblies are used to manage complex designs
    efficiently, allowing for reusable parts and streamlined workflows. Linked components enable
    modifications to be reflected across multiple instances, while assemblies provide a structured
    way to organize and manage interconnected parts.

    Creating Hybrid models and linking in external components and assemblies is Fusion's legacy 
    method for supporting a Bottom-Up design approach.  The new design types, Part and Assembly,
    provide an easier, more efficient and less error-prone way of managing designs.

    If you encounter issues with linked components or assemblies, you have a couple of options:

    - Break the one or more links in the model that MBP is being run on then
      rerun MBP (the easiest)

    - Or, derive a shadow model and run MBP on that derived model. See
      :ref:`Creating derived model <derived-label>` for details.

.. note::
    - The model containing linked components or assemblies must be a saved model, and
      not an unsaved “Untitled” model when running MBP.
    

