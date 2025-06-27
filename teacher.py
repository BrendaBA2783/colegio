# Sección para todas las importaciones necesarias
import random

# Creamos la clase principal
class Teacher:
    def __init__(self, teacher_id=None, teacher_name="", teacher_last_name="", subject="", classroom=""):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_last_name = teacher_last_name
        self.subject = subject
        self.classroom = classroom
        self.__teacher_id_list = []
        self.__teachers = []


    # Método para generar el código único del docente
    def generate_teacher_id(self):
        while True:
            number = random.randint(1, 200)
            if number not in self.__teacher_id_list:
                self.__teacher_id_list.append(number)
                break
        return number

    # Método para buscar un docente por su código
    def search_teacher(self, teacher_id):
        for j in range(len(self.__teachers)):
            if self.__teachers[j].teacher_id == teacher_id:
                return j
        return -1

    # Método para validar los datos del registro del docente
    def validate_teacher_data(self, teacher_id, teacher_name, teacher_last_name, subject, classroom):
        # Validamos que el código del docente sea único
        if self.search_teacher(teacher_id) != -1:
            print("El código del docente ya se encuentra registrado")
            return False
        # Validamos que el nombre y el apellido del docente no estén vacíos ni contengan números
        if not teacher_name or any(char.isdigit() for char in teacher_name):
            print("El nombre no puede estar vacío ni contener números")
            return False
        if not teacher_last_name or any(char.isdigit() for char in teacher_last_name):
            print("El apellido no puede estar vacío ni contener números")
            return False
        # Validamos que la materia y el aula no estén vacíos
        if not subject:
            print("La materia no puede estar vacía")
            return False
        if not classroom:
            print("El aula no puede estar vacía")
            return False
        return True

    # Método para registrar al docente
    def register_teacher(self, teacher):
        # Si el docente no tiene id, se le asigna uno único
        if teacher.teacher_id is None:
            teacher.teacher_id = self.generate_teacher_id()
        if self.search_teacher(teacher.teacher_id) == -1:
            self.__teachers.append(teacher)
            return True
        return False

    def modify_teacher(self, teacher_id, new_name=None, new_last_name=None, new_subject=None, new_classroom=None):
        idx = self.search_teacher(teacher_id)
        if idx == -1:
            print("Docente no encontrado.")
            return False
        teacher = self.__teachers[idx]
        if new_name:
            teacher.teacher_name = new_name
        if new_last_name:
            teacher.teacher_last_name = new_last_name
        if new_subject:
            teacher.subject = new_subject
        if new_classroom:
            teacher.classroom = new_classroom
        print("Docente modificado correctamente.")
        return True

    def enable_teacher(self, teacher_id):
        idx = self.search_teacher(teacher_id)
        if idx == -1:
            print("Docente no encontrado.")
            return False
        self.__teachers[idx].enabled = True
        print("Docente habilitado.")
        return True

    def disable_teacher(self, teacher_id):
        idx = self.search_teacher(teacher_id)
        if idx == -1:
            print("Docente no encontrado.")
            return False
        self.__teachers[idx].enabled = False
        print("Docente deshabilitado.")
        return True

    def list_teachers(self):
        if not self.__teachers:
            print("No hay docentes registrados.")
            return
        for t in self.__teachers:
            estado = getattr(t, 'enabled', True)
            print(f"ID: {t.teacher_id} | Nombre: {t.teacher_name} {t.teacher_last_name} | Materia: {t.subject} | Aula: {t.classroom} | Estado: {'Habilitado' if estado else 'Deshabilitado'}")

    def view_teacher(self, teacher_id):
        idx = self.search_teacher(teacher_id)
        if idx == -1:
            print("Docente no encontrado.")
            return
        t = self.__teachers[idx]
        estado = getattr(t, 'enabled', True)
        print(f"ID: {t.teacher_id}\nNombre: {t.teacher_name} {t.teacher_last_name}\nMateria: {t.subject}\nAula: {t.classroom}\nEstado: {'Habilitado' if estado else 'Deshabilitado'}")

    # Procedimiento vacío para ser llamado desde el menú principal
    def teacher_procedure(self):
        pass
