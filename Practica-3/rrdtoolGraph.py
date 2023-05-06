import rrdtool


def grafica(filename, time_start, time_end, title, unit, var, db, op, name):
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


def grafica1(filename, time_start, time_end, db):  # Uso del Procesador 1
    try:
        rrdtool.graph(filename, "--start", str(time_start), "--end", str(time_end),
                      "--vertical-label=Porcentaje", "--lower-limit", "0", "--upper-limit", "100",
                      "--title=Uso del CPU 1",
                      "DEF:var=" + db + ":procLoad:AVERAGE",
                      "VDEF:var1=var,MAXIMUM",
                      "VDEF:var2=var,MINIMUM",
                      "VDEF:var3=var,AVERAGE",
                      "VDEF:var4=var,STDEV",
                      "LINE3:var#0000FF:CPU 1",
                      "GPRINT:var1:%6.2lf %SMAX",
                      "GPRINT:var2:%6.2lf %SMIN",
                      "GPRINT:var3:%6.2lf %SAVG",
                      "GPRINT:var4:%6.2lf %SSTDEV")
        return "OK"
    except Exception as e:
        print(e)
        return "Error al generar la grafica del uso del CPU 1: " + e.args[0]


def grafica2(filename, time_start, time_end, db):  # Uso de la RAM
    try:
        rrdtool.graph(filename, "--start", str(time_start), "--end", str(time_end),
                      "--vertical-label=Porcentaje", "--lower-limit", "0", "--upper-limit", "100",
                      "--title=Uso de la RAM",
                      "DEF:var1=" + db + ":" + var[0] + ":AVERAGE",
                      "DEF:var2=" + db + ":" + var[1] + ":AVERAGE",
                      "CDEF:var3=var1,100,*," + var[2] + ",/")
    except Exception as e:
        print(e)
