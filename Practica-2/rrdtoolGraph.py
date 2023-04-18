# Roldan-Gomez-Juan
import rrdtool


def grafica(filename, time_start, time_end, title, var, db, name):
    try:
        rrdtool.graph(filename, "--start", str(time_start), "--end", str(time_end),
                      "--vertical-label=Bytes/s", "--title=" + title,
                      "DEF:variable=" + db + ":" + var + ":AVERAGE",
                      "CDEF:escala=variable,8,*",
                      "LINE3:escala#0000FF:" + name)
        return "OK"
    except Exception as e:
        print(e)
        return "Error al generar la grafica :" + e.args[0]
