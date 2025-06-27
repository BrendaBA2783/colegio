from datetime import datetime, date

class AsistenciaFacil:
    def __init__(self):
        # Simulamos estudiantes y aulas ya registrados
        self.registered_students = [
            {'name': 'Ana', 'grade': '5A'},
            {'name': 'Luis', 'grade': '5A'},
            {'name': 'Sofia', 'grade': '6B'}
        ]
        self.registered_classrooms = [str(i) for i in range(1, 21)]
        self.attendances = []

    def find_student(self, name):
        for student in self.registered_students:
            if student['name'].lower() == name.lower():
                return student
        return None

    def register_attendance(self):
        try:
            n = int(input("¿Cuántos estudiantes vas a registrar? (1-10): "))
            if n < 1 or n > 10:
                print("Solo puedes registrar entre 1 y 10 estudiantes.")
                return
        except ValueError:
            print("Debes ingresar un número válido.")
            return
        students = []
        grades = set()
        not_found = []
        for i in range(n):
            name = input(f"Nombre del estudiante #{i+1}: ")
            student = self.find_student(name)
            if not student:
                not_found.append(name)
            else:
                students.append(student)
                grades.add(student['grade'])
        if not_found:
            print(f"No se encontraron los siguientes estudiantes: {', '.join(not_found)}")
            return
        if len(grades) > 1:
            print("Todos los estudiantes deben ser del mismo grado.")
            return
        date_str = input("Fecha de la asistencia (YYYY-MM-DD, vacío para hoy): ")
        if not date_str:
            attendance_date = date.today()
        else:
            try:
                attendance_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            except Exception:
                print("Formato de fecha inválido.")
                return
        inicio = datetime(2025, 1, 20).date()
        hoy = date.today()
        if not (inicio <= attendance_date <= hoy):
            print("La fecha debe estar dentro del año escolar (desde 20/01/2025 hasta hoy).")
            return
        if attendance_date.weekday() >= 5:
            print("Solo se puede registrar asistencia en días hábiles (lunes a viernes).")
            return
        classroom = input("Número de aula (1-20): ")
        if classroom not in self.registered_classrooms:
            print(f"El aula '{classroom}' no ha sido registrada.")
            return
        for a in self.attendances:
            if a['date'] == attendance_date and a['classroom'] == classroom:
                print("El aula ya está ocupada ese día.")
                return
        for a in self.attendances:
            if a['date'] == attendance_date:
                for student in students:
                    if student['name'] in [e['name'] for e in a['students']]:
                        print(f"El estudiante {student['name']} ya está registrado en otra aula ese día.")
                        return
        self.attendances.append({
            'date': attendance_date,
            'classroom': classroom,
            'grade': list(grades)[0],
            'students': students
        })
        print("Asistencia registrada correctamente.")

    def list_attendances(self, by, value):
        found = []
        for a in self.attendances:
            if by == 'date' and str(a['date']) == str(value):
                found.append(a)
            elif by == 'classroom' and a['classroom'] == str(value):
                found.append(a)
            elif by == 'grade' and a['grade'] == str(value):
                found.append(a)
            elif by == 'student':
                for e in a['students']:
                    if e['name'] == value:
                        found.append(a)
        if not found:
            print("No se encontraron asistencias para ese criterio.")
        else:
            for a in found:
                print(f"Fecha: {a['date']} | Aula: {a['classroom']} | Grado: {a['grade']} | Estudiantes: {[e['name'] for e in a['students']]}")
