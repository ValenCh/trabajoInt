from Tad_Empresa import *
from Tad_Cola import *

empresa=CrearEmpresa()

def menu ():
    print("1. Para agregar un cliente\n")
    print("2. Para modificar un cliente\n")
    print("3. Para eliminar un cliente\n")
    print("0. Para salir\n")
    op = int(input("Ingrese a continuacion la opcion que desea realizar: "))
    return op

def agregarCliente():
    cliente = crearCliente()
    num= int(input("Ingrese el numero de cliente: "))
    dni= int(input("Ingrese el dni del cliente: "))
    ape=input("Ingrese el apellido del cliente: ")
    nom=input("Ingrese el nombre del cliente: ")
    fecha=int(input("Ingrese la fecha de alta del cliente ddmmaaaa"))
    service=input("Ingrese el tipo de servicio")
    price=float(input("Ingrese el precio del servicio contratado"))
    cargarCliente(cliente,num,dni,ape,nom,fecha,service,price)
    agregarCliente(empresa,cliente)

def buscarCliente(num):
    tam = Tamanio(empresa)
    for i in range (tamanio): 
        c=RecuperarCliente(i)
        if (verNumero(c) == num):
            return c
    return -1 #tomamos -1 como si el numero de cliente que se busco no se encontro

def modificarCliente(numero):
    c = buscarCliente(numero)
    mod = input("que aspecto desea modificar: Nombre, Apellido, DNI, Tipo de servicio (tipo) o Precio: ").lower
    if mod == "nombre" : 
        ModiNombre(c, input("Ingrese el nuevo nombre "))
    elif mod == "apellido":
        ModiApellido(c, input("Ingrese el nuevo apellido "))
    elif mod == "dni":
        ModiDni(c,int(input("Ingrese el nuevo DNI")))
    elif mod == "tipo":
        ModiTipo(c,input("Ingrese el nuevo tipo de servicio"))
    else:
        ModiPrecio(c,float(input("Ingrese el nuevo precio del servicio")))

def borrarCliente(numero):
    c = RecuperarCliente(numero)
    if (Existe(empresa,c)):
        EliminarCliente(empresa,c)
        print("Cliente eliminado con exito\n")
    else: 
        print("No se encontro el cliente, volviendo al menu\n")

print("--------------- BIENVENIDO ---------------\n")
op = menu()
while (op != 0): 
    #invoca a la funcion que elija el usuario
    if op == 1: 
        agregarCliente
    elif op == 2: 
        numCliente = int(input("Ingrese el numero del cliente que desea modificar: "))
        modificarCliente(numCliente)
    elif op == 3:
        numCliente = int(input("Ingrese el numero del cliente que desea modificar: "))
        borrarCliente(numCliente)
    else:
        print("Opcion incorrecta, vuelva a seleccionar otra\n")
    op = menu()