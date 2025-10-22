# Agenda de contacto

def mostrar_menu():
    print("\nAgenda de contacto: ") #SALTO DE LINEA
    print("1.Agregar nuevo contacto: ")
    print("2.Eliminar contacto existente: ")
    print("3.Buscar contacto ")
    print("4.Lista de contactos ")
    print("5.Salir del programa ")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Por favor ingrese el nombre completo del contacto: ")
    telefono = input("Por favor ingrese el numero de telefono del contacto: ")
    email = input("Por favor ingrese email del contacto:")
    agenda[nombre] = {"telefono": telefono, "email": email} # SE USA DE KEY EL NOMBRE DE LA AGENDA PARA BUSCAR CONTACTO Y NOS ENTREGA INFORMACION TOTAL (TELEFONO, EMAIL)

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"el nombre{nombre} ha sido eliminado exitosamente")

    else:
        print(f"El nombre{nombre} no se encuentra en la agenda")

def buscar_contacto(agenda):
    nombre = input("Por favor ingrese el nombre de la agenda que desea buscar: ")
    if nombre in agenda:
        print(f"nombre: {nombre}")
        print(f"telefono: {agenda [nombre] ['telefono']}")
        print(f"email: {agenda [nombre] ['email']}")
    
    else:
        print(f"el nombre {nombre} no se encuentra en la agenda")

def listar_contactos(agenda):
    if agenda: # TAL CUAL COMO SALE AQUI SIGNIFICA QUE HAY INFORMACION DENTRO DE LA AGENDA
        print("\nLista de contactos: ")
        for nombre, info in agenda.items(): #ITEMS DEVUELVE LISTA DE CLAVE - VALOR QUE HAY DICCIONARIO
            print(f"nombre: {nombre}")
            print(f"Telefono: {info ["telefono"]}")
            print(f"Email:{info["email"]}")
            print("-" * 20) #separador de linea y luego se multiplica por 20
    else:
        print("La agenda aun se encuentra vacia")

        


def agenda_contacto():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)

        elif opcion == "2":
            eliminar_contacto(agenda)
        
        elif opcion == "3":
            buscar_contacto(agenda)

        elif opcion == "4":
            listar_contactos(agenda)
        
        elif opcion == "5":
            print("Saliendo del programa")
            break # SALE DEL BUCLE


        else:
            print("Selecciona una opcion valida: (Seleccione una opcion del 1 al 5)")

agenda_contacto()

