import re
from datetime import datetime

def validar_nombre(nombre):
    if not nombre:
        return "El nombre no puede estar vacío."
    elif not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nombre):
        return "El nombre solo puede contener letras y espacios."
    return None

def validar_identificacion(identificacion):
    if not identificacion:
        return "La identificación no puede estar vacía."
    elif not re.match("^\d+$", identificacion):
        return "La identificación solo puede contener números."
    return None

def validar_cantidad_personas(cantidad_personas):
    try:
        cantidad_personas = int(cantidad_personas)
        if cantidad_personas <= 0:
            return "La cantidad de personas debe ser mayor que 0."
    except ValueError:
        return "Por favor ingrese un número válido para la cantidad de personas."
    return None

def validar_fecha(fecha):
    if not fecha:
        return "La fecha no puede estar vacía."
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        return "Formato de fecha inválido. Por favor ingrese la fecha en el formato YYYY-MM-DD."
    return None

def validar_estado(estado):
    if estado not in ['activo', 'inactivo']:
        return "El estado debe ser 'activo' o 'inactivo'."
    return None

def validar_id_rol(id_rol):
    try:
        id_rol = int(id_rol)
        if id_rol <= 0:
            return "El ID de rol debe ser un número entero positivo."
    except ValueError:
        return "Por favor ingrese un número válido para el ID de rol."
    return None

def validar_salario(salario):
    try:
        salario = float(salario)
        if salario <= 0:
            return "El salario debe ser un número positivo."
    except ValueError:
        return "Por favor ingrese un número válido para el salario."
    return None

def validar_telefono(telefono):
    if not telefono:
        return "El teléfono no puede estar vacío."
    elif not re.match("^\d+$", telefono):
        return "El teléfono solo puede contener números."
    return None

def validar_direccion(direccion):
    if not direccion:
        return "La dirección no puede estar vacía."
    elif not re.match("^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s]+$", direccion):
        return "La dirección solo puede contener letras, números y espacios."
    return None
