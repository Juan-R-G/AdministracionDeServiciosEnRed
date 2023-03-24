from pysnmp.hlapi import *


def consulta11(community, ip, port):  # Sistema Operativo
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.1.1.0"))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1]


def consulta14(community, ip, port):  # Contacto
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.1.4.0"))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1]


def consulta15(community, ip, port):  # Nombre del Agente
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.1.5.0"))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1]


def consulta16(community, ip, port):  # Localizacion
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.1.6.0"))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1]


def consulta21(community, ip, port):  # Numero de interfaces
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.2.1.0"))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1]


def consulta221(community, ip, port, pos):  # Id de Interfaz
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.2.2.1.1." + pos))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1]


def consulta222(community, ip, port, iid):  # Nombre de Interfaz
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.2.2.1.2." + iid))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1]


def consulta227(community, ip, port, iid):  # Estado Administrativo de Interfaz
    error_indication, error_status, error_index, var_binds = next(getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, port)), ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.2.2.1.7." + iid))))
    if error_indication:
        return error_indication
    elif error_status:
        return error_status
    else:
        r = []
        for var_bind in var_binds:
            r = [var.prettyPrint() for var in var_bind]
        return r[1]


# print(consulta11("comunidadASR", "localhost", "161"))
# Linux -> split() -> Linux[0] VersionKernel[2] VersionLinux[3].split("~")[1].split("-") <- Dist-Version
# print(consulta11("comunidadWinASR", "172.100.71.129", "161"))
# Windows -> split(" - ")[1].split(": ")[1].split(" (")[0]
# print(consulta14("comunidadASR", "localhost", "161"))
# print(consulta14("comunidadWinASR", "172.100.71.129", "161"))
# print(consulta15("comunidadASR", "localhost", "161"))
# print(consulta15("comunidadWinASR", "172.100.71.129", "161"))
# print(consulta16("comunidadASR", "localhost", "161"))
# print(consulta16("comunidadWinASR", "172.100.71.129", "161"))
# print(consulta21("comunidadASR", "localhost", "161"))
# print(consulta222("comunidadASR", "localhost", "161", consulta221("comunidadASR", "localhost", "161", "2")))
# print(consulta227("comunidadASR", "localhost", "161", consulta221("comunidadASR", "localhost", "161", "2")))
