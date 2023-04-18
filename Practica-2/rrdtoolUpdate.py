# Roldan-Gomez-Juan
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
                    if ifInUcastPkts == "" or ipInReceives == "" or icmpOutEchos == "" or tcpInSegs == "" or udpInDatagrams == "":
                        raise Exception("Error al hacer las consultas SNMP...")
                    valor = "N:" + ifInUcastPkts + ":" + ipInReceives + ":" + icmpOutEchos + ":" + tcpInSegs + ":" + udpInDatagrams
                    print(db + " - " + valor)
                    rrdtool.update(os.path.join(os.getcwd(), "Databases", db + ".rrd"), valor)
                    rrdtool.dump(os.path.join(os.getcwd(), "Databases", db + ".rrd"), os.path.join(os.getcwd(), "Databases", db + ".xml"))
                    time.sleep(1)
                except Exception as e:
                    if e == KeyboardInterrupt:
                        raise Exception("Se cancelo la ejecucion del programa...")
                    print("Error: " + e.args[0] + "\nmientras se trabajaba con el archivo " + db + ".rrd")
                    databases.remove(db)
        except Exception as e:
            print(e)
            databases = []
