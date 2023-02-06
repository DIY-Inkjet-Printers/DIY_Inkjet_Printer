
# GCode

The printhead can be controlled by sending  
flag bytes over I2C with the help of GCode.

<br>
<br>

## Flag Bytes

The flags are sent as 1 byte codes  
with the following composition:

<br>

<table>
    <tr align = center >
        <th>7</th><th>6</th><th>5</th><th>4</th>
        <th>3</th><th>2</th><th>1</th><th>0</th>
    </tr>
    <tr align = center >
        <td colspan = 4 > Drop At Fixed <br> Frequency </td>
        <td colspan = 4 > Dispense <br> One Drop</td>
    </tr>
</table>

<br>

*The drop frequency can be adjusted in the Arduino firmware.*

<br>
<br>

## Commands

Using the **[M260]** GCode command,  
I2C data can be sent as shown below:

<br>

```gcode
M260 A< Bus Address >
M260 B< Data >
M260 S< Flush >
```

<br>

```gcode
M260 A9  ; Arduino address
M260 B15 ; Dispense a single drop on printhead 1 - 4
M260 S1  ; Flush the buffer
```

<br>


<!----------------------------------------------------------------------------->

[M260]: https://marlinfw.org/docs/gcode/M260.html