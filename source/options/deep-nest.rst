.. _deepnest-label:

Deepnest
========

Deepnest is an open-source nesting application great for laser cutters, plasma cutters,
and other CNC machines. Deepnest packs your components into a compact area to save
material and time. It automatically merges common lines so the laser doesn’t cut the
same path twice. MapBoards Pro can export the maps it creates as SVG file images.

Selecting the **Format for Deepnest** option when exporting an SVG file will enhance the
image for Deepnest in the following ways:

    - The mapped board perimeter will be included separate from any components it
      contains so it can be used with Deepnest as target container
    - Provides the option :ref:`explode_labels-label`, which will include labels in a format recognized
      by Deepnest  

**Note:** If the MBP created map already has labels created, the SVG export will use the
created labels instead of creating new labels or presenting the label options.

If you wish to include component labels and have those labels follow the components
that are rearranged by Deepnest then you need to do the following:

    - Label the map either during map creation or with the post-mapping tasks Label
      Map
    - When you run the post-mapping tasks **Export map to SVG** select the **Explode
      Labels** option  

Deepnest will move the labels with the components when rearranging the mapped board.

    `Getting started with Deepnest <https://deepnest.io/#quickstart>`__
