import re

def is_logged(diccionario):
    if 'user_id' in diccionario:
        return True
    return False

def is_not_empty(the_cadena):
    if the_cadena is not None:
        valid_cadena = the_cadena.strip()
        if valid_cadena != "": return True 
        return False
    return False

def es_natural(cadena):
    x = re.findall('^[1-9][0-9]*$', cadena)
    if len(x)>0: return True
    else: return False

def es_decimal(cadena):
    if '.' in cadena:
        x = re.findall('^[0-9][0-9]*[.]{1}[0-9]*[1-9]+$', cadena)
        if len(x)>0: return True
        else: return False
    else:
        x = re.findall('^[1-9][0-9]*$', cadena)
        if len(x)>0: return True
        else: return False