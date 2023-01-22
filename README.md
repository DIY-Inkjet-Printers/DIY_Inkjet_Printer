
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

$\texttt{\textcolor{Warn}{＊}}$ *Components cannot be printed out of SLA resin and seals / connections*  
      *have to be carefully chosen if you want them to be food grade.*

<br>
<br>

## Backstory

This is my attempt to build an open source inkjet printer by myself.

I started this project because I wanted to build a binder jetting 3D  
printer but couldn't find any open source inkjet printer designs.

<br>

Back in 2019 after reading through the build logs  
of the Oasis 3D printer I was scouring the internet  
for anyone's attempt to build an inkjet printer:

-   Without access to industrial production

-   With simple electronics 

-   From scratch

-   At home

<br>

After I successfully built some projects I found on the  
**Reprap** **[Forum]** & **[Wiki]** I started to work on my own.

<br>

The first working prototype I built had a PMMA printhead  
and print - if everything was aligned perfectly - with black  
ink made from thinned out paint.

After that I designed a printhead with internal channels  
that could flush out the air through the nozzles and be  
produced with a SLA 3D printer.

<br>

After some testing and creating single / multi printhead  
builds I wanted to try printing in four colors, that is CMYK.

While I designed all the required parts, I never got around  
to assembling or even trying them out until I attempted to  
write the **[Hackaday]** building instructions.

<br>

At the time I decided to redesigned the project to fit on  
an Ender 3, this however also made me realize that the  
machine was far too unreliable.

<br>

To remedy this, I changed the following:

-   Designed SLA 3D printed piezo pumps  
    to replace the piezo printheads

-   Used MOSFETs + higher voltage for  
    switching the piezos instead of H-Bridges

-   Used a vacuum duct to carry away excess  
    ink that would otherwise block the nozzle  
    with large ink drops.

<br>

With these changes the printer should be ready to do hour  
long prints without failing due to design based problems.

<br>

<!----------------------------------------------------------------------------->

[Videos]: Documentation/Videos.md


[Hackaday]: https://hackaday.io/project/167446-diy-inkjet-printer
[Forum]: https://reprap.org/forum/read.php?153,52959,page=1
[Wiki]: https://reprap.org/wiki/Reprappable-inkjet


<!---------------------------------[ Buttons ]--------------------------------->

[Button Hackaday]: https://img.shields.io/badge/Hackaday-1A1A1A?style=for-the-badge&logoColor=white&logo=Hackaday
[Button Videos]: https://img.shields.io/badge/Videos-DA1F26?style=for-the-badge&logoColor=white&logo=YouTube
