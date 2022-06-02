def validacion_confirmación(condicion):
    lista_condicion=['0','1']
    if (condicion not in lista_condicion):
        print("Ingrese solo 0(NO) o 1(SI)")
        condicion_nuevo=input("Ingrese nuevamente 0(NO) o 1(SI): ")
        validacion_confirmación(condicion_nuevo)
    else:
        return condicion
c='1'
while (c!='0'):
    alumno=input("Ingrese el nombre del alumno a asignar notas: ")
    condicion_alumno=input(" ¿Ingresar otro? (1→SI / 0→NO) ")
    c=validacion_confirmación(condicion_alumno)
    #c=condicion_alumno