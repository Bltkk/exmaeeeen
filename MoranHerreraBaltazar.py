
trabajadores= [["nombre: " "baltazar mora"],
                   ["nombre: " "juan pedro"],
                   ["nombre: " "elva surita"],
                   ["nombre: " "matias dolor"],
                   ["nombre: " "juana de arocs"],
                   ["nombre: " "sofia cerda "],
                   ["nombre: " "julieta del campo"],
                   ]   

sueldos=[]
trabajadores_sueldo=[]

def asignar_sueldos():    
    for b in trabajadores:
        sueldos.append(("sueldos: " ))
    for sueldos in trabajadores:
        if sueldos["sueldo: "] <2500000:
            trabajadores_sueldo= + sueldos
    
    return print("sueldo", trabajadores_sueldo)

    
    
def clasificar_sueldos():
    sueldos_800=[]
    sueldos_2000=[]
    sueldos_mas=[]
    for x in trabajadores_sueldo:
        if trabajadores_sueldo <800000:
            sueldos_800 =+1
            print("Sueldos menores a 800.000", trabajadores_sueldo,"total", sueldos_800)
        elif trabajadores_sueldo >800000  <2000000:
            sueldos_2000 =+1
            print("Sueldos entre 800.000 y 2.000.000",trabajadores_sueldo,"TOTAL",sueldos_2000)
        elif trabajadores_sueldo >2000000:
            sueldos_mas =+1
            print("sueldo mayores a 2.000.000",trabajadores_sueldo,"total",sueldos_mas)



def ver_estadisticas():
    sueldo_maximo=max(sueldos)
    sueldo_medio=sum(sueldos)
    sueldo_minimo=min(sueldos)
    media_geometrica=pow(sueldos,)
    print("el sueldo maximo", sueldo_maximo)
    print("sueldo medio", sueldo_medio)
    print("sueldo minimo", sueldo_minimo)

def reporte_sueldos():
    print("sueldos ",sueldos, "descuenta salud",descuento_salud, "descuento afp ",descuento_afp)
    descuento_salud= trabajadores_sueldo*0.07
    descuento_afp = trabajadores_sueldo*0.17
    print("probadno")

def salir():
    print(""" 
                    Finalizando programa...
                    Desarrollado por Baltazar Moran
                    Rut 21.089.257-5
                    """)
    
def menu():
    A=int(input("""1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa
"""))
    return A


while True:
    try:
        A=menu()
        if  A== 1:
            asignar_sueldos()
        elif A ==2:
            clasificar_sueldos()
        elif A ==3:
            ver_estadisticas()
        elif A ==4:
            reporte_sueldos()
        elif A ==5:
            salir()
            break  
    except:
        print("algo valido ")

#excelente trabajo un 7 