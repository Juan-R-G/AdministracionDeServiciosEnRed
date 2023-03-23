from pysnmp.hlapi import *


def consulta11(community, ip, port):
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.1.1.0"))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1].split()


def consulta12(community, ip, port):
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.1.2.0"))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1].split('::')


print(consulta11("comunidadASR", "localhost", "161"))
# SO - User - Version Kernel - VersionUbuntu - Otros(2) - Fecha?(6) - Arquitectura
# Windows
print(consulta12("comunidadASR", "localhost", "161"))
# SNMP Version - OID
