import numpy as np
import matplotlib.pyplot as plt

#table info
title_text = 'Tabla de Pepito'
footer_text = 'June 24, 2020'
fig_background_color = 'skyblue'
fig_border = 'steelblue'

var = 'soy una variable'
var2 = 1234123

#La tabla SIEMPRE elimina la primera fila y columna de data (los 'headers')
#el resto se dibuja sin problemas
#debe ser una matriz. Los datos "vacios" deben ser strings vacios

data =  [
            #['nill','nill','texto de cosa 1','','','',''],
            ['a', var,   75131,  577908,  32015],
            ['hola', 381139,   78045,   99308, 160454],
            [89135,  80552,  var2,  497981, 603535],
            [78415,  81858,  150656,  193263,  69638],
            [139361, 331509,  343164,  781380,  52269],
        ]
# Pop the headers from the data array
column_headers = data.pop(0)
row_headers = [x.pop(0) for x in data]

#Convertir no texto a texto (si fuese necesario)
cell_text = []
for row in data:
    cell_text.append([str(x) for x in row])

# Get some lists of color specs for row and column headers
rcolors = plt.cm.BuPu(np.full(len(row_headers), 0.1))
ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))

# Create the figure.
plt.figure(linewidth=2,
           edgecolor=fig_border,
           facecolor=fig_background_color,
           tight_layout={'pad':1},
           #figsize=(5,3)
          )
# Add a table at the bottom of the axes
the_table = plt.table(
                      cellText=cell_text,
                      #rowLabels=row_headers,
                      #rowColours=rcolors,
                      #rowLoc='right',
                      #colColours=ccolors,
                      #colLabels=column_headers,
                      loc='center')

# Scaling is the only influence we have over top and bottom cell padding.
# Make the rows taller (i.e., make cell y scale larger).
the_table.scale(1, 1.5)
# Hide axes
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# Hide axes border
plt.box(on=None)
# Add title
plt.suptitle(title_text)
# Add footer
plt.figtext(0.95, 0.05, footer_text, horizontalalignment='right', size=6, weight='light')
# Force the figure to update, so backends center objects correctly within the figure.
# Without plt.draw() here, the title will center on the axes and not the figure.
plt.draw()
# Create image. plt.savefig ignores figure edge and face colors, so map them.
fig = plt.gcf()
plt.savefig('pyplot-table-demo.png',
            #bbox='tight',
            edgecolor=fig.get_edgecolor(),
            facecolor=fig.get_facecolor(),
            dpi=150
            )