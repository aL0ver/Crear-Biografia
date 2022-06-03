

""" 
Crear una biografia
        ° Pedir y verificar el nombre
        ° Pedir y verificar la edad
        ° Pedir y verificar fecha de nacimiento
                ° Año
                ° Mes
                        ° Si escribe el mes en forma de palabra: 
                                ° Verificar
                                ° Si esta bien escrito:
                                        ° Convertir a minuscula
                                                ° Verificar
                        ° Si escribe el mes como integer: 
                                Convertir  el  integer en el mes correspondiente 
                ° Dia
        ° Pedir lugar de nacimiento 
        Pedir sueño/ aspiracion del usuario
        Imprimir formato de biografia:
        "Nombre: _
         Edad: _
         Fecha de nacimiento: _
         Lugar de nacimiento: _
         Metas personales: _
        "
"""
def toLowerCase(text):
        lowerCase = text.lower()
        return lowerCase
actual_age = 2022
months = ["Enero" , "Febrero" , "Marzo" , "Abril" , "Junio" , "Julio" , "Agosto" , "Septiembre" , "Octubre" , "Novienbre" , "Diciembre"]

while True:
        while True:
                username = input("Ingrese su nombre de pila: ")
                if username.isalpha() == False:
                        print("Tu nombre solo debe contener letras")         
                else: break
        while True:        
                last_username = input("Ingrese su apellido: ")
                if last_username.isalpha() == False:
                        print("Tu apellido solo debe contener letras")                     
                else: break 
        while True:
                born_age = input("Ingrese el año de su nacimiento: ")
                if born_age.isdigit() == True:  
                        if int(born_age) in range (1900,2022):
                                years_old = actual_age - int(born_age)
                                break
                        else:
                                print("Tu fecha año de nacimiento debe estar entre el año 1900 y 2022")
                else: 
                        print("Ingrese el año de forma numerica")
        while True:
                born_month = input("Ingrese su mes de nacimiento: ")
                if born_month.isdigit() == True: # en caso de que la entrada sea numero
                        if int(born_month) < 13:
                                number_month = int(born_month)
                                break
                        else: 
                                print(f"Un año no tiene {born_month} meses")
                                continue 
                elif born_month.isalpha() == True: # en caso de que la entrada sea alfabeto 
                        number_month = 0
                        same = 0
                        for month in months:
                                number_month += 1
                                if toLowerCase(born_month) == toLowerCase(month):
                                        same +=1
                                        break
                        if same == 1:
                                break
                        else: 
                                print("Ha escrito de manera incorrecta el mes")
                                continue
                else:
                        print("Tu entrada no es valida ")
        while True:
                born_day = input("Ingrese el dia de su nacimiento: ")
                if born_day.isdigit() == True:
                        if int(born_day) <= 31:
                                if int(born_day) > 28 and born_month == 2:
                                        print("Febrero no puede tener mas de 28 dias")
                                        continue
                                else:
                                        break
                        else:
                                print(f"Los meses no tienen {born_day} dias") 
                else:
                        print(f"{born_day} no es un numero entero")
        while True:
                born_place = input("Ingrese el pais donde nacio: ")
                if born_place.isalpha() == True:
                        break 
                else:
                        print("El pais no puede contener numeros ni espacios")
        while True:
                meta = input("Igrese cual son sus metas en la vida: ")
                if meta.isdigit() == True or meta.isdecimal() == True:
                        continue 
                else: 
                        break
        print(f"Nombre: {username} {last_username}")
        print(f"Edad: {years_old}")
        print(f"Fecha de nacimiento: {months[number_month-1]} {born_day}, {born_age}.")
        print(f"Lugar de nacimiento: {born_place}")
        if meta == "":
                print = (f"Metas personales: No registro ninguna meta.")
        else:        
                print(f"Metas personales: {meta}")
