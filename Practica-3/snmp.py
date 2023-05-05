from pysnmp.hlapi import *


def consulta(community, ip, port, oid):
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity(oid))))

    res = "error"

    if error_indication:
        print(error_indication)
        return res
    elif error_status:
        print(error_status)
        return res
    else:
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
            res = r[1]
        return res


# print(consulta("JuanRGomez", "localhost", "161", "1.3.6.1.2.1.25.3.3.1.2.196608"))  # Uso del procesador 1
# print(consulta("JuanRGomez", "localhost", "161", "1.3.6.1.2.1.25.2.2.0"))  # Total RAM disponible
# print(consulta("JuanRGomez", "localhost", "161", "1.3.6.1.2.1.25.2.3.1.6.1"))  # Total RAM usada (con cache)
# print(consulta("JuanRGomez", "localhost", "161", "1.3.6.1.2.1.25.2.3.1.6.7"))  # Total cache
# print(consulta("JuanRGomez", "localhost", "161", "1.3.6.1.2.1.25.2.3.1.5.36"))  # Total Tamaño Disco (*4096/1x10e9 = GB)
# print(consulta("JuanRGomez", "localhost", "161", "1.3.6.1.2.1.25.2.3.1.6.36"))  # Total Espacio Disco Usado (*4096/1x10e9 = GB)
