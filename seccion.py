#creando la sección de clases

#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
info_alumnos=[[],[],[]]#[[alumnos],[notas],[nota final]]
notas_max_min=[[]]#[alumno][1]→ nota menor,[alumno][0]→ nota mayor .Lista de la mejor/menor nota de cada alumno
notas_min_pc=[]#la pc mas baja de cada alumno

print("3 CAMBIO EN GITHUB")

class Seccion:
    def __init__(self,nseccion,curso,profesor):
        self.nseccion=nseccion
        self.curso=curso
        self.profesor=profesor
    #lista_alumnos=[]

    def agregar_alumno(self,info_alumnos,curso,nseccion):
        cond=1
        n=0
        while(cond!=0):
            nalumno=input("Nombre del alumno a ingresar: ")
            if nalumno in info_alumnos[0]:
                print("Ya existe ese alumno")
            #lista_alumnos.append(nalumno)
            else:    
                info_alumnos[0].append(nalumno)#poner al final en la lista de alumnos
                info_alumnos[0][n]= Alumno(nalumno,nseccion,curso)
                #info_alumnos[1].append(nalumno)
                #info_alumnos[1][n]= Notas(nalumno)
                #info_alumnos[1][n]= Notas(nalumno)
                print("Se agrego al alumno: "+nalumno)
            n=n+1
            cond=input("Desea agregar otro alumno (1→SI / 0→NO):")
            cond=int(cond)
            """if cond==0:
                break"""
 
    def quitar_alumno(self,info_alumnos):
        cond=1
        while(cond!=0):
            nalumno=input("Nombre del alumno a eliminar: ")
            if nalumno in info_alumnos[0]:
                info_alumnos[0].remove(nalumno)
                print("Se elimino al alumno: "+nalumno)
            else:
                print("Ya no existe ese alumno")
            cond=input("Desea eiminar otro alumno (1→SI / 0→NO):")
            if cond==0:
                break

    def ver_lista(self,info_alumnos,nseccion):
        print("Lista de alumnos de la seccion "+str(nseccion)+": ")
        i=1
        for x in range(len(info_alumnos[0])):
            print("Alumno n° "+str(i)+" : "+str(info_alumnos[0][x].nombre))
            i=i+1
        return len(info_alumnos[0])
    def mayor_nota(self,info_alumnos):
        print("Mayor nota de la seccion")
        mayor=0
        for i in range(len(info_alumnos[2])):
            if info_alumnos[2][i]>mayor:
                mayor=info_alumnos[2][i]
                notas_max_min[0][i]=mayor
                j=i#guardamos la posicion del alumno con la mas alta nota
        print(mayor+" del alumno "+info_alumnos[0][j])

        print("Tres notas más altas de la seccion")
        mayor2=0
        for i in range(len(info_alumnos[2])):
            if (info_alumnos[2][i]>mayor2 and info_alumnos[2][i]<mayor):
                mayor2=info_alumnos[2][i]
                notas_max_min[0][i]=mayor2
                my2=i#guardamos la posicion del alumno con la mas alta nota
        
        mayor3=0
        for i in range(len(info_alumnos[2])):
            if (info_alumnos[2][i]>mayor3 and info_alumnos[2][i]<mayor and info_alumnos[2][i]<mayor2):
                mayor3=info_alumnos[2][i]
                notas_max_min[0][i]=mayor3
                my3=i#guardamos la posicion del alumno con la mas alta nota
        
        print(mayor+" del alumno "+info_alumnos[0][j])
        print(mayor2+" del alumno "+info_alumnos[0][my2])
        print(mayor3+" del alumno "+info_alumnos[0][my3])

    def menor_nota(self,info_alumnos):
        print("Menor nota de la seccion")
        menor=20
        for i in range(len(info_alumnos[2])):
            if info_alumnos[2][i]<menor:
                menor=info_alumnos[2][i]
                notas_max_min[1][i]=menor
                j=i#guardamos la posicon del alumno con la mas baja nota
        print(menor+" del alumno "+info_alumnos[0][j])
        
        print("Tres notas más altas de la seccion")
        menor2=20
        menor3=20

        for i in range(len(info_alumnos[2])):
            if (info_alumnos[2][i]<menor2 and info_alumnos[2][i]>menor):
                menor2=info_alumnos[2][i]
                notas_max_min[1][i]=menor2
                mn2=i#guardamos la posicion del alumno con la mas alta nota

        for i in range(len(info_alumnos[2])):
            if (info_alumnos[2][i]<menor3 and info_alumnos[2][i]>menor and info_alumnos[2][i]>menor2):
                menor3=info_alumnos[2][i]
                notas_max_min[1][i]=menor3
                mn3=i#guardamos la posicion del alumno con la mas alta nota

        print(menor3+" del alumno "+info_alumnos[0][mn3])
        print(menor2+" del alumno "+info_alumnos[0][mn2])
        print(menor+" del alumno "+info_alumnos[0][j]) 

    

    def ingresar_notas(self,nalumno,pc1,pc2,pc3,pc4,parcial,final):
        
        for j in range(len(info_alumnos[0])):
            if nalumno==info_alumnos[0][j].nombre:
                print(info_alumnos[0][j].nombre)
                notas=[pc1,pc2,pc3,pc4,parcial,final]
                print(notas)
                    #print(i)
                    #print(notas[i])
                #info_alumnos[1][j].append(notas[i])
                print(info_alumnos[1][j])
                info_alumnos[1][j]=notas

                print(str(info_alumnos[0][j].nombre))
                break
            elif (j==(len(info_alumnos[0])-1)):
                print("No esta el alumno "+nalumno)

    def ver_notas(self,info_alumnos,nombre):
        for j in range(len(info_alumnos[0])):
            if nombre==info_alumnos[0][j].nombre:
                print("Notas del alumno "+nombre+" : ")
                print(info_alumnos[1][j])
                break
            elif (j==(len(info_alumnos[0])-1)):
                print("No esta el alumno "+nombre)

    def ver_notas_seccion(self,info_alumnos,seccion):
        print("Notas de la sección "+str(seccion))
        print(info_alumnos[1])

    def inicializar_notas(self,columna):    #inicializando las notas para que haya listas vacias en la columna notas (sino marca error)
        for j in range(len(info_alumnos[0])):
            notas=[]
            info_alumnos[columna].append(notas)
            if (columna==1):
                print("Se inicializo las notas de las pcs del alumno "+str(j+1))  
                print(info_alumnos[columna][j])
            else:
                print("Se inicializo la nota final del alumno "+str(j+1))  
                print(info_alumnos[columna][j])

    def inicializar_notas_min_pc(self,notas_min_pc):

        for j in range(len(info_alumnos[0])):
                notas=[]
                notas_min_pc.append(notas)
                print("Se inicializo la nota mas baja del alumno "+str(j+1))


    def promedio_alumnos(self,info_alumnos,notas_min_pc):
        #minimo=min(info_alumnos)
        #menor=20
        min_valor=[]
        """"
        for j in range(len(info_alumnos[0])):
                a=0
                min_valor.append(a)
        #min_valor.pop(0)
        print(min_valor)"""
        for i in range(len(info_alumnos[0])):
            for j in range(4):#lee las 4 primeras notas
                print("ttttttttttttttttttttt")
                a=info_alumnos[1][i][j]
                print(a)
                min_valor.append(a)
                print(min_valor[j])
            print("las 4 pcs")
            print(min_valor)
            menor=min(min_valor)
            print("ffffffffffffffff")
            print(menor)
            notas_min_pc[i]=menor
            print(notas_min_pc[i])
            print(notas_min_pc)
            min_valor=[]
        """notapcs=0
        #eliminando y guardando la pc más baja de cada alumno
        menor=20 #es tipo int o entero

        for x in range(len(info_alumnos[1])):
            for j in range(4):
                a=int(info_alumnos[1][x][j])#a es entero o int
                print("-----------------------------------------------------------")
                print(a)
                print(type(a))

                if a<menor:#if int(info_alumnos[1][x][j])<menor:
                    
                    print("=================================================")
                    print(notas_min_pc[x])
                    menor=notas_min_pc[x]#aca se convierte en lista, menor es tipo lista
                    print(menor)
                    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
                    print(type(menor))
                    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")              
            notas_min_pc[x] = menor  #guardando la nota mas baja de cada alumno
            menor=20 """
        #poniendo las notas finales de cada alumno
        notapcs=0
        for x in range(len(info_alumnos[1])):  
            for j in range(4):
                if info_alumnos[1][x][j]==notas_min_pc[x]:#no lee la nota menor
                    notapcs=notapcs
                else:
                    notapcs=info_alumnos[1][x][j]+notapcs
                print (notapcs)
            notapcs=notapcs/3
            info_alumnos[2][x]=(notapcs+info_alumnos[1][x][4]+info_alumnos[1][x][5])/3#alumnos[1][x][4]→parcial, alumnos[1][x][5]→final
            print("Promedio final del alumno "+str(info_alumnos[0][x].nombre)+" es: "+str(info_alumnos[2][x]))
            notapcs=0

class Alumno:
    def __init__(self,nombre,nseccion,curso):
            self.nombre=nombre
            self.nseccion=nseccion
            self.curso=curso


class Notas:
    #info_alumnos[0][n]= Alumno(nalumno,nseccion,curso)
    #info_alumnos[1][n]= Alumno(nalumno,nseccion,curso)
    def __init__(self,alumno):
        self.alumno=alumno
    
    

    
                
       