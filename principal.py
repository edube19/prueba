from re import X
from turtle import pos
from uuid import NAMESPACE_URL
from seccion import *
lista_secciones=[]

crear_seccion(lista_secciones)

buscar_seccion(lista_secciones)

cantidad_secciones=ver_secciones(lista_secciones)

#seccion1=Seccion(1,'Matemática','Echendia')
#seccion2=Seccion(2,'Fisica','Tafur')
print("Cantidad de secciones",cantidad_secciones)

#agregar_alumno(self,info_alumnos,curso,nseccion):
continuar_secciones=1
#for x in range(cantidad_secciones):
    #while (continuar_secciones!=0):
condicion=1
contador=0
vacio=[]
"""
while (contador!=len(lista_secciones)):
    nombre_seccion=input("Ponga el nombre/número de la seccion a poner notas: ") 
    if nombre_seccion in lista_secciones[contador].nseccion:
        if(lista_secciones[contador]==vacio):
            print("Ingrese los alumnos de la seccion "+lista_secciones[contador].nseccion+": \n")
            info_alumnos_listado=lista_secciones[contador].info_alumnos
            curso_listado=lista_secciones[contador].curso
            nombre_seccion_listado=lista_secciones[contador].nseccion
            notas_min_pc_listado=lista_secciones[contador].notas_min_pc

            lista_secciones[contador].agregar_alumno(info_alumnos_listado,curso_listado,nombre_seccion_listado)
            lista_secciones[contador].ver_lista(info_alumnos_listado,nombre_seccion_listado)

            lista_secciones[contador].inicializar_notas(1,info_alumnos_listado)#1 para inicializar la columna de notas
            lista_secciones[contador].inicializar_notas(2,info_alumnos_listado)#2 para inicializar la columna de nota final
            lista_secciones[contador].inicializar_notas_min_pc(notas_min_pc_listado,info_alumnos_listado)#inicializa la nota mas baja de todas
            c=1
            while (c!=0):
                alumno=input("Ingrese el nombre del alumno a asignar notas: ")
                lista_secciones[contador].recibir_notas(info_alumnos_listado,alumno)
                condicion_alumno=int(input(" ¿Ingresar otro? (1→SI / 0→NO) "))
                c=condicion_alumno

            lista_secciones[contador].ver_notas_seccion(info_alumnos_listado,nombre_seccion_listado)
            lista_secciones[contador].promedio_alumnos(info_alumnos_listado,notas_min_pc_listado)
            lista_secciones[contador].mayor_nota(info_alumnos_listado)
            lista_secciones[contador].menor_nota(info_alumnos_listado) 
            contador=len(lista_secciones)    
        else:
            print("Los datos de la seccion "+nombre_seccion+" ya fueron ingresadas")
            print(lista_secciones[contador])  
            contador=len(lista_secciones)
    else:
        contador=contador+1
        if (contador==len(lista_secciones)):
            print("No existe la seccion: ",nombre_seccion)

"""
while(condicion!=0 or contador!=len(lista_secciones)):
    #nombre_seccion=input("Ponga el nombre/número de la seccion a poner notas: ") 
    nombre_seccion=input("Ponga el nombre/número de la seccion a poner notas: ")
    for x in range(cantidad_secciones):    
        if (nombre_seccion == lista_secciones[x].nseccion):  
            print(lista_secciones[x].nseccion)
            if(lista_secciones[x].nseccion not in vacio):
                print("Ingrese los alumnos de la seccion "+lista_secciones[x].nseccion+": \n")
                info_alumnos_listado=lista_secciones[x].info_alumnos
                curso_listado=lista_secciones[x].curso
                nombre_seccion_listado=lista_secciones[x].nseccion
                notas_min_pc_listado=lista_secciones[x].notas_min_pc

                lista_secciones[x].agregar_alumno(info_alumnos_listado,curso_listado,nombre_seccion_listado)
                lista_secciones[x].ver_lista(info_alumnos_listado,nombre_seccion_listado)

                lista_secciones[x].inicializar_notas(1,info_alumnos_listado)#1 para inicializar la columna de notas
                lista_secciones[x].inicializar_notas(2,info_alumnos_listado)#2 para inicializar la columna de nota final
                lista_secciones[x].inicializar_notas_min_pc(notas_min_pc_listado,info_alumnos_listado)#inicializa la nota mas baja de todas
                c=1
                while (c!=0):
                    alumno=input("Ingrese el nombre del alumno a asignar notas: ")
                    lista_secciones[x].recibir_notas(info_alumnos_listado,alumno)
                    condicion_alumno=int(input(" ¿Ingresar otro? (1→SI / 0→NO) "))
                    c=condicion_alumno

                lista_secciones[x].ver_notas_seccion(info_alumnos_listado,nombre_seccion_listado)
                lista_secciones[x].promedio_alumnos(info_alumnos_listado,notas_min_pc_listado)
                lista_secciones[x].mayor_nota(info_alumnos_listado)
                lista_secciones[x].menor_nota(info_alumnos_listado)
                vacio.append(nombre_seccion)
                condicion=int(input("Desea poner datos de otra seccion (1→SI / 0→NO):"))
                contador=len(lista_secciones)
            else:
                print("Los datos de la seccion "+nombre_seccion+" ya fueron ingresadas")
                contador=len(lista_secciones)
                #condicion=int(input("Desea poner datos de otra seccion (1→SI / 0→NO):"))
        else:
            if ((x+1)==len(lista_secciones)):
                print("La seccion no existe")
                condicion=int(input("Desea poner datos de otra seccion (1→SI / 0→NO):"))
            #continuar_secciones=int(input(" ¿Ingresar datos de otra seccion? (1→SI / 0→NO) "))

"""n=1
seccion1.agregar_alumno(a,'Matemática',n)
seccion1.ver_lista(a,n)
seccion=input("Ingrese la seccion a poner nota → Seccion: ")
m=2
seccion2.agregar_alumno(seccion2.info_alumnos,'Fisica',m)
seccion2.ver_lista(seccion2.info_alumnos,m)

seccion1.inicializar_notas(1,seccion1.info_alumnos)#1 para inicializar la columna de notas
seccion1.inicializar_notas(2,seccion1.info_alumnos)#2 para inicializar la columna de nota final
seccion1.inicializar_notas_min_pc(seccion1.notas_min_pc,seccion1.info_alumnos)#inicializa la nota mas baja de todas

seccion2.inicializar_notas(1,seccion2.info_alumnos)#1 para inicializar la columna de notas
seccion2.inicializar_notas(2,seccion2.info_alumnos)#2 para inicializar la columna de nota final
seccion2.inicializar_notas_min_pc(seccion2.notas_min_pc,seccion2.info_alumnos)#inicializa la nota mas baja de todas
c=1


print("Seccion 1")
while (c!=0):
    alumno=input("Ingrese el nombre del alumno a asignar notas: ")
    seccion1.recibir_notas(seccion1.info_alumnos,alumno)
    condicion=int(input(" ¿Ingresar otro? (1→SI / 0→NO) "))
    c=condicion

seccion1.ver_notas_seccion(seccion1.info_alumnos,1)
seccion1.promedio_alumnos(seccion1.info_alumnos,seccion1.notas_min_pc)
seccion1.mayor_nota(seccion1.info_alumnos)
seccion1.menor_nota(seccion1.info_alumnos)

c=1
print("Seccion 2")
while (c!=0):
    alumno=input("Ingrese el nombre del alumno a asignar notas: ")
    seccion2.recibir_notas(seccion2.info_alumnos,alumno)
    condicion=int(input(" ¿Ingresar otro? (1→SI / 0→NO) "))
    c=condicion


seccion2.ver_notas_seccion(seccion2.info_alumnos,2)

seccion2.promedio_alumnos(seccion2.info_alumnos,seccion2.notas_min_pc)
seccion2.mayor_nota(seccion2.info_alumnos)
seccion2.menor_nota(seccion2.info_alumnos) """