def arithmetic(a:float,b:float,c:str):
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - Korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype var:
    """
 
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        r=a/b
        if b!=0:
            r=a/b
        else:
            r="Div/0"
    else:
        print("Viga")
        r=0.0
    return r
 
def is_year_lwap(aasta:int):
    """Liigaasta leidmine
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsioni logilises formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus
 
def square(storona:float):
    """Square leidmine
    perimetr - storona*4
    ploshad - storona*storona
    diagonal - sqrt(2*storona)
    :param float storona: Esimene arv
    :rtype var:
    """
    if storona=="perimetr":
        sq=storona*4
    elif storona=="ploshad":
        sq=storona*storona
    elif storona=="diagonal":
        sq=sqrt(2*storona)
    else:
        print("Viga")
    return sq