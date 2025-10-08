.. _installation-label:

.. |running| image:: /_static/images/running.png
    :height: 2.5ex
    :class: no-scaled-link


Installing MapBoards Pro
************************

.. _win_install-label:

Windows Installation
====================

To complete an installation or update of the add-in:

- Verify that you are running the latest Fusion 360 version.
- Run the add-in **Installer** by selecting it in the Downloads directory of File Explorer;
  right-click and select Install.
- With Fusion 360 running, press **Shift-S**, select the Add-Ins tab, find the add-in in the list,
  select it, and press Run.
- Verify that the add-in is running. |running|

.. _mac_os_install-label:

MacOS Installation
==================



To complete an installation or update of the add-in:

- Verify that you are running the latest Fusion 360 version.
- Run the add-in Installer by selecting it in the Downloads directory, right-clicking and
  selecting Open to proceed with the install, following any instructions given by the install
  program.

If an install error occurs then follow the :ref:`Pre-Install Instructions <pre-install-label>` below.

If the install runs without error, restart Fusion and follow these steps to check if
the add-in was successfully installed:

- With Fusion 360 running, press **Shift-S**, select the Add-Ins tab, find the add-in in the list
  and verify that the add-in is running. |running|
- If the installed Add-In is not in the list or it is not running, follow the Pre-Install
  instructions below.

.. _pre-install-label:

Pre-Install Instructions
========================

If installation fails, perform the following steps, then rerun the installer, and activate the
add-in by restarting Fusion:

- Invoke Spotlight using Command-Space bar.
- Type **Terminal** and press Enter.
- Copy & paste the following commands at the Terminal prompt,
  entering your password when prompted:

  .. role:: tiny

  1. First, create the directory (if not already done):
   :tiny:`sudo mkdir -p /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins`

  2. Then, set ownership:
   :tiny:`sudo chown ${USER}:staff /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins`

  3. Finally, set write permissions:
   :tiny:`sudo chmod u+w /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins`


