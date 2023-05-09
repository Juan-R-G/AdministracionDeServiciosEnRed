# Roldan-Gomez-Juan
import rrdtool


def grafica(filename, time_start, time_end, title, unit, var, db, op, name):  # Reporte de Contabilidac
    try:
        rrdtool.graph(filename, "--start", str(time_start), "--end", str(time_end),
                      "--vertical-label=" + unit, "--title=" + title,
                      "DEF:variable=" + db + ":" + var + ":AVERAGE",
                      "CDEF:escala=variable" + op,
                      "LINE3:escala#0000FF:" + name)
        return "OK"
    except Exception as e:
        print(e)
        return "Error al generar la grafica: " + e.args[0]


def grafica1(filename, time_start, time_end, title, db, umbral, color):  # Uso del Procesador 1
    try:
        rrdtool.graph(filename, "--start", str(time_start), "--end", str(time_end),
                      "--vertical-label=Porcentaje", "--lower-limit", "0", "--upper-limit", "100",
                      "--title=Uso del CPU 1 " + title + " - " + umbral + " %",
                      "DEF:var=" + db + ":procLoad:AVERAGE",
                      "VDEF:var1=var,MAXIMUM",
                      "VDEF:var2=var,MINIMUM",
                      "VDEF:var3=var,AVERAGE",
                      "VDEF:var4=var,STDEV",
                      "CDEF:var5=var," + umbral + ",GT,var,0,IF",
                      "AREA:var#0000FF:CPU 1",
                      "AREA:var5#" + color + ":Umbral Sobrepasado",
                      "GPRINT:var1:%6.2lf %SMAX",
                      "GPRINT:var2:%6.2lf %SMIN",
                      "GPRINT:var3:%6.2lf %SAVG",
                      "GPRINT:var4:%6.2lf %SSTDEV")
        return "OK"
    except Exception as e:
        print(e)
        return "Error al generar la grafica del uso del CPU 1: " + e.args[0]


def grafica2(filename, time_start, time_end, title, db, var, umbral, color):  # Uso de la RAM
    try:
        rrdtool.graph(filename, "--start", str(time_start), "--end", str(time_end),
                      "--vertical-label=Porcentaje", "--lower-limit", "0", "--upper-limit", "100",
                      "--title=Uso de la Memoria Fisica " + title + " - " + umbral + " %",
                      "DEF:var1=" + db + ":ramUsed:AVERAGE",
                      "DEF:var2=" + db + ":cachUsed:AVERAGE",
                      "CDEF:var3=var1,100,*," + str(var) + ",/",
                      "CDEF:var4=var2,100,*," + str(var) + ",/",
                      "CDEF:var5=var3,var4,-",
                      "VDEF:var6=var5,MAXIMUM",
                      "VDEF:var7=var5,MINIMUM",
                      "VDEF:var8=var5,AVERAGE",
                      "VDEF:var9=var5,STDEV",
                      # "CDEF:var10=var5," + umbral + ",GT,var5,0,IF",
                      "LINE3:var5#0000FF:RAM",
                      # "AREA:var10#" + color + ":Umbral Sobrepasado",
                      "GPRINT:var6:%6.2lf %SMAX",
                      "GPRINT:var7:%6.2lf %SMIN",
                      "GPRINT:var8:%6.2lf %SAVG",
                      "GPRINT:var9:%6.2lf %SSTDEV")
        return "OK"
    except Exception as e:
        print(e)
        return "Error al generar la grafica del uso de la Memoria Fisica: " + e.args[0]


""" import os
import datetime
grafica1(os.path.join(os.getcwd(), "Images", "cpuUmbrales.png"), int(datetime.datetime.now().timestamp())-50400, int(datetime.datetime.now().timestamp()), "Prueba", os.path.join(os.getcwd(), "Databases", "localhost.rrd"), "100", "00FF00")
grafica2(os.path.join(os.getcwd(), "Images", "ramUmbrales.png"), int(datetime.datetime.now().timestamp())-50400, int(datetime.datetime.now().timestamp()), "Prueba", os.path.join(os.getcwd(), "Databases", "localhost.rrd"), 11625324, "100", "00FF00") """
