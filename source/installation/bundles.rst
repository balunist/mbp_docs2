.. _bundles-label:

.. |update_available| image:: /_static/images/update_available.png
    :height: 3.0ex
    :class: no-scaled-link

Download Bundle
***************

.. role:: blue-bold

Purchased add-in bundles are available to download at the following link.

    `Downloads <https://icarussoftlandings.com/bundle/>`__

When installing on MacOS, see :ref:`MacOS Install <mac_os_bundles-label>`

When installing on Windows, see :ref:`Windows Install <win_bundles-label>`


.. _mac_os_bundles-label:

MacOS Bundle Install Instructions
=================================

After performing the following steps, restart Fusion to activate the add-in.

- Invoke Spotlight using Command-Space bar.
- Type **Terminal** and press Enter.
- Copy & paste the following commands at the Terminal prompt,
  entering your password when prompted:

  .. role:: tiny

  1. First, create the directory (if not already done):
   :tiny:`sudo mkdir -p /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins`

  2. Then, set ownership:
   :tiny:`sudo chown ${USER}:staff /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins`

  3. Set write permissions:
   :tiny:`sudo chmod u+w /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins`

  4. Delete existing bundle folder if it exists:
   :tiny:`rm -rf /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins/MapBoardsPro.bundle`

  5. Unzip the downloaded bundle file into the ApplicationPlugins folder:
   :tiny:`unzip /Users/${USER}/Downloads/MapBoardsPro_macos.zip -d /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins/`


.. _win_bundles-label:

Windows Bundle Install Instructions
===================================

After performing the following steps, restart Fusion to activate the add-in.


  1. Open File Explorer and navigate to your **Downloads** folder.

  2. Right click on the downloaded zip file and select **Extract All...**, then **Browse**
     to select the following folder:
   :tiny:`..\\Autodesk\\ApplicationPlugins`

  3. If the app bundle folder exists select it, right click and delete it (**Important**).

  4. Make sure the folder **ApplicationPlugins** is selected in the **Folder** input field at the bottom,
     click **Select Folder**, then click **Extract**. 

.. image:: /_static/images/Extract_Target.png
    :width: 40%



