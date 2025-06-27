#Seccion para todas las importaciones necesarias
import random
from grade import Grade

#Creamos la clase principal
class Student:
    def __init__(self, student_id=None, student_name="", student_last_name="", student_grade=""):
        self.__student_name = student_name
        self.__student_id = []
        self.__student_last_name = student_last_name
        self.__student_grade = student_grade
        self.__students = []
        self.grade = Grade()  
        
    #Metodo para generar el id del estudiante
    def generate_student_id(self):
        while True:
            number = random.randint(1, 200)
            if number not in self.__student_id:
                self.__student_id.append(number)
                break
        return number
    
    #Metodo para buscar un estudiante por su id
    def search_student(self, student_id):
        for j in range(len(self.__students)):
            if self.__students[j].student_id == student_id:
                return j
        return -1

    #Metodo para validar los datos del registro del estudiante
    def validate_student_data(self, student_id, student_grade, student_name, student_last_name):

        #Validamos que el id del estudiante sea unico
        if self.search_student(student_id) != -1:
            print("El id del estudiante ya se encuentra registrado")
            return False
        
        #Validamos que el nombre y el apellido del estudiante no este vacio y con numeros
        if not student_name or any(char.isdigit() for char in student_name):
            print("El nombre no puede estar vacío ni contener números")
            return False
        if not student_last_name or any(char.isdigit() for char in student_last_name):
            print("El apellido no puede estar vacío ni contener números")
            return False
        
        #Validamos que el grado del estudiante exista
        if not self.grade.is_valid_grade(student_grade):
            print("El grado del estudiante no existe")
            return False

        return True

    #Creamos el metodo para registrar al estudiante 
    def register_student(self, student):
        if self.search_student(student.student_id) == -1:
            self.__students.append(student)
            return True
        return False