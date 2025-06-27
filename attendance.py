import random
from datetime import date, datetime, timedelta

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

    # Método para validar los datos de la asistencia (actualizado con nuevas reglas)
    def validate_attendance_data(self, attendance_id, attendance_date, classroom, students, teacher, subject):
        # Año escolar: inicia el 20/01/2025
        start_school = datetime(2025, 1, 20)
        today = datetime.today()
        # Solo días hábiles (lunes a viernes) y dentro del año escolar
        if not attendance_date:
            print("La fecha de la asistencia no puede estar vacía")
            return False
        if isinstance(attendance_date, str):
            try:
                attendance_date = datetime.strptime(attendance_date, "%Y-%m-%d")
            except Exception:
                print("Formato de fecha inválido. Use YYYY-MM-DD.")
                return False
        if attendance_date < start_school or attendance_date > today:
            print("La fecha debe estar dentro del año escolar y hasta hoy.")
            return False
        if attendance_date.weekday() >= 5:
            print("Solo se puede registrar asistencia en días hábiles (lunes a viernes).")
            return False
        if self.search_attendance(attendance_id) != -1:
            print("El código de la asistencia ya se encuentra registrado")
            return False
        if not classroom or not (1 <= int(classroom) <= 20):
            print("El aula de clase debe estar entre 1 y 20")
            return False
        if not students or not isinstance(students, list):
            print("Debe registrar al menos un estudiante")
            return False
        if len(students) > 10:
            print("No se pueden registrar más de 10 estudiantes por aula y grado")
            return False
        # Verificar que todos los estudiantes sean del mismo grado
        if len(set([s['student'].grade for s in students])) > 1:
            print("Todos los estudiantes deben pertenecer al mismo grado/curso")
            return False
        if not teacher:
            print("El docente encargado no puede estar vacío")
            return False
        if not subject:
            print("La materia no puede estar vacía")
            return False
        # Verificar que el aula esté disponible (no haya otra asistencia ese día en ese aula)
        for a in self.__attendances:
            if a.attendance_date == attendance_date and a.classroom == classroom:
                print("El aula ya está ocupada en esa fecha")
                return False
        # Verificar que ningún estudiante esté en otra aula ese día
        for a in self.__attendances:
            if a.attendance_date == attendance_date:
                for s in students:
                    if any(s['student'] == x['student'] for x in a.students):
                        print(f"El estudiante {s['student']} ya está registrado en otra aula ese día")
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

    # Métodos para listar asistencias por fecha, estudiante, grupo o aula
    def list_attendances_by(self, by, value):
        found = False
        for a in self.__attendances:
            if by == 'fecha' and str(a.attendance_date) == str(value):
                self.view_attendance(a.attendance_id)
                found = True
            elif by == 'estudiante':
                for s in a.students:
                    if str(s['student']) == str(value):
                        self.view_attendance(a.attendance_id)
                        found = True
            elif by == 'grupo' and hasattr(a.students[0]['student'], 'grade') and str(a.students[0]['student'].grade) == str(value):
                self.view_attendance(a.attendance_id)
                found = True
            elif by == 'aula' and str(a.classroom) == str(value):
                self.view_attendance(a.attendance_id)
                found = True
        if not found:
            print("No se encontraron asistencias para ese criterio.")

    # Procedimiento vacío para ser llamado desde el menú principal
    def attendance_procedure(self):
        pass

    def get_total_students(self):
        # Retorna el total de estudiantes únicos registrados en asistencias
        students = set()
        for attendance in self.__attendances:
            for s in attendance.students:
                students.add(s['student'])
        return len(students)

    def get_students_by_grade(self):
        # Retorna un diccionario con la cantidad de estudiantes por grado
        grades = {}
        for attendance in self.__attendances:
            for s in attendance.students:
                grade = s.get('grade', 'Sin grado')
                grades[grade] = grades.get(grade, 0) + 1
        return grades

    def get_attendance_by_date(self):
        # Retorna un diccionario con la cantidad de asistencias por fecha
        dates = {}
        for attendance in self.__attendances:
            date = str(attendance.attendance_date)
            count = sum(1 for s in attendance.students if s['present'])
            dates[date] = dates.get(date, 0) + count
        return dates

    def get_absence_by_date(self):
        # Retorna un diccionario con la cantidad de inasistencias por fecha
        dates = {}
        for attendance in self.__attendances:
            date = str(attendance.attendance_date)
            count = sum(1 for s in attendance.students if not s['present'])
            dates[date] = dates.get(date, 0) + count
        return dates

    def get_unjustified_absence_by_date(self):
        # Retorna un diccionario con la cantidad de inasistencias injustificadas por fecha
        dates = {}
        for attendance in self.__attendances:
            date = str(attendance.attendance_date)
            count = sum(1 for s in attendance.students if not s['present'] and not s['excused'])
            dates[date] = dates.get(date, 0) + count
        return dates

    def get_justified_absence_by_date(self):
        # Retorna un diccionario con la cantidad de inasistencias justificadas por fecha
        dates = {}
        for attendance in self.__attendances:
            date = str(attendance.attendance_date)
            count = sum(1 for s in attendance.students if not s['present'] and s['excused'])
            dates[date] = dates.get(date, 0) + count
        return dates