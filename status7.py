import numpy as np
import matplotlib.pyplot as plt



#table info
title_text = 'Status 7'
footer_text = ''
fig_background_color = 'white'
fig_border = 'black'

#table config
text_size = 15

#La tabla SIEMPRE elimina la primera fila y columna de data (los 'headers')
#el resto se dibuja sin problemas
#debe ser una matriz. Los datos "vacios" deben ser strings vacios

var_fecha = 'dd mm aa'
var_info_text = 'favor generar boleta (esto es un texto de prueba)'

var_nro_aviso = '3'
var_fecha_rechazo_factura = 'dd mm aa'

var_nombre_proveedor = 'Fabrica Chocolate'
var_monto_factura = 999999
var_monto_oc = 9999999
var_folio_factura = 99999
var_nro_oc = '010101'
var_fecha_factura = 'dd mm aa'
var_fecha_oc = 'dd mm aa'



data =  [
            ['nill','1','2','3'], #nill esta fila no se ve (da el formato)
            ['nill','Nombre Proveedor',var_nombre_proveedor,'',''],
            ['nill','Monto Factura',var_monto_factura,'Monto OC',var_monto_oc],
            ['nill','Folio Factura',var_folio_factura,'N° OC',var_nro_oc],
            ['nill','Fecha Factura',var_fecha_factura,'Fecha OC',var_fecha_oc],

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
plt.figure(linewidth=1,
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
the_table.scale(1, 1.15)
# Hide axes
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# Hide axes border
plt.box(on=None)
# Add title
plt.suptitle(title_text)
# Add footer
#plt.figtext(0.95, 0.05, footer_text, horizontalalignment='right', size=text_size, weight='light')

#plt.figtext(.5,.95,'\nFoo Bar\n', fontsize=18, ha='center')

plt.figtext(.1,.8,'Confirmacion Factura con OC/OS\n' + var_info_text,fontsize=10,ha='left')

plt.figtext(.1,.75,'Fecha: ' + var_fecha,fontsize=10,ha='left')

plt.figtext(.1,.7,'Aviso N°: ' + var_nro_aviso,fontsize=10,ha='left')

plt.figtext(.1,.65,'Fecha de Rechazo de Factura: ' + var_fecha_rechazo_factura,fontsize=10,ha='left')

# Force the figure to update, so backends center objects correctly within the figure.
# Without plt.draw() here, the title will center on the axes and not the figure.
plt.draw()
# Create image. plt.savefig ignores figure edge and face colors, so map them.
fig = plt.gcf()
plt.savefig('status7.png',
            #bbox='tight',
            edgecolor=fig.get_edgecolor(),
            facecolor=fig.get_facecolor(),
            dpi=150
            )