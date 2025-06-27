#Espacio para importar las librerias necesarias para el funcionamiento del programa
from os import system
import random

#Creamos la clase principal del archivo grade.py (Grade)
class Grade:

    #Inicializamos el constructor de la clase
    def __init__(self, grade_id=None, grade_name="", grade_students_quantity=0):
        self.__grade_id = grade_id
        self.__grade_name = grade_name
        self.__grade_students_quantity = grade_students_quantity
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


    #Metodo para verificar si el grado ingresado es valido
    def is_valid_grade(self, grade):
        return grade in self.__grades

    #Metodo para generar el id del grado sin que se repita
    def generate_grade_id(self):
        if len(self.__grade_ids) >= 200:
            print("Ya se han usado todos los IDs disponibles para los grados")
            return None
        while True:
            number = random.randint(1, 200)
            if number not in self.__grade_ids:
                self.__grade_ids.append(number)
                return number
    
    #Metodo para buscar un grado por su id
    def search_grade(self, grade_id):
        for i in range(len(self.__grades)):
            if grade_id == self.__grades[i].get_all_grade_ids():
                return i
        return -1

    #Metodo para validar los datos del registro del grado
    def validate_grade_data(self, grade_id, grade_name, grade_students_quantity):
        #Validamos que el id del grado sea unico
        if self.search_grade(grade_id) != -1:
            print("El id del grado ya se encuentra registrado")
            return False
        #Validamos que el nombre del grado no este vacio
        if not grade_name:
            print("El nombre del grado no puede estar vacío")
            return False
        #Validamos que la cantidad de estudiantes sea un numero positivo
        if grade_students_quantity <= 0 or not isinstance(grade_students_quantity, int):
            print("La cantidad de estudiantes debe ser un número positivo")
            return False
        return True
    
    #Creamos el metodo para registrar el grado
    def register_grade(self, grade):
        if self.search_grade(grade.get_grade_id()) == -1:
            self.__grades.append(grade)
            return True
        return False