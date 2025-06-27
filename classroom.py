import random

class Classroom:
    def __init__(self, classroom_id=None, classroom_name="", capacity=0):
        self.classroom_id = classroom_id
        self.classroom_name = classroom_name
        self.capacity = capacity
        self.__classroom_id_list = []
        self.__classrooms = []

    # Método para generar el código único del aula
    def generate_classroom_id(self):
        while True:
            number = random.randint(1, 200)
            if number not in self.__classroom_id_list:
                self.__classroom_id_list.append(number)
                break
        return number

    # Método para buscar un aula por su código
    def search_classroom(self, classroom_id):
        for j in range(len(self.__classrooms)):
            if self.__classrooms[j].classroom_id == classroom_id:
                return j
        return -1

    # Método para validar los datos del aula
    def validate_classroom_data(self, classroom_id, classroom_name, capacity):
        if self.search_classroom(classroom_id) != -1:
            print("El código del aula ya se encuentra registrado")
            return False
        if not classroom_name:
            print("El nombre del aula no puede estar vacío")
            return False
        if not isinstance(capacity, int) or capacity <= 0:
            print("La capacidad debe ser un número entero positivo")
            return False
        return True

    # Método para registrar el aula
    def register_classroom(self, classroom):
        if classroom.classroom_id is None:
            classroom.classroom_id = self.generate_classroom_id()
        if self.search_classroom(classroom.classroom_id) == -1:
            self.__classrooms.append(classroom)
            return True
        return False

    # Método para modificar los datos del aula
    def modify_classroom(self, classroom_id, new_name=None, new_capacity=None):
        idx = self.search_classroom(classroom_id)
        if idx == -1:
            print("Aula no encontrada.")
            return False
        classroom = self.__classrooms[idx]
        if new_name:
            classroom.classroom_name = new_name
        if new_capacity is not None:
            classroom.capacity = new_capacity
        print("Aula modificada correctamente.")
        return True

    # Método para habilitar un aula
    def enable_classroom(self, classroom_id):
        idx = self.search_classroom(classroom_id)
        if idx == -1:
            print("Aula no encontrada.")
            return False
        self.__classrooms[idx].enabled = True
        print("Aula habilitada.")
        return True

    # Método para deshabilitar un aula
    def disable_classroom(self, classroom_id):
        idx = self.search_classroom(classroom_id)
        if idx == -1:
            print("Aula no encontrada.")
            return False
        self.__classrooms[idx].enabled = False
        print("Aula deshabilitada.")
        return True

    # Método para listar todas las aulas
    def list_classrooms(self):
        if not self.__classrooms:
            print("No hay aulas registradas.")
            return
        for c in self.__classrooms:
            estado = getattr(c, 'enabled', True)
            print(f"ID: {c.classroom_id} | Nombre: {c.classroom_name} | Capacidad: {c.capacity} | Estado: {'Habilitada' if estado else 'Deshabilitada'}")

    # Método para visualizar los detalles de un aula
    def view_classroom(self, classroom_id):
        idx = self.search_classroom(classroom_id)
        if idx == -1:
            print("Aula no encontrada.")
            return
        c = self.__classrooms[idx]
        estado = getattr(c, 'enabled', True)
        print(f"ID: {c.classroom_id}\nNombre: {c.classroom_name}\nCapacidad: {c.capacity}\nEstado: {'Habilitada' if estado else 'Deshabilitada'}")

    # Procedimiento vacío para ser llamado desde el menú principal
    def classroom_procedure(self):
        pass