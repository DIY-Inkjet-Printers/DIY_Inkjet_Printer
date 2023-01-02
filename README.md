
```math
\definecolor{G1}{RGB}{64,64,64}
\definecolor{G2}{RGB}{86,86,86}
\definecolor{G3}{RGB}{99,99,99}
\definecolor{G4}{RGB}{116,116,116}
\definecolor{G5}{RGB}{137,137,137}
\definecolor{G6}{RGB}{157,157,157}
\definecolor{G7}{RGB}{171,171,171}
\definecolor{G8}{RGB}{192,192,192}
\definecolor{G9}{RGB}{220,220,220}
\definecolor{C}{RGB}{0,147,211}
\definecolor{M}{RGB}{204,0,147}
\definecolor{Y}{RGB}{255,241,12}
\definecolor{K}{RGB}{220,220,220}
\definecolor{Warn}{RGB}{85,170,0}
```

<br>


<div align = center>

<pre>

<h1>DIY Inkjet Printer</h1>
<i>An open source inkjet printer built</i> 
<i>without industrial manufacturing.</i>

</pre>

<br>
<br>

[![Button Videos]][Videos]   
[![Button Hackaday]][Hackaday]

<br>
<br>

</div>

## Printing

*Possible ways to print with toolhead.*

<br>

<kbd> <br>   $\huge\texttt{\textcolor{G1}{𝗚}\textcolor{G2}{𝗿}\textcolor{G3}{𝗮}\textcolor{G4}{𝘆}\textcolor{G5}{𝘀}\textcolor{G6}{𝗰}\textcolor{G7}{𝗮}\textcolor{G8}{𝗹}\textcolor{G9}{𝗲}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor{Red}{𝗥}\textcolor{Green}{𝗚}\textcolor{Blue}{𝗕}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor{C}{𝗖}\textcolor{M}{𝗠}\textcolor{Y}{𝗬}\textcolor{K}{𝗞}}$   <br> </kbd>

<br>
<br>

## Applications

*The printhead could be used as an add-on for*

<br>

<kbd> <br>   $\huge\texttt{\textcolor{C}{𝗗𝗼𝘁 𝗠𝗮𝘁𝗿𝗶𝘅 𝗜𝗺𝗮𝗴𝗲𝘀}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor{C}{𝗣𝗮𝗿𝘁 𝗟𝗮𝗯𝗲𝗹𝗶𝗻𝗴}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor{C}{𝗕𝗶𝗻𝗱𝗲𝗿 𝗝𝗲𝘁}}$   <br> </kbd>

<kbd> <br>   $\huge\texttt{\textcolor{Warn}{𝗣𝗿𝗶𝗻𝘁𝗶𝗻𝗴 𝗼𝗻 𝗙𝗼𝗼𝗱}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor{Warn}{𝗕𝗶𝗼 𝗣𝗿𝗶𝗻𝘁𝗶𝗻𝗴}}$   <br> </kbd>

<br>

$\texttt{\textcolor{Warn}{＊}}$ *Components cannot be printed out of SLA resin and seals / connections have to be carefully chosen if you want them to be food grade.*

<br>
<br>

## Backstory

The printhead is controlled by an Arduino which can be controlled directly via i2c or via GCODE (M260) if you use RAMPS or another board which supports i2c.

This is my attempt to build an open source inkjet printer by myself.

I started this project because I wanted to build a binder jetting 3D printer but could not find any open source inkjet printer designs for this. So I started trying to build one.

The toolhead design is a piezo printhead inspired by https://reprap.org/forum/read.php?153,52959,page=1 and https://reprap.org/wiki/Reprappable-inkjet.


Back in 2019 after reading through the build logs of the Oasis 3DP I was searching on the internet if someone has ever tried to build an inkjet printer from scratch, at home, with simple electronics and without access to industrial production lines.

I found something about that at the Reprap Forum and on thingiverse and tried to build their projects. After successfully building the projects I started the work on this project.

The design goal of the project is to build a piezo inkjet printer from scratch.

The first working build had a PMMA printhead and could if everything was aligned perfectly print with black ink (water + paint color).

After that I started printing the printhead with a SLA 3D printer to be able to create internal channels for flushing the air out of the printhead through the nozzle.

After some testing with it and building single and multi printhead builds I wanted to try printing in four colors or CMYK.

I designed the needed parts for that, but I never tried them out until I recently attempted to write building instructions for that.

For writing the instructions I redesigned the project to fit it on an Ender 3 and while doing that I figured out that the machine was far to unreliable to get it working at all. 

So I had to find a way to make it more reliable.

For that I designed SLA 3D printed piezo pumps instead of the piezo printheads, used MOSFETs and higher voltage for switching the piezos instead of the H bridges and used a vacuum duct to carry away the excess ink that would otherwise block the nozzle with a large ink drop.

With these changes the printer should be ready to do hour long prints whitout failing due to design based problems.

<br>

<!----------------------------------------------------------------------------->

[Videos]: Documentation/Videos.md


[Hackaday]: https://hackaday.io/project/167446-diy-inkjet-printer


<!---------------------------------[ Buttons ]--------------------------------->

[Button Hackaday]: https://img.shields.io/badge/Hackaday-1A1A1A?style=for-the-badge&logoColor=white&logo=Hackaday
[Button Videos]: https://img.shields.io/badge/Videos-DA1F26?style=for-the-badge&logoColor=white&logo=YouTube
