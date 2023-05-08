import os
from snmp import consulta
import rrdtool
import time
databases = []
if os.path.exists(os.path.join(os.getcwd(), "Databases")):
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Databases")):
        for name in files:
            if ".xml" not in name:
                databases.append(name.replace(".rrd", ""))
    while len(databases):
        try:
            for db in databases:
                try:
                    file = open(os.path.join(os.getcwd(), "Dispositivos", db + ".txt"), "r")
                    t = file.readline().replace("\n", "").split('-')
                    first = ''
                    while first == '':
                        x = file.readline().replace("\n", "")
                        if '&' in x:
                            first = x[1]
                    file.close()
                    ip = t[0].split(':')[1]
                    comm = t[2].split(':')[1]
                    port = t[3].split(':')[1]
                    ifInUcastPkts = consulta(comm, ip, port, "1.3.6.1.2.1.2.2.1.11." + first)
                    ipInReceives = consulta(comm, ip, port, "1.3.6.1.2.1.4.3.0")
                    icmpOutEchos = consulta(comm, ip, port, "1.3.6.1.2.1.5.21.0")
                    tcpInSegs = consulta(comm, ip, port, "1.3.6.1.2.1.6.10.0")
                    udpInDatagrams = consulta(comm, ip, port, "1.3.6.1.2.1.7.1.0")
                    procLoad = consulta(comm, ip, port, "1.3.6.1.2.1.25.3.3.1.2.196608")
                    ramUsed = consulta(comm, ip, port, "1.3.6.1.2.1.25.2.3.1.6.1")
                    cachUsed = consulta(comm, ip, port, "1.3.6.1.2.1.25.2.3.1.6.7")
                    hddUsed = consulta(comm, ip, port, "1.3.6.1.2.1.25.2.3.1.6.36")
                    if ifInUcastPkts == "error" or ipInReceives == "error" or icmpOutEchos == "error" or tcpInSegs == "error" or udpInDatagrams == "error" or procLoad == "error" or ramUsed == "error" or cachUsed == "error" or hddUsed == "error":
                        raise Exception("Error al hacer las consultas SNMP...")
                    valor = "N:" + ifInUcastPkts + ":" + ipInReceives + ":" + icmpOutEchos + ":" + tcpInSegs + ":" + udpInDatagrams + ":" + procLoad + ":" + ramUsed + ":" + cachUsed + ":" + hddUsed
                    print(db + " - " + valor)
                    rrdtool.update(os.path.join(os.getcwd(), "Databases", db + ".rrd"), valor)
                    time.sleep(5)
                except Exception as e:
                    if e == KeyboardInterrupt:
                        raise Exception("Se cancelo la ejecucion del programa...")
                    print("Error: " + e.args[0] + "\nmientras se trabajaba con el archivo " + db + ".rrd")
                    databases.remove(db)
        except Exception as e:
            print(e)
            databases = []
