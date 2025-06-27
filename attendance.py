import random
from datetime import date

class Attendance:
    def __init__(self, attendance_id=None, attendance_date=None, classroom=None, students=None, teacher=None, subject=None):
        self.attendance_id = attendance_id
        self.attendance_date = attendance_date or date.today()
        self.classroom = classroom
        self.students = students if students is not None else []  # Lista de diccionarios: {'student': obj, 'present': bool, 'excused': bool, 'justification': str}
        self.teacher = teacher
        self.subject = subject
        self.__attendance_id_list = []
        self.__attendances = []

    # Método para generar el código único de la asistencia
    def generate_attendance_id(self):
        while True:
            number = random.randint(1, 10000)
            if number not in self.__attendance_id_list:
                self.__attendance_id_list.append(number)
                break
        return number

    # Método para buscar una asistencia por su código
    def search_attendance(self, attendance_id):
        for j in range(len(self.__attendances)):
            if self.__attendances[j].attendance_id == attendance_id:
                return j
        return -1

    # Método para validar los datos de la asistencia
    def validate_attendance_data(self, attendance_id, attendance_date, classroom, students, teacher, subject):
        if self.search_attendance(attendance_id) != -1:
            print("El código de la asistencia ya se encuentra registrado")
            return False
        if not attendance_date:
            print("La fecha de la asistencia no puede estar vacía")
            return False
        if not classroom:
            print("El aula de clase no puede estar vacía")
            return False
        if not students or not isinstance(students, list):
            print("Debe registrar al menos un estudiante")
            return False
        if not teacher:
            print("El docente encargado no puede estar vacío")
            return False
        if not subject:
            print("La materia no puede estar vacía")
            return False
        return True

    # Método para registrar la asistencia
    def register_attendance(self, attendance):
        if attendance.attendance_id is None:
            attendance.attendance_id = self.generate_attendance_id()
        if self.search_attendance(attendance.attendance_id) == -1:
            self.__attendances.append(attendance)
            return True
        return False

    # Métodos para listar y visualizar asistencias
    def list_attendances(self):
        if not self.__attendances:
            print("No hay asistencias registradas.")
            return
        for a in self.__attendances:
            print(f"ID: {a.attendance_id} | Fecha: {a.attendance_date} | Aula: {a.classroom} | Docente: {a.teacher} | Materia: {a.subject}")

    def view_attendance(self, attendance_id):
        idx = self.search_attendance(attendance_id)
        if idx == -1:
            print("Asistencia no encontrada.")
            return
        a = self.__attendances[idx]
        print(f"ID: {a.attendance_id}\nFecha: {a.attendance_date}\nAula: {a.classroom}\nDocente: {a.teacher}\nMateria: {a.subject}")
        print("Estudiantes:")
        for s in a.students:
            nombre = s['student']
            presente = 'Sí' if s['present'] else 'No'
            excusa = 'Sí' if s.get('excused', False) else 'No'
            justificacion = s.get('justification', '')
            print(f"- {nombre} | Presente: {presente} | Excusa: {excusa} | Justificación: {justificacion}")

    # Procedimiento vacío para ser llamado desde el menú principal
    def attendance_procedure(self):
        pass