# NFS FCE Paint Booth
*A Need for Speed III/HS FCE color editor that doesn't suck and then some!*

**Addtional credits to**:	30secondsofcode.org (hex to RGB and RGB to hex snippets) 

Did this as a way to learn a bit of Python and to see if I could cut down on tool usage for colors since all existing tools for it are ass to some degree (NFS Wizard and FCE Finish do not take tolerance values into account so colors aren't displayed accurately AND messed up with your colors upon saving, CarCad is ancient jank and also slightly messed your colors on saving, FCE Converter does save colors properly but the interface is jank and colors aren't displayed properly, FCE Colors is both brilliant -exports colors to a image file and can import said image back; perfect for backing up colors- and maddening -since you're working with an image you can't see colors accurately 'till you do some shenanigans in your image editor and depending of your editor, colors might not be saved accurately either-) 

## Features

Python-based, so it can be run in platforms besides Windows; Python script and standalone Windows application included.
* Supports NFS3 and HS FCE files
* Does the expected FCE color edition features: edit, add, delete and copy color sets.
* HSVT, HTML and color picker-based color selection for precise or convenient color edition.
* Can export and import color tables to and from CSV files, said files are compatible with both FCE versions.
* Displays colors accounting for tolerance values in aim to pursue the best color display accuracy.
* Add a random color set or generate a whole color table of random colors (novelty feature because half the time you get eye-searing combos, but hey, it's worth the flex 💪).

## Requirements

* Python 3 (tested with Python 3.8, 3.10 and 3.13) for script version.

## Installation/Use

* Unzip the NFS_FCEPaintBooth_winExe folder if you're using the Windows standalone app or NFS_FCEPaintBooth.py file if you're using the script version.
* For the Windows standalone app: open the NFS_FCEPaintBooth_winExe folder and run NFS_FCEPaintBooth.exe
* For the Python script version:
  * On Windows:
    * If you have Python 3 as your default Python instance, just double click the NFS_FCEPaintBooth.py file
      *Alternatively, open a Powershell/Command Prompt window in the folder you have the NFS_FCEPaintBooth.py file and type py NFSHS_FedataHFlagEdit.py and press Enter
  * On Linux:
    * Make the NFS_FCEPaintBooth.py file executable by opening a Terminal window in the folder you have the NFS_FCEPaintBooth.py file, then type chmod +x NFSHS_FedataHFlagEdit.py and press Enter
    * If you have Python 3 as your default Python instance, just double click the NFS_FCEPaintBooth.py file
      * Alternatively, open a Terminal window in the folder you have the NFS_FCEPaintBooth.py file and type python3 NFSHS_FedataHFlagEdit.py and press Enter
* You can also edit the colors exported to a CSV file: open up a text editor or a spreadsheet program (e.g. Excel, LibreOffice Calc) to do so
  * The CSV file structure is the following:
    * first row, first digit is the amount of color sets (0-16), don't touch the trailing numbers
      
            8,0,0,0
      
    * the following 16 rows are the color sets, colors in each set are tuples wrapped in quotes, separated in columns by commas. Said columns correspond to primary color, interior color (HS only), secondary color and driver hair color (HS only). Each tuple has 4 values separated by commas, which are hue (scale 0-360), saturation, brightness and tolerance (scale 0-255) respectively
            
            "[0, 255, 128, 129]","[256, 6, 74, 128]","[38, 122, 114, 127]","[42, 190, 70, 127]"

            "[64, 60, 90, 127]","[256, 6, 74, 128]","[52, 2, 26, 127]","[42, 190, 70, 127]"

            ...

    * unused color sets can be left with [0, 0, 0, 0] values for each column
      * if you export a NFS3 color table, FCE Paint Booth will automatically give it interior ([0, 0, 64, 127]) and driver hair ([42, 190, 70, 127]) colors as a convenience feature if you want to import it to a HS FCE
      * if you're using a spreadsheet program remember to save with comma as separator and double quote marks (") as a quote character

## Construction

|Programs used|Known bugs|May be incompatible with|
|------|-----|--|
|IDLE|If you punch in HSVT values, you have to press Tab to trigger changes|MCO FCE files (haven't tested)|
|    |If you punch in HTML values, you have to press Enter to trigger changes (this is by design since HTML to HSV conversion is imprecise and triggers the "changes in file flag")|
