def vref(tension=int):
    if tension>2.5:
        degree_sign = u'\N{DEGREE SIGN}'
        falso= ((100*tension)/2.5)
        grado=falso - 100
        print("el error medido es: ",grado,degree_sign)
        return falso
    else:  falso = ((100*tension)/2.5)
    return falso
    
    
    

degree_sign = u'\N{DEGREE SIGN}'
tension_vref= float(input("tension a leer: "))

print("cantidad de grados leidos",vref(tension_vref),degree_sign)