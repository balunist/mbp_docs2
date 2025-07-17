.. _mapreport-label:

Map Report
~~~~~~~~~~

The  **Map Report** task will create an HTML document which will be viewed in
the default browser when the View option is selected. There are a number of
options to customize the report as seen in the image below.

.. image:: /_static/images/mapreport.png
    :width: 40 %
    :align: center

|

For labels both  **Part #** and  **Name** are optional and any combination is
valid. The size controls the combination you select. Sliding the size to the
far left will remove that element of the label. The map will be included with
perimeter, insets or pockets, and cutouts set with selectable colors. Insets
has a  **Grayscale** color which when set will produce a varying grayscale
color, the lighter gray for deeper inset pockets and the darker gray for
shallow inset pockets.

The  **Report Output** option includes the following:

    **View**
        view the report with the default web browser when the report
        generation is complete

    **Print**
        view a printable report with the default web browser print option which
        will allow the creation of a PDF output file or a printout

    **Rotate**
        print option to rotate and scaled boards for improved readability

    **HTML Only**
        generate the report HTML file without viewing in the web browser

    **Group common dimensions**
        compress list by grouping to a single line components with common
        dimensions

    **Use Full Path Name**
        Component names will include the entire unique full path as seen in the
        browser tree


The report will include the following views.

    **Map**
        displays the list of boards and clicking on each board will display an
        image of the corresponding mapped board.

    **Cutlist**
        displays a cut list of components sorted by Board, Width and Length.
        Components with matching width and length on the same board will be
        grouped into a single entry with the appropriate quantity.

    **Materials**
        displays a list of board type and quantities required to manufacture
        the model. A board type is determined as a unique material and
        thickness pairing. The material is either the physical material or the
        material appearance if the **Use Appearance** option has been
        specified when the map was created.

    **Options**
        displays the list of options used by MapBoards Pro to create the map.
        This can be useful when comparing the effect options have on the
        resulting map created. Just save the report with different meaningful
        name.

|



.. _samplereport-label:

Sample Report
~~~~~~~~~~~~~


Use the  **Map**,  **Cutlist**,  **Materials** and  **Options** links to
navigate through the report. The  **Help** link is disabled in this sample
since it displays this help. While viewed in a browser, pages from the report
can be saved to PDF or printed.

View report here `Sample Report <https://icarussoftlandings.com/app/docs/reportsample/>`__

