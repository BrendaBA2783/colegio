import random

class Subject:
    def __init__(self, subject_id=None, subject_name=""):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.__subject_id_list = []
        self.__subjects = []

    # Método para generar el código único de la materia
    def generate_subject_id(self):
        while True:
            number = random.randint(1, 200)
            if number not in self.__subject_id_list:
                self.__subject_id_list.append(number)
                break
        return number

    # Método para buscar una materia por su código
    def search_subject(self, subject_id):
        for j in range(len(self.__subjects)):
            if self.__subjects[j].subject_id == subject_id:
                return j
        return -1

    # Método para validar los datos de la materia
    def validate_subject_data(self, subject_id, subject_name):
        if self.search_subject(subject_id) != -1:
            print("El código de la materia ya se encuentra registrado")
            return False
        if not subject_name:
            print("El nombre de la materia no puede estar vacío")
            return False
        return True

    # Método para registrar la materia
    def register_subject(self, subject):
        if subject.subject_id is None:
            subject.subject_id = self.generate_subject_id()
        if self.search_subject(subject.subject_id) == -1:
            self.__subjects.append(subject)
            return True
        return False

    # Método para modificar el nombre de la materia
    def modify_subject(self, subject_id, new_name=None):
        idx = self.search_subject(subject_id)
        if idx == -1:
            print("Materia no encontrada.")
            return False
        subject = self.__subjects[idx]
        if new_name:
            subject.subject_name = new_name
        print("Materia modificada correctamente.")
        return True

    # Método para habilitar una materia
    def enable_subject(self, subject_id):
        idx = self.search_subject(subject_id)
        if idx == -1:
            print("Materia no encontrada.")
            return False
        self.__subjects[idx].enabled = True
        print("Materia habilitada.")
        return True

    # Método para deshabilitar una materia
    def disable_subject(self, subject_id):
        idx = self.search_subject(subject_id)
        if idx == -1:
            print("Materia no encontrada.")
            return False
        self.__subjects[idx].enabled = False
        print("Materia deshabilitada.")
        return True

    # Método para listar todas las materias
    def list_subjects(self):
        if not self.__subjects:
            print("No hay materias registradas.")
            return
        for s in self.__subjects:
            estado = getattr(s, 'enabled', True)
            print(f"ID: {s.subject_id} | Nombre: {s.subject_name} | Estado: {'Habilitada' if estado else 'Deshabilitada'}")

    # Método para visualizar los detalles de una materia
    def view_subject(self, subject_id):
        idx = self.search_subject(subject_id)
        if idx == -1:
            print("Materia no encontrada.")
            return
        s = self.__subjects[idx]
        estado = getattr(s, 'enabled', True)
        print(f"ID: {s.subject_id}\nNombre: {s.subject_name}\nEstado: {'Habilitada' if estado else 'Deshabilitada'}")

    # Procedimiento vacío para ser llamado desde el menú principal
    def subject_procedure(self):
        pass

