#Espacio para importar las librerias necesarias para el funcionamiento del programa
from os import system
import random

#Creamos la clase principal del archivo grade.py (Grade)
class Grade:

    #Inicializamos el constructor de la clase
    def __init__(self, grade_id=None, grade_name="", grade_students_quantity=0, enabled=True):
        self.__grade_id = grade_id
        self.__grade_name = grade_name
        self.__grade_students_quantity = grade_students_quantity
        self.enabled = enabled
        self.__grade_ids = []
        self.__grades = []

    #Metodos getters para los atributos privados (Obtener los valores de los atributos)
    #Obtener el id del grado
    def get_grade_id(self):
        return self.__grade_id
    
    #Obtener el nombre del grado
    def get_grade_name(self):
        return self.__grade_name
    
    #Obtener la cantidad de estudiantes del grado
    def get_grade_students_quantity(self):
        return self.__grade_students_quantity
    
    #Obtener la lista de ids de grados registrados
    def get_all_grade_ids(self):
        return self.__grade_ids
    
    #Metodos setters para los atributos privados (Modificar los valores de los atributos)
    def set_grade_name(self, new_name):
        self.__grade_name = new_name

    def set_students_quantity(self, new_quantity):
        self.__grade_students_quantity = new_quantity


    #Metodo para verificar si el grado ingresado es valido
    def is_valid_grade(self, grade):
        return grade in self.__grades

    #Metodo para generar el id del grado sin que se repita
    def generate_grade_id(self):
        if len(self.__grade_ids) >= 200:
            print("\033[91m\nYa se han usado todos los IDs disponibles para los grados")
            return None
        while True:
            number = random.randint(1, 200)
            if number not in self.__grade_ids:
                self.__grade_ids.append(number)
                return number
    
    #Metodo para buscar un grado por su id
    def search_grade(self, grade_id):
        for i in range(len(self.__grades)):
            if grade_id == self.__grades[i].get_grade_id():
                return i
        return -1

    #Metodo para validar los datos del registro del grado
    def validate_grade_data(self, grade_id, grade_name, grade_students_quantity):
        #Validamos que el id del grado sea unico
        if self.search_grade(grade_id) != -1:
            print("\033[91m\nEl id del grado ya se encuentra registrado")
            return False
        #Validamos que el nombre del grado no este vacio
        if not grade_name:
            print("\033[91m\nEl nombre del grado no puede estar vacío")
            return False
        #Validamos que la cantidad de estudiantes sea un numero positivo
        if grade_students_quantity < 0 or not isinstance(grade_students_quantity, int) or grade_students_quantity > 10:
            print("\033[91m\nLa cantidad de estudiantes debe ser un número positivo y menor o igual a 10")
            return False
        return True
    
    #Creamos el metodo para registrar el grado
    def register_grade(self, grade, grade_id):
        if self.search_grade(grade.get_grade_id()) == -1:
            self.__grades.append(grade)
            self.__grade_ids.append(grade_id)
            return True
        return False
    
    #Metodo para modificacion del grado 
    def modify_grade(self, grade_id):
        position_id = self.search_grade(grade_id)
        if position_id == -1:
            print("\033[91m\nEl id del grado no se encuentra registrado")
            return False
        
        grade = self.__grades[position_id]
        print("\033[0m\nSeleccione el dato que desea modificar: ")
        print("1. Nombre del grado")
        print("2. Cantidad de estudiantes del grado")

        try:
            option = int(input("\nIngrese la opción: "))
        except ValueError:
            print("\033[91m\nError: Debe ingresar un dato válido")
            return False
        
        if option == 1:
            new_name = input("\033[0mIngrese el nuevo nombre del grado: ")

            if not new_name.strip():
                print("\033[91m\nEl nombre del grado no puede estar vacío")
                return False

            if any(char.isdigit() for char in new_name):
                print("\033[91m\nEl nombre del grado no debe contener números")
                return False

            grade.set_grade_name(new_name) 

        elif option == 2:
            try:
                new_quantity = int(input("\033[0mIngrese la nueva cantidad de estudiantes del grado: "))
                if new_quantity <= 0 or new_quantity > 10:
                    print("\033[91m\nLa cantidad de estudiantes debe ser un número positiva y menor a 11")
                    return False

                grade.set_students_quantity(new_quantity) 

            except ValueError:
                print("\033[91m\nError: Debe ingresar un dato válido")
                return False
        return True

    #Metodo para listar el grado
    def list_grades(self):
        if not self.__grades:
            print("\033[91m\nNo hay grados registrados")
            return False
        for grade in self.__grades:
            grade_state = "Habilitado" if getattr(grade, 'enabled', True) else "Deshabilitado"
            print(f"\033[0m\nID: {grade.get_grade_id()}\nNombre: {grade.get_grade_name()}\nCantidad de estudiantes: {grade.get_grade_students_quantity()}\nEstado: {grade_state}")
        return True
    
    #Metodo para habilitar o deshabilitar el grado
    def enable_grade(self, teacher_id):
        idx = self.search_grade(teacher_id)
        if idx == -1:
            print("\033[91m\nError: Grado no encontrado.")
            return False
        self.__grades[idx].enabled = True
        print("\033[92m\nGrado habilitado")
        return True

    def disable_grade(self, teacher_id):
        idx = self.search_grade(teacher_id)
        if idx == -1:
            print("\033[91m\nError: Grado no encontrado.")
            return False
        self.__grades[idx].enabled = False
        print("\033[92m\nGrado deshabilitado")
        return True
    
    #visualizar grados
    def view_grade(self, teacher_id):
        idx = self.search_grade(teacher_id)
        if idx == -1:
            print("\033[91m\nError: Grado no encontrado.")
            return False
        grade = self.__grades[idx]
        grade_state = "Habilitado" if getattr(grade, 'enabled', True) else "Deshabilitado"
        print(f"\033[0m\nID: {grade.get_grade_id()}\nNombre: {grade.get_grade_name()}\nCantidad de estudiantes: {grade.get_grade_students_quantity()}\nEstado: {grade_state}")
        return True