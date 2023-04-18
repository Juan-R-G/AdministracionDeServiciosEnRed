# Roldan-Gomez-Juan
from pysnmp.hlapi import *


def consulta(community, ip, port, oid):
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity(oid))))

    if error_indication:
        print(error_indication)
        return "error"
    elif error_status:
        print(error_status)
        return "error"
    else:
        res = "error"
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
            res = r[1]
        return res


# print(consulta("comunidadASR", "localhost", "161", "1.3.6.1.2.1.1.1.0"))
