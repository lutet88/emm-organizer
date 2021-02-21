## hardware code

`rgbController/rgbController.ino`

this is a pretty simple script that uses 6-byte packets to communicate between a microcontroller and USB Serial at 115200 baudrate. commands are outlined at the top of that script.


`RGBController.py`

this script owns two threads (using `threading`), one to communicate with whomever imported it, and one to quickly read from a queue and output that to Serial. it's a pretty dandy script that does what it needs to do. `__connect` is kinda inefficient but it's what you need to keep Serial open.


`PinMapper.py`

this script creates the `PinMap` and `PinMapper` objects, along with some helpful functions to index this simple data structure.


`pinmaps.py`

this script contains all the maps that we used for this project. it's pretty hardware-dependent, so please make your own if you try and replicate this
