"""
Post Processing Script to create GCODE from X,Y positions of Dot Matrix Images

It should work with Matthew Rayfield's Pixels to Gcode:
https://matthewrayfield.com/tools/pixels-to-gcode/

To work with other tools the find and replace input part must be changed.

Many lines are commented out which are for multi nozzle setup.
"""

#tkinter for file selection
from tkinter import filedialog as fd
filename = fd.askopenfilename()

#start and endcode
startcode = "G28\nG01 X0.0 Y0.0 F3600"
endcode = "\nG01 X55 Y10"

#toolhead offsets
tool0x = 0.0
tool0y = 0.0
# tool1x = 8.0
# tool1y = 0.0
# tool2x = 16.0
# tool2y = 0.0
# tool3x = 24.0
# tool3y = 0.0
# tool4x = 32.0
# tool4y = 0.0
# tool5x = 40.0
# tool5y = 0.0
# tool6x = 48.0
# tool6y = 0.0
# tool7x = 56.0
# tool7y = 0.0
# tool8x = 64.0
# tool8y = 0.0
# tool9x = 72.0
# tool9y = 0.0

#read from file
with open(filename) as infile:
    instr = infile.read()

#find and replace text for the right input format
instr0 = instr.replace("G0 Z1.00 F10000", "")
instr1 = instr0.replace("G0 Z4.00 F10000", "")
instr1.split('\n')
instr2 = [line for line in instr1.split('\n') if line.strip() != '']
instr3 = str(instr2)
instr4 = instr3.replace("G0 X", "")
instr5 = instr4.replace(" Y", ",")
instr6 = instr5.replace(" Z4.00 F10000', '", "\n")
instr7 = instr6.replace("['", "")
instr8 = instr7.replace(" Z4.00 F10000']", "")
instr9 = instr8.replace("\n", ",")
inlist = [line for line in instr9.split(',') if line.strip() != '']
inlist0 =[float(i) for i in inlist]

#read every second value
xfloat = inlist0[0::2]
yfloat = inlist0[1::2]
xyfloat = list(zip(xfloat, yfloat))

#toolrange as float x/y; x alone; y alone
#width = 240 hight = 300
import numpy
hight = (300.0)
tool00range = [(x,y) for x in numpy.arange(0.0, 240.0, 1.0) for y in numpy.arange(hight)]
tool00xrange, tool00yrange = zip(*tool00range)
# tool10range = [(x,y) for x in numpy.arange(8.0, 16.0, 1.0) for y in numpy.arange(hight)]
# tool10xrange, tool10yrange = zip(*tool10range)
# tool20range = [(x,y) for x in numpy.arange(16.0, 24.0, 1.0) for y in numpy.arange(hight)]
# tool20xrange, tool20yrange = zip(*tool20range)
# tool30range = [(x,y) for x in numpy.arange(24.0, 32.0, 1.0) for y in numpy.arange(hight)]
# tool30xrange, tool30yrange = zip(*tool30range)
# tool40range = [(x,y) for x in numpy.arange(32.0, 40.0, 1.0) for y in numpy.arange(hight)]
# tool40xrange, tool40yrange = zip(*tool40range)
# tool50range = [(x,y) for x in numpy.arange(40.0, 48.0, 1.0) for y in numpy.arange(hight)]
# tool50xrange, tool50yrange = zip(*tool50range)
# tool60range = [(x,y) for x in numpy.arange(48.0, 56.0, 1.0) for y in numpy.arange(hight)]
# tool60xrange, tool60yrange = zip(*tool60range)
# tool70range = [(x,y) for x in numpy.arange(56.0, 64.0, 1.0) for y in numpy.arange(hight)]
# tool70xrange, tool70yrange = zip(*tool70range)
# tool80range = [(x,y) for x in numpy.arange(64.0, 72.0, 1.0) for y in numpy.arange(hight)]
# tool80xrange, tool80yrange = zip(*tool80range)
# tool90range = [(x,y) for x in numpy.arange(72.0, 80.0, 1.0) for y in numpy.arange(hight)]
# tool90xrange, tool90yrange = zip(*tool90range)

# tool01range = [(x,y) for x in numpy.arange(80.0, 88.0, 1.0) for y in numpy.arange(hight)]
# tool01xrange, tool01yrange = zip(*tool01range)
# tool11range = [(x,y) for x in numpy.arange(88.0, 96.0, 1.0) for y in numpy.arange(hight)]
# tool11xrange, tool11yrange = zip(*tool11range)
# tool21range = [(x,y) for x in numpy.arange(96.0, 104.0, 1.0) for y in numpy.arange(hight)]
# tool21xrange, tool21yrange = zip(*tool21range)
# tool31range = [(x,y) for x in numpy.arange(104.0, 112.0, 1.0) for y in numpy.arange(hight)]
# tool31xrange, tool31yrange = zip(*tool31range)
# tool41range = [(x,y) for x in numpy.arange(112.0, 120.0, 1.0) for y in numpy.arange(hight)]
# tool41xrange, tool41yrange = zip(*tool41range)
# tool51range = [(x,y) for x in numpy.arange(120.0, 128.0, 1.0) for y in numpy.arange(hight)]
# tool51xrange, tool51yrange = zip(*tool51range)
# tool61range = [(x,y) for x in numpy.arange(128.0, 136.0, 1.0) for y in numpy.arange(hight)]
# tool61xrange, tool61yrange = zip(*tool61range)
# tool71range = [(x,y) for x in numpy.arange(136.0, 144.0, 1.0) for y in numpy.arange(hight)]
# tool71xrange, tool71yrange = zip(*tool71range)
# tool81range = [(x,y) for x in numpy.arange(144.0, 152.0, 1.0) for y in numpy.arange(hight)]
# tool81xrange, tool81yrange = zip(*tool81range)
# tool91range = [(x,y) for x in numpy.arange(152.0, 160.0, 1.0) for y in numpy.arange(hight)]
# tool91xrange, tool91yrange = zip(*tool91range)

# tool02range = [(x,y) for x in numpy.arange(160.0, 168.0, 1.0) for y in numpy.arange(hight)]
# tool02xrange, tool02yrange = zip(*tool02range)
# tool12range = [(x,y) for x in numpy.arange(168.0, 176.0, 1.0) for y in numpy.arange(hight)]
# tool12xrange, tool12yrange = zip(*tool12range)
# tool22range = [(x,y) for x in numpy.arange(176.0, 184.0, 1.0) for y in numpy.arange(hight)]
# tool22xrange, tool22yrange = zip(*tool22range)
# tool32range = [(x,y) for x in numpy.arange(184.0, 192.0, 1.0) for y in numpy.arange(hight)]
# tool32xrange, tool32yrange = zip(*tool32range)
# tool42range = [(x,y) for x in numpy.arange(192.0, 200.0, 1.0) for y in numpy.arange(hight)]
# tool42xrange, tool42yrange = zip(*tool42range)
# tool52range = [(x,y) for x in numpy.arange(200.0, 208.0, 1.0) for y in numpy.arange(hight)]
# tool52xrange, tool52yrange = zip(*tool52range)
# tool62range = [(x,y) for x in numpy.arange(208.0, 216.0, 1.0) for y in numpy.arange(hight)]
# tool62xrange, tool62yrange = zip(*tool62range)
# tool72range = [(x,y) for x in numpy.arange(216.0, 224.0, 1.0) for y in numpy.arange(hight)]
# tool72xrange, tool72yrange = zip(*tool72range)
# tool82range = [(x,y) for x in numpy.arange(224.0, 232.0, 1.0) for y in numpy.arange(hight)]
# tool82xrange, tool82yrange = zip(*tool82range)
# tool92range = [(x,y) for x in numpy.arange(232.0, 240.0, 1.0) for y in numpy.arange(hight)]
# tool92xrange, tool92yrange = zip(*tool92range)

#find coordinates in toolhead ranges
diff00 = list(set(xyfloat) & set(tool00range))
# diff10 = list(set(xyfloat) & set(tool10range))
# diff20 = list(set(xyfloat) & set(tool20range))
# diff30 = list(set(xyfloat) & set(tool30range))
# diff40 = list(set(xyfloat) & set(tool40range))
# diff50 = list(set(xyfloat) & set(tool50range))
# diff60 = list(set(xyfloat) & set(tool60range))
# diff70 = list(set(xyfloat) & set(tool70range))
# diff80 = list(set(xyfloat) & set(tool80range))
# diff90 = list(set(xyfloat) & set(tool90range))

# diff01 = list(set(xyfloat) & set(tool01range))
# diff11 = list(set(xyfloat) & set(tool11range))
# diff21 = list(set(xyfloat) & set(tool21range))
# diff31 = list(set(xyfloat) & set(tool31range))
# diff41 = list(set(xyfloat) & set(tool41range))
# diff51 = list(set(xyfloat) & set(tool51range))
# diff61 = list(set(xyfloat) & set(tool61range))
# diff71 = list(set(xyfloat) & set(tool71range))
# diff81 = list(set(xyfloat) & set(tool81range))
# diff91 = list(set(xyfloat) & set(tool91range))

# diff02 = list(set(xyfloat) & set(tool02range))
# diff12 = list(set(xyfloat) & set(tool12range))
# diff22 = list(set(xyfloat) & set(tool22range))
# diff32 = list(set(xyfloat) & set(tool32range))
# diff42 = list(set(xyfloat) & set(tool42range))
# diff52 = list(set(xyfloat) & set(tool52range))
# diff62 = list(set(xyfloat) & set(tool62range))
# diff72 = list(set(xyfloat) & set(tool72range))
# diff82 = list(set(xyfloat) & set(tool82range))
# diff92 = list(set(xyfloat) & set(tool92range))

#add values to list so that zip() works
#values are toolhead offsets
if len(diff00) == 0:
    diff00 = [((tool0x), (tool0y))]
# if len(diff10) == 0:
    # diff10 = [((tool1x), (tool1y))]
# if len(diff20) == 0:
    # diff20 = [((tool2x), (tool2y))]
# if len(diff30) == 0:
    # diff30 = [((tool3x), (tool3y))]
# if len(diff40) == 0:
    # diff40 = [((tool4x), (tool4y))]
# if len(diff50) == 0:
    # diff50 = [((tool5x), (tool5y))]
# if len(diff60) == 0:
    # diff60 = [((tool6x), (tool6y))]
# if len(diff70) == 0:
    # diff70 = [((tool7x), (tool7y))]
# if len(diff80) == 0:
    # diff80 = [((tool8x), (tool8y))]
# if len(diff90) == 0:
    # diff90 = [((tool9x), (tool9y))]
    
# if len(diff01) == 0:
    # diff01 = [((tool0x), (tool0y))]
# if len(diff11) == 0:
    # diff11 = [((tool1x), (tool1y))]
# if len(diff21) == 0:
    # diff21 = [((tool2x), (tool2y))]
# if len(diff31) == 0:
    # diff31 = [((tool3x), (tool3y))]
# if len(diff41) == 0:
    # diff41 = [((tool4x), (tool4y))]
# if len(diff51) == 0:
    # diff51 = [((tool5x), (tool5y))]
# if len(diff61) == 0:
    # diff61 = [((tool6x), (tool6y))]
# if len(diff71) == 0:
    # diff71 = [((tool7x), (tool7y))]
# if len(diff81) == 0:
    # diff81 = [((tool8x), (tool8y))]
# if len(diff91) == 0:
    # diff91 = [((tool9x), (tool9y))]
    
# if len(diff02) == 0:
    # diff02 = [((tool0x), (tool0y))]
# if len(diff12) == 0:
    # diff12 = [((tool2x), (tool2y))]
# if len(diff22) == 0:
    # diff22 = [((tool2x), (tool2y))]
# if len(diff32) == 0:
    # diff32 = [((tool3x), (tool3y))]
# if len(diff42) == 0:
    # diff42 = [((tool4x), (tool4y))]
# if len(diff52) == 0:
    # diff52 = [((tool5x), (tool5y))]
# if len(diff62) == 0:
    # diff62 = [((tool6x), (tool6y))]
# if len(diff72) == 0:
    # diff72 = [((tool7x), (tool7y))]
# if len(diff82) == 0:
    # diff82 = [((tool8x), (tool8y))]
# if len(diff92) == 0:
    # diff92 = [((tool9x), (tool9y))]

#XY values for matplotlib and calculating
diff00x, diff00y = zip(*diff00)
# diff10x, diff10y = zip(*diff10)
# diff20x, diff20y = zip(*diff20)
# diff30x, diff30y = zip(*diff30)
# diff40x, diff40y = zip(*diff40)
# diff50x, diff50y = zip(*diff50)
# diff60x, diff60y = zip(*diff60)
# diff70x, diff70y = zip(*diff70)
# diff80x, diff80y = zip(*diff80)
# diff90x, diff90y = zip(*diff90)

# diff01x, diff01y = zip(*diff01)
# diff11x, diff11y = zip(*diff11)
# diff21x, diff21y = zip(*diff21)
# diff31x, diff31y = zip(*diff31)
# diff41x, diff41y = zip(*diff41)
# diff51x, diff51y = zip(*diff51)
# diff61x, diff61y = zip(*diff61)
# diff71x, diff71y = zip(*diff71)
# diff81x, diff81y = zip(*diff81)
# diff91x, diff91y = zip(*diff91)

# diff02x, diff02y = zip(*diff02)
# diff12x, diff12y = zip(*diff12)
# diff22x, diff22y = zip(*diff22)
# diff32x, diff32y = zip(*diff32)
# diff42x, diff42y = zip(*diff42)
# diff52x, diff52y = zip(*diff52)
# diff62x, diff62y = zip(*diff62)
# diff72x, diff72y = zip(*diff72)
# diff82x, diff82y = zip(*diff82)
# diff92x, diff92y = zip(*diff92)

#find coordinates for finished GCODE
x00offset = [x - tool0x for x in diff00x]
y00offset = [x - tool0y for x in diff00y]      
# x10offset = [x - tool1x for x in diff10x]
# y10offset = [x - tool1y for x in diff10y]
# x20offset = [x - tool2x for x in diff20x]
# y20offset = [x - tool2y for x in diff20y]
# x30offset = [x - tool3x for x in diff30x]
# y30offset = [x - tool3y for x in diff30y]
# x40offset = [x - tool4x for x in diff40x]
# y40offset = [x - tool4y for x in diff40y]
# x50offset = [x - tool5x for x in diff50x]
# y50offset = [x - tool5y for x in diff50y]
# x60offset = [x - tool6x for x in diff60x]
# y60offset = [x - tool6y for x in diff60y]
# x70offset = [x - tool7x for x in diff70x]
# y70offset = [x - tool7y for x in diff70y]
# x80offset = [x - tool8x for x in diff80x]
# y80offset = [x - tool8y for x in diff80y]
# x90offset = [x - tool9x for x in diff90x]
# y90offset = [x - tool9y for x in diff90y]

# x01offset = [x - tool0x for x in diff01x]
# y01offset = [x - tool0y for x in diff01y]      
# x11offset = [x - tool1x for x in diff11x]
# y11offset = [x - tool1y for x in diff11y]
# x21offset = [x - tool2x for x in diff21x]
# y21offset = [x - tool2y for x in diff21y]
# x31offset = [x - tool3x for x in diff31x]
# y31offset = [x - tool3y for x in diff31y]
# x41offset = [x - tool4x for x in diff41x]
# y41offset = [x - tool4y for x in diff41y]
# x51offset = [x - tool5x for x in diff51x]
# y51offset = [x - tool5y for x in diff51y]
# x61offset = [x - tool6x for x in diff61x]
# y61offset = [x - tool6y for x in diff61y]
# x71offset = [x - tool7x for x in diff71x]
# y71offset = [x - tool7y for x in diff71y]
# x81offset = [x - tool8x for x in diff81x]
# y81offset = [x - tool8y for x in diff81y]
# x91offset = [x - tool9x for x in diff91x]
# y91offset = [x - tool9y for x in diff91y]

# x02offset = [x - tool0x for x in diff02x]
# y02offset = [x - tool0y for x in diff02y]      
# x12offset = [x - tool1x for x in diff12x]
# y12offset = [x - tool1y for x in diff12y]
# x22offset = [x - tool2x for x in diff22x]
# y22offset = [x - tool2y for x in diff22y]
# x32offset = [x - tool3x for x in diff32x]
# y32offset = [x - tool3y for x in diff32y]
# x42offset = [x - tool4x for x in diff42x]
# y42offset = [x - tool4y for x in diff42y]
# x52offset = [x - tool5x for x in diff52x]
# y52offset = [x - tool5y for x in diff52y]
# x62offset = [x - tool6x for x in diff62x]
# y62offset = [x - tool6y for x in diff62y]
# x72offset = [x - tool7x for x in diff72x]
# y72offset = [x - tool7y for x in diff72y]
# x82offset = [x - tool8x for x in diff82x]
# y82offset = [x - tool8y for x in diff82y]
# x92offset = [x - tool9x for x in diff92x]
# y92offset = [x - tool9y for x in diff92y]

#add values from second and third pass to values from first pass
#x00offset = x00offset + x01offset + x02offset
# x10offset = x10offset + x11offset + x12offset
# x20offset = x20offset + x21offset + x22offset
# x30offset = x30offset + x31offset + x32offset
# x40offset = x40offset + x41offset + x42offset
# x50offset = x50offset + x51offset + x52offset
# x60offset = x60offset + x61offset + x62offset
# x70offset = x70offset + x71offset + x72offset
# x80offset = x80offset + x81offset + x82offset
# x90offset = x90offset + x91offset + x92offset

# y00offset = y00offset + y01offset + y02offset
# y10offset = y10offset + y11offset + y12offset
# y20offset = y20offset + y21offset + y22offset
# y30offset = y30offset + y31offset + y32offset
# y40offset = y40offset + y41offset + y42offset
# y50offset = y50offset + y51offset + y52offset
# y60offset = y60offset + y61offset + y62offset
# y70offset = y70offset + y71offset + y72offset
# y80offset = y80offset + y81offset + y82offset
# y90offset = y90offset + y91offset + y92offset

#create list with X and Y coordinates
tool0xy = list(zip(x00offset, y00offset))
# tool1xy = list(zip(x10offset, y10offset))
# tool2xy = list(zip(x20offset, y20offset))
# tool3xy = list(zip(x30offset, y30offset))
# tool4xy = list(zip(x40offset, y40offset))
# tool5xy = list(zip(x50offset, y50offset))
# tool6xy = list(zip(x60offset, y60offset))
# tool7xy = list(zip(x70offset, y70offset))
# tool8xy = list(zip(x80offset, y80offset))
# tool9xy = list(zip(x90offset, y90offset))

#convert to dict
tool0string = [i for i in tool0xy]
tool0dict = { i : 1 for i in tool0string }
# tool1string = [i for i in tool1xy]
# tool1dict = { i : 2 for i in tool1string }
# tool2string = [i for i in tool2xy]
# tool2dict = { i : 4 for i in tool2string }
# tool3string = [i for i in tool3xy]
# tool3dict = { i : 8 for i in tool3string }
# tool4string = [i for i in tool4xy]
# tool4dict = { i : 16 for i in tool4string }
# tool5string = [i for i in tool5xy]
# tool5dict = { i : 32 for i in tool5string }
# tool6string = [i for i in tool6xy]
# tool6dict = { i : 64 for i in tool6string }
# tool7string = [i for i in tool7xy]
# tool7dict = { i : 128 for i in tool7string }
# tool8string = [i for i in tool8xy]
# tool8dict = { i : 256 for i in tool8string }
# tool9string = [i for i in tool9xy]
# tool9dict = { i : 512 for i in tool0string }

#merge dicts with same key
from collections import defaultdict
# dd = defaultdict(list)
# for d in (tool0dict, tool1dict, tool2dict, tool3dict, tool4dict, \
          # tool5dict, tool6dict, tool7dict, tool8dict, tool9dict):
    # for key, value in d.items():
        # dd[key].append(value)

#sum of dict values
# dsum = {k: sum(v) for k, v in dd.items()}

#split 16bit int in two halfes
dbyte0 = {k: (v >> 8) & 0xFF for k, v in tool0dict.items()}
dbyte1 =  {k: v & 0xFF for k, v in tool0dict.items()}

#merge dicts with byte0 and byte1
d16bit = defaultdict(list)
for d in (dbyte0, dbyte1):
    for key, value in d.items():
        d16bit[key].append(value)

#convert dict to list
dl = [(k, v) for k, v in d16bit.items()]

#convert bytes to string and add GCODE
dlc = [(x, "M260 A9 M260 B" + str(y[0]), "M260 B" + str(y[1]) + "M260 S1") for x, y in dl]

#list with coordinates only
dv = [i[0] for i in dlc]

#take XY values for virtualization
dvx, dvy = zip(*dv)

#sort list
sortedcoords = sorted(dlc , key=lambda k: [k[0][0], k[0][1]])

#take min and max values
#ymin = min(dvy)
#ymax = max(dvy)

#delete double values
#nodoublesx = list(set(dvx))

#coordinates for raster printing
#raster = [(x,y) for x in nodoublesx for y in numpy.arange(ymin, ymax, 1.0)]

#delete double coordinates
#rasterdiff = [x for x in raster if x not in dv]

#tuple in tuple for right format
#tupleraster = [(x, ) for x in rasterdiff]

#join lists together
#rasterall = dlc + tupleraster
#sraster = sorted(rasterall , key=lambda k: [k[0][0]])

#groupby X coordinates
#from itertools import groupby
#res = [list(v) for i, v in groupby(sraster, lambda x: x[0][0])]

#groupby X coordinates
from itertools import groupby
res = [list(v) for i, v in groupby(sortedcoords, lambda x: x[0][0])]

#separate even and odd passes
evenlist = res[::2]
oddlist = res[1::2]

#reverse odd pass direction
oddreversed = [t[::-1] for t in oddlist]

#merge even and odd passes
finishedlist = list(zip(evenlist, oddreversed))

#convert list to string
dstr = str(finishedlist)

#find and replace text for the right output format
dstr0 = dstr.replace("((", "G01 X")
dstr1 = dstr0.replace("[([", startcode + "\n")
dstr2 = dstr1.replace(")]", "")
dstr3 = dstr2.replace("([", "")
dstr4 = dstr3.replace("', [", "), ")
dstr5 = dstr4.replace("),", "\n")
dstr6 = dstr5.replace("M260 A9", "M260 A9\n")
dstr7 = dstr6.replace("M260 B0", "M260 B0\n")
dstr8 = dstr7.replace("M260 B1", "M260 B1\n")
dstr9 = dstr8.replace(" 'M", "M")
dstr10 = dstr9.replace(" M", "M")
dstr11 = dstr10.replace("',M", "M")
dstr12 = dstr11.replace(" G", "G")
dstr13 = dstr12.replace("'", "")
dstr14 = dstr13.replace(", ", " Y")
dstr15 = dstr14 + endcode

#write to file
f = open(filename[:-6] + "-out" + ".gcode", "w")
f.write(str(dstr15))
f.close()

#plot toolrange and toolhead coordinates with matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(tool00xrange, tool00yrange, s=1, c='0.9')
# ax1.scatter(tool10xrange, tool10yrange, s=1, c='0.8')
# ax1.scatter(tool20xrange, tool20yrange, s=1, c='0.9')
# ax1.scatter(tool30xrange, tool30yrange, s=1, c='0.8')
# ax1.scatter(tool40xrange, tool40yrange, s=1, c='0.9')
# ax1.scatter(tool50xrange, tool50yrange, s=1, c='0.8')
# ax1.scatter(tool60xrange, tool60yrange, s=1, c='0.9')
# ax1.scatter(tool70xrange, tool70yrange, s=1, c='0.8')
# ax1.scatter(tool80xrange, tool80yrange, s=1, c='0.9')
# ax1.scatter(tool90xrange, tool90yrange, s=1, c='0.8')

# ax1.scatter(tool01xrange, tool01yrange, s=1, c='0.9')
# ax1.scatter(tool11xrange, tool11yrange, s=1, c='0.8')
# ax1.scatter(tool21xrange, tool21yrange, s=1, c='0.9')
# ax1.scatter(tool31xrange, tool31yrange, s=1, c='0.8')
# ax1.scatter(tool41xrange, tool41yrange, s=1, c='0.9')
# ax1.scatter(tool51xrange, tool51yrange, s=1, c='0.8')
# ax1.scatter(tool61xrange, tool61yrange, s=1, c='0.9')
# ax1.scatter(tool71xrange, tool71yrange, s=1, c='0.8')
# ax1.scatter(tool81xrange, tool81yrange, s=1, c='0.9')
# ax1.scatter(tool91xrange, tool91yrange, s=1, c='0.8')

# ax1.scatter(tool02xrange, tool02yrange, s=1, c='0.9')
# ax1.scatter(tool12xrange, tool12yrange, s=1, c='0.8')
# ax1.scatter(tool22xrange, tool22yrange, s=1, c='0.9')
# ax1.scatter(tool32xrange, tool32yrange, s=1, c='0.8')
# ax1.scatter(tool42xrange, tool42yrange, s=1, c='0.9')
# ax1.scatter(tool52xrange, tool52yrange, s=1, c='0.8')
# ax1.scatter(tool62xrange, tool62yrange, s=1, c='0.9')
# ax1.scatter(tool72xrange, tool72yrange, s=1, c='0.8')
# ax1.scatter(tool82xrange, tool82yrange, s=1, c='0.9')
# ax1.scatter(tool92xrange, tool92yrange, s=1, c='0.8')

# ax1.scatter(xfloat, yfloat, s=1, c='RED', alpha=0.5)
ax1.scatter(dvx, dvy, s=1, c='BLUE', alpha=0.5)
plt.show()
