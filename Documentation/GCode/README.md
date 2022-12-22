
GCODE Commands
The printer can be controlled by sending values via i2c.

Each set bit represents a printer command like:


0 - everything off

1 - single drop printhead 1

2 - single drop printhead 2

4 - single drop printhead 3

8 - single drop printhead 4

16 - drops at fixed frequency printhead 1

32 - drops at fixed frequency printhead 2

64 - drops at fixed frequency printhead 3

128 - drops at fixed frequency printhead 4

You can change the frequency in the Arduino Sketch


The values can also be added to each other to eject drops from multiple printheads at once like if you send value 15 printhead 1, 2, 3 and 4 eject a drop.

For sending the values you can use the M260 command like:

M260 A9
M260 B1
M260 S1
or
M260 A9
M260 B16
M260 S1
or
M260 A9
M260 B0
M260 S1


If you are using a CAM software for printing along paths you can set the following command for start ejecting drops:

M260 A9
M260 B16
M260 S1
And set the following command for stop ejecting drops:

M260 A9
M260 B0
M260 S1