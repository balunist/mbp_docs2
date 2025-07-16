.. _installation-label:

.. |running| image:: /_static/images/running.png
    :height: 2.5ex
    :class: no-scaled-link


Installing MapBoards Pro
************************

See the following for steps to download the add-in installer.
:ref:`App Store Installers <app_store-label>`

MapBoards Pro is a *Fusion 360 Plug-In* written in Python available for both
Windows and MacOS. The following describes the installation based on the
targeted OS.

.. _win_install-label:

Windows Installation
====================

To complete a new or update install of the add-in:

- Verify that you are running the latest Fusion 360 version
- Run the add-in **Installer** by selecting it in the Downloads directory with
  File Explorer; right-click and selecting Install
- With Fusion 360 running press **Shift-S**, select the Add-Ins tab, find the
  add-in in the list and select it, press Run
- Verify that the add-in is running |running|

.. _mac_os_install-label:

MacOS Installation
==================



To complete a new or update install of the add-in:

- Verify that you are running the latest Fusion 360 version
- Run the add-in Installer by selecting it in the Downloads directory,
  right-click and selecting Open to proceed with the install following the
  instructions.

If an install error occurs then follow the **Pre-Install** instructions below.

If the install runs without error, restart Fusion then check if the Add-In was
successfully installed by doing the following.

- With Fusion 360 running press **Shift-S**, select the Add-Ins tab, find the
  add-in in the list and verify that the add-in is running |running|
- If the installed Add-In is not in the list or it is not running then follow
  the Pre-Install instructions below.

=============== Pre-Install - if Installer fails =================

Perform the following steps then rerun the installer. Then activate the add-in
by restarting Fusion.

- press Command-Space bar, to invoke Spotlight
- type **Terminal** and press return
- Copy & Paste the following two commands at the Terminal prompt pressing
  Enter after each command.  Type your password and enter when prompted.

   .. role:: tiny

   :tiny:`sudo mkdir -p ${USER}:staff /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins`

   :tiny:`sudo chmod u+w /Users/${USER}/Library/\'Application Support\'/Autodesk/ApplicationPlugins`
