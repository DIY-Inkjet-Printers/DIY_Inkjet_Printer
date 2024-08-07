
<br/>

<div align = center >

<pre>

<h1>DIY Inkjet Printer</h1>
<i>An open source inkjet printer built</i> 
<i>without industrial manufacturing.</i>

</pre>

<br/>

[![Button Videos]][Videos]   
[![Button Hackaday]][Hackaday]      
[![Button Frame]][Frame]   
[![Button Pump]][Pump]   
[![Button Head]][Head]      
[![Button Firmware]][Firmware]   
[![Button GCode]][GCode]

<br/>

[<img width = 100% src = './Resources/Cover.webp' >][#]

<br/>

</div>

## Printing

*Possible ways to print with toolhead.*

<br>

<kbd> <br>   $\huge\texttt{\textcolor[RGB]{64,64,64}{𝗚}\textcolor[RGB]{86,86,86}{𝗿}\textcolor[RGB]{99,99,99}{𝗮}\textcolor[RGB]{116,116,116}{𝘆}\textcolor[RGB]{137,137,137}{𝘀}\textcolor[RGB]{157,157,157}{𝗰}\textcolor[RGB]{171,171,171}{𝗮}\textcolor[RGB]{192,192,192}{𝗹}\textcolor[RGB]{220,220,220}{𝗲}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor{Red}{𝗥}\textcolor{Green}{𝗚}\textcolor{Blue}{𝗕}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor[RGB]{0,147,211}{𝗖}\textcolor[RGB]{204,0,147}{𝗠}\textcolor[RGB]{255,241,12}{𝗬}\textcolor[RGB]{220,220,220}{𝗞}}$   <br> </kbd>

<br>
<br>

## Applications

*The printhead could be used as an add-on for*

<br>

<kbd> <br>   $\huge\texttt{\textcolor[RGB]{0,147,211}{𝗗𝗼𝘁 𝗠𝗮𝘁𝗿𝗶𝘅 𝗜𝗺𝗮𝗴𝗲𝘀}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor[RGB]{0,147,211}{𝗣𝗮𝗿𝘁 𝗟𝗮𝗯𝗲𝗹𝗶𝗻𝗴}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor[RGB]{0,147,211}{𝗕𝗶𝗻𝗱𝗲𝗿 𝗝𝗲𝘁}}$   <br> </kbd>

<kbd> <br>   $\huge\texttt{\textcolor[RGB]{85,170,0}{𝗣𝗿𝗶𝗻𝘁𝗶𝗻𝗴 𝗼𝗻 𝗙𝗼𝗼𝗱}}$   <br> </kbd>   
<kbd> <br>   $\huge\texttt{\textcolor[RGB]{85,170,0}{𝗕𝗶𝗼 𝗣𝗿𝗶𝗻𝘁𝗶𝗻𝗴}}$   <br> </kbd>

<br>

$\texttt{\textcolor[RGB]{85,170,0}{＊}}$ *Components cannot be printed out of SLA resin and seals / connections*  
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
and was able to print - if everything was aligned perfectly -  
with black ink made from thinned out paint.

Afterwards I designed a printhead with internal channels  
that could flush out the air through the inbuilt nozzles and  
printed it using a SLA 3D printer.

<br>

After some testing and creating single / multi printhead  
builds I wanted to try printing in four colors, that is $\texttt{\textcolor[RGB]{0,147,211}{𝗖}\textcolor[RGB]{204,0,147}{𝗠}\textcolor[RGB]{255,241,12}{𝗬}\textcolor[RGB]{220,220,220}{𝗞}}$.

While I designed all the required parts, I never got around  
to assembling or even trying them out until I attempted to  
write the **[Hackaday]** building instructions.

<br>

At the time I decided to redesigned the project to fit on  
an **[Ender 3]**, this however also made me realize that the  
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

[#]: #

[Firmware]: Documentation/Firmware
[Videos]: Documentation/Videos.md
[Frame]: Documentation/Machine%20Frame
[GCode]: Documentation/GCode
[Pump]: Documentation/Piezeo%20Pump
[Head]: Documentation/Printhead


[Hackaday]: https://hackaday.io/project/167446-diy-inkjet-printer
[Ender 3]: https://www.creality.com/products/ender-3-3d-printer
[Forum]: https://reprap.org/forum/read.php?153,52959,page=1
[Wiki]: https://reprap.org/wiki/Reprappable-inkjet


<!---------------------------------[ Buttons ]--------------------------------->

[Button Hackaday]: https://img.shields.io/badge/Hackaday-161b22?style=for-the-badge&logoColor=white&logo=Hackaday
[Button Videos]: https://img.shields.io/badge/Videos-DA1F26?style=for-the-badge&logoColor=white&logo=YouTube

[Button Firmware]: https://img.shields.io/badge/Firmware-319795?style=for-the-badge
[Button GCode]: https://img.shields.io/badge/GCode-8669AE?style=for-the-badge
[Button Frame]: https://img.shields.io/badge/Frame-6E6E6E?style=for-the-badge
[Button Head]: https://img.shields.io/badge/Head-CD9834?style=for-the-badge
[Button Pump]: https://img.shields.io/badge/Pump-00A1D6?style=for-the-badge
