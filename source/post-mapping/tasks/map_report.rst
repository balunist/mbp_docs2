.. _mapreport-label:

Map Report
**********

The **Map Report** task will create an HTML document which can be viewed in the default
browser when the View option is selected. There are a number of options for customizing the
report as seen in the image below.

.. image:: /_static/images/mapreport.png
    :width: 40 %
    :align: center

|

For labels, both **Part #** and **Name** are optional and valid in any combination. The size controls
the combination you select. Sliding the size to the far left will remove that element from the
label. The map will be included with perimeter, insets or pockets, and cutouts set with
selectable colors. Insets have a **Grayscale** color option which, when set, will produce a varying
grayscale color, using lighter gray for deeper inset pockets and darker gray for shallow inset
pockets.

The **Report Output** options include the following:

    - **View** - view the report with the default web browser when the report generation is
      complete

    - **Print** - view a printable report with the default web browser print option which will
      allow the creation of a PDF output file or a printout

    - **Rotate** - print option to rotate and scale boards for improved readability

    - **HTML Only** - generate the report HTML file without viewing it in the web browser

    - **Group common dimensions** - compress list by grouping components with common

    - **Use Full Path Name** - component names will include their unique full path, as seen in the
      browser tree


The report will include the following views:

    **Map**
        Displays the list of boards. Clicking on each board will display an image of the corresponding
        mapped board.

    **Cutlist**
        Displays a cutlist of components sorted by Board, Width, and Length. Components on the same
        board matching in width and length will be grouped into a single entry with the appropriate
        quantity if **Group common dimensions** option is selected.

    **Materials**
        Displays a list of board types and the quantities required to manufacture the model. A board
        type is a unique material and thickness pairing. The material is either the physical material or
        the material appearance specified in the **Use Appearance** option when the map was created.

    **Options**
        Displays the list of options used by MapBoards Pro to create the map. This can be useful when
        comparing the effects options have on the resulting map. Just save the report with a different
        meaningful name.

|



.. _samplereport-label:

Sample Report
=============


Use the  **Map**,  **Cutlist**,  **Materials** and  **Options** links to
navigate through the report. The  **Help** link is disabled in this sample
since it displays this help. While viewed in a browser, pages from the report
can be saved to PDF or printed.

View report here `Sample Report <https://icarussoftlandings.com/app/docs/reportsample/>`__

