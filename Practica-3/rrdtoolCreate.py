# Roldan-Gomez-Juan
import os
import rrdtool
devices = []
if os.path.exists(os.path.join(os.getcwd(), "Dispositivos")):
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Dispositivos")):
        for name in files:
            devices.append(name.replace(".txt", ""))
    if len(devices):
        if not os.path.exists(os.path.join(os.getcwd(), "Databases")):
            os.mkdir(os.path.join(os.getcwd(), "Databases"))
        for name in devices:
            if not os.path.exists(os.path.join(os.getcwd(), "Databases", name + ".rrd")):
                try:
                    rrdtool.create(os.path.join(os.getcwd(), "Databases", name + ".rrd"),
                                   "--start", "N", "--step", "60",
                                   "DS:ifInUcastPkts:COUNTER:120:U:U",
                                   "DS:ipInReceives:COUNTER:120:U:U",
                                   "DS:icmpOutEchos:COUNTER:120:U:U",
                                   "DS:tcpInSegs:COUNTER:120:U:U",
                                   "DS:udpInDatagrams:COUNTER:120:U:U",
                                   "DS:procLoad:GAUGE:120:0:100",
                                   "DS:ramUsed:GAUGE:120:U:U",
                                   "DS:cachUsed:GAUGE:120:U:U",
                                   "DS:hddUsed:GAUGE:120:U:U",
                                   "RRA:AVERAGE:0.5:1:2000",
                                   "RRA:AVERAGE:0.5:5:400",
                                   "RRA:AVERAGE:0.5:10:200",
                                   "RRA:AVERAGE:0.5:20:100")
                    print("Se creo exitosamente el archivo " + name + ".rrd")
                except Exception as e:
                    print("Ocurrio un error al crear el archivo " + name + ".rrd")
                    print("Error: " + e.args[0])
