from re import *
import doctest
def check_password(password):
    """
    Функция, проверяющая корректность пароля
    
    Args:
    password (str): Пароль.
    
    Returns:
    bool: Является ли пароль корректным.
    
    Примеры:
    
    >>> check_password("пароль")
    False
    >>> check_password("password")
    False
    >>> check_password("qwerty")
    False
    >>> check_password("lOngPa$$W0Rd")
    False
    >>> check_password("rtG&3FG#Tr^e")
    True
    >>> check_password("a^A1@*@1Aa")
    True
    >>> check_password("oF^a1D@y5%e6")
    True
    >>> check_password("enroi#$*rkdeR#$*092uwedchf34tguv394h")
    True
    """

    result = match(r"^(?=.*[a-z].*[a-z])(?=.*\d)(?=.*[$^%@#&*].*[$^%@#&*].*[$^%@#&*])[\w$^%@#&*]{8,}$", password)
    if result is not None:
        return True
    else:
        return False
    
doctest.testmod(verbose=True)