#creando la sección de clases

#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
from asyncio.windows_events import NULL
from distutils.log import info
from pickle import APPEND
import os
import time
lista_secciones=[]

def validacion_confirmación(condicion):
    lista_condicion=['0','1']
    if (condicion not in lista_condicion):
        print("Ingrese solo 0(NO) o 1(SI)")
        condicion_nuevo=input("Ingrese nuevamente 0(NO) o 1(SI): ")
        validacion_confirmación(condicion_nuevo)
    else:
        return condicion

def crear_seccion(lista_secciones,lista_nombre_secciones):
    print("-----Creando secciones-----")
    #lista_nombre_secciones=[]
    cond='1'
    while(cond!='0'):
        #while True:
        nombre_seccion=input("Ingrese el nombre/número de la seccion: ")    
        if (nombre_seccion in lista_nombre_secciones):
            print("Ya existe esa sección")
        else:
            lista_nombre_secciones.append(nombre_seccion)
            curso=input("Ingrese el curso de la seccion: ")
            profesor=input("Ingrese el profesor de la seccion: ")
            lista_secciones.append(Seccion(nombre_seccion,curso,profesor))
            print("Seccion creada")
        condicion=input("Desea agregar otra seccion (1→SI / 0→NO):")
        cond=validacion_confirmación(condicion)    

def buscar_seccion(lista_secciones):
    condicion='1'
    contador=0
    while(condicion!='0'):
        nombre_seccion=input("Ponga el nombre/número de la seccion a buscar: ")
        for x in range(len(lista_secciones)):
            if nombre_seccion == lista_secciones[x].nseccion:
                print("La seccion "+nombre_seccion+" si existe")
                condicion=int(input("Desea buscar otra seccion (1→SI / 0→NO):"))
                break
            else:
                contador=x
                if ((contador+1)==len(lista_secciones)):
                    print("La seccion no existe")
                    cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                    condicion=validacion_confirmación(cond)

def eliminar_seccion(lista_secciones,lista_nombre_secciones):
    condicion='1'
    contador=0
    while(condicion!='0'):
        nombre_seccion=input("Ponga el nombre/número de la seccion a eliminar: ")
        for x in range(len(lista_secciones)):
            if nombre_seccion == lista_secciones[x].nseccion:
                print("Seccion a eliminar: ",nombre_seccion)
                lista_secciones.pop(x)
                lista_nombre_secciones.remove(nombre_seccion)
                print("Se elimino la seccion: "+nombre_seccion)
                cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                condicion=validacion_confirmación(cond)
                break
            else:
                contador=x
                if ((contador+1)==len(lista_secciones)):
                    print("La seccion no existe")
                    cond=input("Desea buscar otra seccion (1→SI / 0→NO):")
                    condicion=validacion_confirmación(cond)

def ver_secciones(lista_secciones):
    print("Lista de secciones")
    for x in range(len(lista_secciones)):
        print("Seccion "+lista_secciones[x].nseccion+"\n") 
    return len(lista_secciones) 

class Seccion:
    
    notas_max_min=[[]]#[alumno][1]→ nota menor,[alumno][0]→ nota mayor .Lista de la mejor/menor nota de cada alumno
    notas_min_pc=[]#la pc mas baja de cada alumno
    
    def __init__(self,nseccion,curso,profesor):
        self.nseccion=nseccion
        self.curso=curso
        self.profesor=profesor
        self.info_alumnos=[[],[],[]]#para que pertenesca a este,[[alumnos],[notas],[nota final]]
        self.notas_min_pc=[]
        self.lista_nombres=[]
    
    def agregar_alumno(self,info_alumnos,curso,nseccion,lista_nombres):
        print("Seccion ",nseccion)
        #lista_nombres=[]#guarda los nombres de todos los alumnos
        cond='1'
        while(cond!='0'):
            nombre_valido=0#si es cero seguira pidiendo el nombre
            while(nombre_valido==0):
                nombreAlumno=input("Nombre del alumno a ingresar: ")
                if nombreAlumno.isalpha():
                    nombre_valido=1#se ingreso un nombre valido (solo letras)
                else:
                    print("Ingrese solo nombres")
            if nombreAlumno in lista_nombres:
                print("Ya existe este alumno")
            else:
                lista_nombres.append(nombreAlumno)
                info_alumnos[0].append(Alumno(nombreAlumno,nseccion,curso))#poner al final en la lista de alumnos
                print("Se agrego al alumno: "+nombreAlumno)
            condicion=input("Desea agregar otro alumno (1→SI / 0→NO):")
            cond=validacion_confirmación(condicion)

    def quitar_alumno(self,info_alumnos,lista_nombres,posicion,lista_secciones):
        condicion='1'
        while(condicion!='0'):
            nombre_valido=0#si es cero seguira pidiendo el nombre
            while(nombre_valido==0):
                nombreAlumno=input("Nombre del alumno a eliminar: ")
                if nombreAlumno.isalpha():
                    nombre_valido=1#se ingreso un nombre valido (solo letras)
                else:
                    print("Ingrese solo nombres")
            for x in range(len(lista_secciones[posicion].info_alumnos[0])):
                if nombreAlumno == lista_secciones[posicion].info_alumnos[0][x].nombre:
                    continuar=input("Alumno a eliminar: "+nombreAlumno+" ¿Continuar? (1→SI / 0→NO)")
                    continuar_condicion=validacion_confirmación(continuar)
                    if (continuar_condicion=='1'):
                        info_alumnos[0].pop(x)
                        lista_nombres.remove(nombreAlumno)
                        print("Se elimino de la seccion"+lista_secciones[posicion].nseccion+"al alumno: "+nombreAlumno)
                    cond=input("Desea buscar eliminar otro alumno (1→SI / 0→NO):")
                    condicion=validacion_confirmación(cond)
                    break
                else:
                    contador=x
                    if ((contador+1)==len(lista_secciones[posicion].info_alumnos[0])):
                        print("El alumno no pertenece a la seccion",lista_secciones[posicion].nseccion)
                        cond=input("Desea buscar eliminar otro alumno (1→SI / 0→NO):")
                        condicion=validacion_confirmación(cond)          

    def ver_lista(self,info_alumnos,nseccion,posicion,lista_secciones):
        print("Lista de alumnos de la seccion "+str(nseccion)+": ")
        print("total alumnos de la seccin "+nseccion+" : "+str(len(lista_secciones[posicion].info_alumnos[0])))
        for x in range(len(lista_secciones[posicion].info_alumnos[0])):
            print("Alumno n° "+str(x+1)+" : "+lista_secciones[posicion].info_alumnos[0][x].nombre)
        return len(info_alumnos[0])

    def mayor_nota(self,info_alumnos):
        vacio=[]
        max_value = 0
        max_idx = 0
        for idx, num in enumerate(info_alumnos[2]):
            if(info_alumnos[2][idx]!=vacio):
                if (max_value ==0 or num > max_value):
                    max_value = num
                    max_idx = idx
        print('La Maxima nota es: ', str(max_value), "del alumno: ", str(info_alumnos[0][max_idx].nombre))

        tres_mejores_notas=[]
        tres_mejores_notas.append(max_value)
        print("..................")
        print(tres_mejores_notas)

        vacio=[]
        max_value1 = 0
        max_idx1 = 0
        for idx, num in enumerate(info_alumnos[2]):
            if(info_alumnos[2][idx]!=vacio and info_alumnos[2][idx] not in tres_mejores_notas):
                if (max_value1 < max_value or num > max_value1 ):
                    max_value1 = num
                    max_idx1 = idx
        tres_mejores_notas.append(max_value1)

        vacio=[]
        max_value2 = 0
        max_idx2 = 0
        for idx, num in enumerate(info_alumnos[2]):
            if(info_alumnos[2][idx]!=vacio and info_alumnos[2][idx] not in tres_mejores_notas):
                if (max_value2 < max_value1 or num > max_value2 ):
                    max_value2 = num
                    max_idx2 = idx
        print("Las tres mejores notas son: ")
        print("3 mejor nota es: "+str(max_value2)+" del alumno: "+str(info_alumnos[0][max_idx2].nombre))
        print("2 mejor nota es: "+str(max_value1)+" del alumno: "+str(info_alumnos[0][max_idx1].nombre))
        print("La mejor nota es: "+str(max_value)+" del alumno: "+str(info_alumnos[0][max_idx].nombre))

    def menor_nota(self,info_alumnos):   
        vacio=[]
        min_value = 20
        min_idx = None
        for idx, num in enumerate(info_alumnos[2]):
            if (info_alumnos[2][idx]!=vacio):
                if (min_value == 20 or num < min_value ):
                    min_value = num
                    min_idx = idx
        print('La menor nota es: ', str(min_value), "del alumno: ", str(info_alumnos[0][min_idx].nombre))
    def recibir_notas(self,info_alumnos,alumno):
        notas=[]#aca se guardaran las notas
        vacio=[]
        contador=0
        validacion_nota=0
        notascero=[]#solo para inicializar las notas
        for j in range(6):
            notas.append(notascero)
        # print(notas)
        while (contador!=len(info_alumnos[0])):
            if alumno in info_alumnos[0][contador].nombre:
                if(info_alumnos[1][contador]==vacio):
                    print("Ingresar notas del alumno "+info_alumnos[0][contador].nombre+": ")    
                    for k in range(6):
                        if k<4:
                            while(validacion_nota==0):
                                notas[k]=int(input(f'PC{str(k+1)}: '))
                               
                                if notas[k] in range(21):
                                    info_alumnos[1][contador].append(notas[k])
                                    validacion_nota=1
                                else:
                                    print("Nota no valida, debe ingresar notas de 0 a 20")
                            validacion_nota=0
                        elif k==4:
                            while(validacion_nota==0):
                                notas[k]=int(input("Parcial: "))
                           
                                if notas[k] in range(21):
                                    info_alumnos[1][contador].append(notas[k])
                                    validacion_nota=1
                                else:
                                    print("Nota no valida, debe ingresar notas de 0 a 20")
                            validacion_nota=0
                        else:
                            while(validacion_nota==0):
                                notas[k]=int(input("Final: "))
                            
                                if notas[k] in range(21):
                                    info_alumnos[1][contador].append(notas[k])
                                    validacion_nota=1
                                else:
                                    print("Nota no valida, debe ingresar notas de 0 a 20")
                            validacion_nota=0
                    print(notas)
                    contador=len(info_alumnos[0])
                else:
                    print("Las notas del alumno "+alumno+" ya fueron ingresadas")
                    print(info_alumnos[1][contador])  
                    contador=len(info_alumnos[0])
            else:
                contador=contador+1
                if (contador==len(info_alumnos[0])):
                    print("No existe el alumno")
    def accion_eliminar_modificar_nota(self,info_alumnos,contador,alumno,opcion):
        validacion_nota=0 
        while True:
            os.system('cls')
            print("Eliga la accion a realizar")
            print ("\t1 - Eliminar nota")
            print ("\t2 - Modificar nota")
            print ("\t3 - Cancelar")
            opcion1=input("Eliga una opcion ...\n")
            int_opcion=int(opcion)   
            if opcion1=="1":   
                    info_alumnos[1][contador][int_opcion-1]=None
                    print("Se elimino la nota del alumno ",alumno)
                    time.sleep(8)
            elif opcion1=="2":
                while(validacion_nota==0):
                    nueva_nota=int(input("Ingrese nueva nota"))
                    if (nueva_nota in range(21)):
                        antigua_nota=info_alumnos[1][contador][int_opcion-1]
                        info_alumnos[1][contador][int_opcion-1]=nueva_nota 
                        print("Se modifico la nota: "+str(antigua_nota)+" → "+str(info_alumnos[1][contador][int_opcion-1]))
                        time.sleep(8)
                        validacion_nota=1
                    else:
                        print("Nota no valida, debe ingresar notas de 0 a 20") 
                validacion_nota=0 
                print("Se modifico nota del alumno ",alumno)
                time.sleep(8)
            elif opcion1=="3":
                break
            else:
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")            

    def ver_notas_seccion(self,info_alumnos,seccion):
        print("Notas de la sección "+str(seccion))
        print(info_alumnos[1])

    def eliminar_modificar_notas(self,info_alumnos,x,alumno,lista_secciones):
        vacio=[]
        contador=0
        while (contador!=len(info_alumnos[0])):
            if alumno in info_alumnos[0][contador].nombre:
                if(info_alumnos[1][contador]!=vacio):
                    os.system('cls')
                    print("Notas del alumno",alumno)
                    print ("\t1 - pc1:",info_alumnos[1][contador][0])
                    print ("\t2 - pc2:",info_alumnos[1][contador][1])
                    print ("\t3 - pc3:",info_alumnos[1][contador][2])
                    print ("\t4 - pc4:",info_alumnos[1][contador][3])
                    print ("\t5 - parcial:",info_alumnos[1][contador][4])
                    print ("\t6 - final:",info_alumnos[1][contador][5])
                    print ("\t7 - Todas las notas")
                    print ("\t9 - regresar")
                    opcion=input("Eliga una opcion para eliminar/modificar...\n") 
                    if opcion!="7":
                        lista_secciones[x].accion_eliminar_modificar_nota(info_alumnos,contador,alumno,opcion)
                    elif opcion=="7":
                        continuar=input("Se eliminaran las notas del alumno "+alumno+". ¿Desea continuar? (1→SI / 0→NO):")  
                        continuar_validacion=validacion_confirmación(continuar)
                        if (continuar_validacion=='1'):
                            for j in range(6):
                                info_alumnos[1][contador][j]=None           
                            print("Se eliminaron las notas del alumno "+alumno) 
                    elif opcion=="9":
                        contador=len(info_alumnos[0])
                        break
                    else:
                        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
                    break
                else:
                    print("No hay notas aun a modificar")
                    break
            else:
                contador=contador+1
                if (contador==len(info_alumnos[0])):
                    print ("No se encuentra el alumno "+alumno+" en la seccion")

    def inicializar_notas(self,columna,info_alumnos):    #inicializando las notas para que haya listas vacias en la columna notas (sino marca error)
        for j in range(len(info_alumnos[0])):
            notas=[]
            info_alumnos[columna].append(notas)

    def inicializar_notas_min_pc(self,notas_min_pc,info_alumnos):
        for j in range(len(info_alumnos[0])):
                notas=[]
                notas_min_pc.append(notas)

    def promedio_alumnos(self,info_alumnos,alumno):
        min_valor=[]
        vacio=[]
        contador=0
        while (contador!=len(info_alumnos[0])):
            if alumno in info_alumnos[0][contador].nombre:
                for j in range(4):#lee las 4 primeras notas
                    a=info_alumnos[1][contador][j]
                    min_valor.append(a)
                menor=min(min_valor) 
                notapcs=0
                if info_alumnos[1][contador]!=vacio:
                    for j in range(4):
                        if (info_alumnos[1][contador][j]==menor or info_alumnos[1][contador][j]==None):#no lee la nota menor o notas vacias (None)
                            notapcs=notapcs
                        else:
                            notapcs=info_alumnos[1][contador][j]+notapcs
                    notapcs=notapcs/3
                    info_alumnos[2][contador]=round((notapcs+info_alumnos[1][contador][4]+info_alumnos[1][contador][5])/3,2)#alumnos[1][x][4]→parcial, alumnos[1][x][5]→final
                    print("Promedio final del alumno "+str(info_alumnos[0][contador].nombre)+" es: "+str(info_alumnos[2][contador]))
                    contador=len(info_alumnos[0])   
            else:
                contador=contador+1
                if (contador==len(info_alumnos[0])):
                    print ("No se encuentra el alumno "+alumno+" en la seccion")
class Alumno:
    def __init__(self,nombre,nseccion,curso):
            self.nombre=nombre
            self.nseccion=nseccion
            self.curso=curso

class Notas:
    #info_alumnos[0][n]= Alumno(nombreAlumno,nseccion,curso)
    #info_alumnos[1][n]= Alumno(nombreAlumno,nseccion,curso)
    def __init__(self,alumno):
        self.alumno=alumno

    
    

    
                
       
