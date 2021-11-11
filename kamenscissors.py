from moodle import *
from math import *
while True:
    print("Funktsioonid".center(50,"+"))
    print("arithmetic - A, is year leap - Y, square - S")
    v=input("=> ")
    if v.upper()=="A":
        arv1=float(input("Arv 1:"))
        arv2=float(input("Arv 2:"))
        sym=input("Tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=="Y":
        rezult=is_year_leap(int(input("Sisesta aasta")))
        print(rezult)
    elif v.upper()=="S":
        rezult=square(float(input("Arv => ")))
        print=square(rezult)