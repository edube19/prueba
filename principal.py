from re import X
from turtle import pos, position
from uuid import NAMESPACE_URL
from seccion import *
import os



#crear_seccion(lista_secciones)

#buscar_seccion(lista_secciones)

#agregar_alumno(self,info_alumnos,curso,nseccion):


contador=0
vacio=[]
lista_secciones=[]
lista_nombre_secciones=[]
def menu():

    os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    print("-----SALON V1-----")
    print("Eliga una opción: \n")
    print ("\t1 - Agregar/quitar seccion")#acabado 3/3
    print( "\t2 - Elegir una seccion")
    print ("\t9 - salir")

    #print ("\t2 - Agregar/quitar alumnos")#acabado 3/3
    #print ("\t3 - Agregar/modificar/eliminar/ver notas")
    #print ("\t9 - salir")

while True:
# Mostramos el menu
    menu()
    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu=="1":#agregar/quitar seccion
        while True:
            print ("\t1 - Agregar seccion")#acabado
            print ("\t2 - Quitar seccion")#acabado
            #print ("\t3 - Ver secciones")#acabado
            print ("\t9 - Regresar")
            opcion=input("Eliga una opcion...\n")
            if opcion=="1":#agregar seccion
                os.system('cls')
                crear_seccion(lista_secciones,lista_nombre_secciones)   
            elif opcion=="2":#quitar seccion
                eliminar_seccion(lista_secciones,lista_nombre_secciones)
            #elif opcion=="3":
                #cantidad_secciones=ver_secciones(lista_secciones)
                #print("Cantidad de secciones",cantidad_secciones)
            elif opcion=="9":#regresar
                break
            else:
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar") 
    elif opcionMenu=="2":#elegir seccion
        
        os.system('cls')
        opcionMenu_elegirseccion=None
        #condicion_opcion1='1'
        while(opcionMenu_elegirseccion!='0'):
            #nombre_seccion=input("Eliga el nombre/número de la seccion : ")
            for x in range(len(lista_secciones)):
                print (f"\t{x+1} - seccion {lista_secciones[x].nseccion}")#imprime todas las secciones existentes
            print ("\t0 - Regresar")
            opcionMenu_elegirseccion=input("Eliga una opcion...\n")
            if opcionMenu_elegirseccion in range(len(lista_secciones)+1):
            #for x in range(len(lista_secciones)):    
                #if nombre_seccion == lista_secciones[x].nseccion:
                while True:
                    os.system('cls')
                    print ("\t1 - Agregar alumno")#acabado
                    print ("\t2 - Quitar alumno")#
                    print ("\t3 - Ver lista alumnos")#acabado
                    print ("\t9 - Regresar")
                    opcion=input("Eliga una opcion...\n")    
                    #else :
                        #if ((x+1)==len(lista_secciones)):
                    #print("La seccion no existe")
                    cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                    condicion_opcion1=validacion_confirmación(cond)  
        """while True:
            os.system('cls')
            print ("\t1 - Agregar alumno")#acabado
            print ("\t2 - Quitar alumno")#
            print ("\t3 - Ver lista alumnos")#acabado
            print ("\t9 - Regresar")
            opcion=input("Eliga una opcion...\n")
            if opcion=="1":#Agregar alumno, acabado
                os.system('cls')
                condicion_opcion1='1'
                while(condicion_opcion1!='0'):
                    nombre_seccion=input("Ponga el nombre/número de la seccion a poner alunmos: ")
                    for x in range(len(lista_secciones)):
                        if nombre_seccion == lista_secciones[x].nseccion:
                            #if (nombre_seccion not in vacio):
                                print("Ingrese los alumnos de la seccion "+lista_secciones[x].nseccion+": \n")
                                info_alumnos_listado=lista_secciones[x].info_alumnos#
                                curso_listado=lista_secciones[x].curso#
                                nombre_seccion_listado=lista_secciones[x].nseccion#
                                lista_nombres_listado=lista_secciones[x].lista_nombres#

                                lista_secciones[x].agregar_alumno(info_alumnos_listado,curso_listado,nombre_seccion_listado,lista_nombres_listado)
                                cond=input("Desea buscar de otra seccion (1→SI / 0→NO):")
                                condicion_opcion1=validacion_confirmación(cond)
                                break
                        else :
                            if ((x+1)==len(lista_secciones)):
                                print("La seccion no existe")
                                cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                                condicion_opcion1=validacion_confirmación(cond)"""

            elif opcion=="2":#Quitar alumno,arreglado y acabado
                os.system('cls')
                condicion_opcion2='1'
                while(condicion_opcion2!='0'):
                    nombre_seccion=input("Ponga el nombre/número de la seccion: ")
                    for x in range(len(lista_secciones)):
                        if nombre_seccion == lista_secciones[x].nseccion:
                            lista_secciones[x].quitar_alumno(info_alumnos_listado,lista_nombres_listado,x,lista_secciones)
                            #print("Alumno eliminado de la seccion ",nombre_seccion)
                            cond=input("Desea buscar de otra seccion (1→SI / 0→NO):")
                            condicion_opcion2=validacion_confirmación(cond)
                            break
                        else :
                            if ((x+1)==len(lista_secciones)):
                                print("La seccion no existe")
                                cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                                condicion_opcion2=validacion_confirmación(cond)

            elif opcion=="3":#Ver lista alumnos, acabado
                condicion_opcion3='1'
                os.system('cls')
                while(condicion_opcion3!='0'):
                    nombre_seccion=input("Ponga el nombre/número de la seccion: ")
                    for x in range(len(lista_secciones)):
                        if nombre_seccion == lista_secciones[x].nseccion:
                            lista_secciones[x].ver_lista(info_alumnos_listado,nombre_seccion,x,lista_secciones)
                            cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                            condicion_opcion3=validacion_confirmación(cond)
                            break
                        else :
                            if ((x+1)==len(lista_secciones)):
                                print("La seccion no existe")
                                cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                                condicion_opcion3=validacion_confirmación(cond)
            elif opcion=="9":
                break
            else:
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    elif opcionMenu=="3":
        while True:
            os.system('cls')
            print ("\t1 - Agregar/ver nota alumno")
            print ("\t2 - Eliminar nota alumno")
            print ("\t3 - Calcular nota final alumno")
            print ("\t9 - Regresar")
            opcion=input("Eliga una opcion...\n")
            if opcion=="1":#Agregar/ver nota alumno
                condicion='1'
                while(condicion!='0'):
                    nombre_seccion=input("Ponga el nombre/número de la seccion a poner notas")
                    for x in range(len(lista_secciones)):
                        if nombre_seccion == lista_secciones[x].nseccion:
                            print("Ingrese los alumnos de la seccion "+lista_secciones[x].nseccion+": \n")
                            notas_min_pc_listado=lista_secciones[x].notas_min_pc
                            lista_secciones[x].inicializar_notas(1,info_alumnos_listado)#1 para inicializar la columna de notas
                            lista_secciones[x].inicializar_notas(2,info_alumnos_listado)#2 para inicializar la columna de nota final
                            lista_secciones[x].inicializar_notas_min_pc(notas_min_pc_listado,info_alumnos_listado)#inicializa la nota mas baja de todas
                            c='1'
                            while (c!='0'):
                                alumno=input("Ingrese el nombre del alumno a asignar notas: ")
                                lista_secciones[x].recibir_notas(info_alumnos_listado,alumno)
                                condicion_alumno=input(" ¿Ingresar otro? (1→SI / 0→NO) ")
                                c=validacion_confirmación(condicion_alumno)
                            lista_secciones[x].ver_notas_seccion(info_alumnos_listado,nombre_seccion_listado)
                            cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                            condicion=validacion_confirmación(cond)
                            break
                        else :
                            if ((x+1)==len(lista_secciones)):
                                print("La seccion no existe")
                                cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                                condicion=validacion_confirmación(cond)
            elif opcion=="2":#Eliminar nota alumno, elimina y todo pero 
                             #no se puede salir de este bucle al invocar la funcion :/
                os.system('cls')
                condicion_opcion2='1'
                c='1'
                while(condicion_opcion2!='0'):
                    nombre_seccion=input("Ponga el nombre/número de la seccion: ")
                    for x in range(len(lista_secciones)):
                        if nombre_seccion == lista_secciones[x].nseccion:
                            while (c!='0'):
                                alumno=input("Ingrese el nombre del alumno a modificar nota: ")
                                lista_secciones[x].eliminar_modificar_notas(info_alumnos_listado,x,alumno,lista_secciones)
                                condicion_alumno=input(" ¿Ingresar otro? (1→SI / 0→NO) ")
                                c=validacion_confirmación(condicion_alumno)
                            cond=input("Desea modificar de otra seccion (1→SI / 0→NO):")
                            condicion_opcion2=validacion_confirmación(cond)
                            break
                        else :
                            if ((x+1)==len(lista_secciones)):
                                print("La seccion no existe")
                                cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                                condicion_opcion2=validacion_confirmación(cond)
            elif opcion=="3":#sacar nota,ya esta
                os.system('cls')
                condicion_opcion3='1'
                c='1'
                while(condicion_opcion3!='0'):
                    nombre_seccion=input("Ponga el nombre/número de la seccion: ")
                    for x in range(len(lista_secciones)):
                        if nombre_seccion == lista_secciones[x].nseccion:
                            while (c!='0'):
                                alumno=input("Ingrese el nombre del alumno a sacar nota: ")
                                lista_secciones[x].promedio_alumnos(info_alumnos_listado,alumno)
                                condicion_alumno=input(" ¿Ingresar otro? (1→SI / 0→NO) ")
                                c=validacion_confirmación(condicion_alumno)
                            cond=input("Desea modificar de otra seccion (1→SI / 0→NO):")
                            condicion_opcion3=validacion_confirmación(cond)
                            break
                        else :
                            if ((x+1)==len(lista_secciones)):
                                print("La seccion no existe")
                                cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                                condicion_opcion3=validacion_confirmación(cond)
            elif opcion=="9":
                break
            else:
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

    elif opcionMenu=="9":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
