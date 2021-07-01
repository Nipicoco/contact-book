import pickle
import os
#utilizado para serializar y deserializar una estructura de objeto de Python.
#En otras palabras, es el proceso de convertir un objeto Python en un flujo de bytes para almacenarlo en un archivo / base de datos
# o mantener el estado del programa en todas las sesiones.
UI = '''
########################
1. Agregar             #
2. Ver lista           #
3. Buscar contacto     #
4. Actualizar contacto #
5. Eliminar contacto   #
6. Guardar y salir     #
########################
'''

#definiremos clases para tener los objetos y definiciones guardadas
class Personas(object):

    def __init__(self, ID=None, nombre=None, telefono=None):
        self.ID = ID
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return "{} {:>5} {:>15}".format(self.ID, self.nombre, self.telefono)

#en este objecto de clase, guardaremos las deficiones para minimizar el uso de codigo en general.
class Oyasuminasai(object):

    def __init__(self, basedatos):
        self.basedatos = basedatos
        self.personas = {}
        if not os.path.exists(self.basedatos):
            puntero = open(self.basedatos, 'wb')
            pickle.dump({}, puntero)
            puntero.close()
        else:
            with open(self.basedatos, 'rb') as person_list:
                self.personas = pickle.load(person_list)

    def agregar(self):
        ID, nombre, telefono = self.detalles()
        if ID not in self.personas:
            self.personas[ID] = Personas(ID, nombre, telefono)
        else:
            print("Contacto ya presente.")

    def ver_todos(self):
        if self.personas:
            print("{} {:>5} {:>23}".format('ID', 'Nombre', 'Telefono'))
            for person in self.personas.values():
                print(person)
        else:
            print("No hay contactos.")

    def buscar(self):
        ID = input("Ingresar el ID: ")
        if ID in self.personas:
            print(self.personas[ID])
        else:
            print("Contacto no encontrado.")
#def del lo usaremos como destructor de datos no deseados
#Una referencia a objetos tambien se elimina cuando el objeto deja de ser referencia o cuando finaliza el programa ejecutado
    def detalles(self):
        ID = input("ID: ")
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        return ID, nombre, telefono
    def detalles2(self):
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        return nombre, telefono
    def actualizar(self):
        ID = input("Ingresar el ID: ")
        if ID in self.personas:
            print("Encontrado. Ingresar nuevos detalles.")
            nombre, telefono = self.detalles2()
            self.personas[ID].__init__(ID, nombre, telefono)
            print("Actualizado con exito.")
        else:
            print("Contact0 no encontrado.")

    def eliminar(self):
        ID = input("Ingresar el ID a eliminar: ")
        if ID in self.personas:
            del self.personas[ID]
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")

#init como constructor o inicializador, y se llama automáticamente cuando crea una nueva clase.
#Dentro de esa función, el objeto recién creado se asigna al parámetro self
    def __del__(self):
        with open(self.basedatos, 'wb') as db:
            pickle.dump(self.personas, db)

    def __str__(self):
        return UI

#aqui ejecutaremos nuestro programa, guardando txt con los datos y mandando los inputs en serie, antes de llamar a las definiciones
def main():
    si = Oyasuminasai('contactos.txt')
    manzanilla = ''
    while manzanilla != '6':
        print(si)
        manzanilla = input('Elegir opcion: ')
        if manzanilla == '1':
            si.agregar()
        elif manzanilla == '2':
            si.ver_todos()
        elif manzanilla == '3':
            si.buscar()
        elif manzanilla == '4':
            si.actualizar()
        elif manzanilla == '5':
            si.eliminar()
        elif manzanilla == '6':
            print("Saliendo del programa.")
        else:
            print("Opcion invalida.")

if __name__ == '__main__':
    main()