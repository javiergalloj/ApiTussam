from lxml import etree
from suds.client import Client


peticion = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)

linea = raw_input("Introduce una linea:")

estadolinea = peticion.service.GetStatusLinea(linea)
estadolinea = etree.fromstring(estadolinea)
estadolinea = estadolinea[0][0]
ns = "{http://tempuri.org/}"
activos = estadolinea.find(ns+'GetStatusLineaResult/'+ns+'activos')
frec_bien = estadolinea.find(ns+'GetStatusLineaResult/'+ns+'frec_bien')
graves = estadolinea.find(ns+'GetStatusLineaResult/'+ns+'graves')

print "Autobuses activos:",activos.text
print "Autobuses bien de frecuencia:",frec_bien.text
print "Incidencias graves:",graves.text