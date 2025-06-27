#Espacio para realizar la importacion de las librerias o archivos (clases) necesari@s
from os import system
from datetime import datetime
from student import Student
from grade import Grade
from teacher import Teacher
from classroom import Classroom
from subject import Subject
from attendance import Attendance
from report import Report

#Colores a usar
#\033[96m -> Azul 
#\033[92m -> Verde 
#\033[93m -> Amarillo 
#\033[91m -> Rojo
#\033[0m -> Color original

#Creamos la clase principal menu 
class Menu: 

    #Inicializamos el contructor de la clase Menu
    def __init__ (self):
        self.student = Student()
        self.grade = Grade()
        self.teacher = Teacher()
        self.classroom = Classroom()
        self.subject = Subject()
        self.attendance = Attendance()

    #EMPEZAMOS A REALIZAR LOS METODOS PARA LOS GRADOS
    #Registrar grado
    def register_grade(self):
        system("cls")
        print("\033[96mREGISTRO DE GRADO\n")

        try:
            grade_name = input("\033[0mIngrese el nombre del grado: ")
            grade_students_quantity = int(input("Ingrese la cantidad de estudiantes del grado: "))
        
        except ValueError:
            print("\033[91m\nError: Debe ingresar un dato válido")
            input("\033[93m\nPresione enter para continuar...")
            return

        grade_id = self.grade.generate_grade_id()

        if self.grade.validate_grade_data(grade_id, grade_name, grade_students_quantity):
            grade = Grade(grade_id, grade_name, grade_students_quantity)
            if self.grade.register_grade(grade, grade_id) == True:
                print(F"El id del grado es: {grade_id}")
                print("\033[92m\nGrado registrado exitosamente!")
                input("\033[93m\nPresione enter para continuar...")
            else:
                print("\033[91m\nError al registrar el grado. Intente nuevamente.")
                input("\033[93m\nPresione enter para continuar...")
        else:
            print("\033[91m\nError: Datos del grado no válidos")
            input("\033[93m\nPresione enter para continuar...")

    #MModificar grado
    def modify_grade(self):
        system("cls")
        print("\033[96mMODIFICAR GRADO\n")
        
        grade_id = int(input("\033[0mIngrese el ID del grado a modificar: "))

        if self.grade.modify_grade(grade_id) == True:
            print("\033[92m\nGrado modificado exitosamente!")
            input("\033[93m\nPresione enter para continuar...")
        else:
            print("\033[91m\nError al modificar el grado. Intente nuevamente.")
            input("\033[93m\nPresione enter para continuar...")

    #Listar grados
    def list_grades(self):
        system("cls")
        print("\033[96mLISTA DE GRADOS\n")
        self.grade.list_grades()
        input("\033[93m\nPresione enter para continuar...")

    #Habilitar grado
    def enable_grade(self):
        system("cls")
        print("\033[96mHABILITAR GRADO\n")
        try:
            grade_id = int(input("\033[0mIngrese el ID del grado a habilitar: "))
        except ValueError:
            print("\033[91m\nError: Debe ingresar un número válido")
            input("\033[93m\nPresione Enter para continuar...")
            return
        self.grade.enable_grade(grade_id)
        input("\033[93m\nPresione Enter para continuar...")

    #Deshabilitar grado
    def disable_grade(self):
        system("cls")
        print("\033[96mDESHABILITAR GRADO\n")
        try:
            grade_id = int(input("\033[0mIngrese el ID del grado a deshabilitar: "))
        except ValueError:
            print("\033[91m\nError: Debe ingresar un número válido")
            input("\033[93m\nPresione Enter para continuar...")
            return
        self.grade.disable_grade(grade_id)
        input("\033[93m\nPresione Enter para continuar...")

    #Visualizar grado
    def view_grade(self):
        system("cls")
        print("\033[96mVISUALIZAR GRADO\n")
        try:
            grade_id = int(input("\033[0mIngrese el ID del grado a visualizar: "))
        except ValueError:
            print("\033[91m\nError: Debe ingresar un número válido")
            input("\033[93m\nPresione Enter para continuar...")
            return
        self.grade.view_grade(grade_id)
        input("\033[93m\nPresione Enter para continuar...")

    #EMPEZAMOS A REALIZAR LOS METODOS PARA LOS ESTUDIANTES
    #Registrar estudiantes
    def register_student(self):
        system("cls")
        print("Registro de estudiante\n")

        try:
            student_name = input("Ingrese el nombre del estudiante: ")
            student_last_name = input("Ingrese el apellido del estudiante: ")
            student_grade = input("Ingrese el grado del estudiante: ")
        
        except ValueError:
            print("Error: Debe ingresar un dato válido")
            input("\nPresione Enter para continuar...")

        
        student_id = self.student.generate_student_id()

        if self.student.validate_student_data(student_id, student_grade, student_name, student_last_name):
            student = Student(student_id, student_name, student_last_name, student_grade)
            if self.student.register_student(student, student_id) == True:
                print(F"El id del estudiante es: {student_id}")
                print("\nEstudiante registrado exitosamente!")
                input("\nPresione Enter para continuar...")
            else:
                print("Error al registrar el estudiante. Intente nuevamente.")
                input("\nPresione Enter para continuar...")
        else:
            print("Error: Datos del estudiante no válidos")
            input("\nPresione Enter para continuar...")
    
    #Registrar docentes
    def register_teacher(self):
        system("cls")
        print("Registro de docente\n")
        try:
            teacher_name = input("Ingrese el nombre del docente: ")
            teacher_last_name = input("Ingrese el apellido del docente: ")
            subject = input("Ingrese la materia que imparte: ")
            classroom = input("Ingrese el aula asignada: ")
        except ValueError:
            print("Error: Debe ingresar un dato válido")
            input("\nPresione Enter para continuar...")
            return
        teacher_id = self.teacher.generate_teacher_id()
        if self.teacher.validate_teacher_data(teacher_id, teacher_name, teacher_last_name, subject, classroom):
            teacher = Teacher(teacher_id, teacher_name, teacher_last_name, subject, classroom)
            if self.teacher.register_teacher(teacher) == True:
                print(f"El código del docente es: {teacher_id}")
                print("\nDocente registrado exitosamente!")
                input("\nPresione Enter para continuar...")
            else:
                print("Error al registrar el docente. Intente nuevamente.")
                input("\nPresione Enter para continuar...")
        else:
            print("Error: Datos del docente no válidos")
            input("\nPresione Enter para continuar...")

    # Métodos para modificar, habilitar, deshabilitar, listar y visualizar docentes
    def modify_teacher(self):
        system("cls")
        print("Modificar docente\n")
        try:
            teacher_id = int(input("Ingrese el ID del docente a modificar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        new_name = input("Nuevo nombre (dejar vacío para no cambiar): ")
        new_last_name = input("Nuevo apellido (dejar vacío para no cambiar): ")
        new_subject = input("Nueva materia (dejar vacío para no cambiar): ")
        new_classroom = input("Nuevo aula (dejar vacío para no cambiar): ")
        if new_name == "": new_name = None
        if new_last_name == "": new_last_name = None
        if new_subject == "": new_subject = None
        if new_classroom == "": new_classroom = None
        self.teacher.modify_teacher(teacher_id, new_name, new_last_name, new_subject, new_classroom)
        input("Presione Enter para continuar...")

    def enable_teacher(self):
        system("cls")
        print("Habilitar docente\n")
        try:
            teacher_id = int(input("Ingrese el ID del docente a habilitar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.teacher.enable_teacher(teacher_id)
        input("Presione Enter para continuar...")

    def disable_teacher(self):
        system("cls")
        print("Deshabilitar docente\n")
        try:
            teacher_id = int(input("Ingrese el ID del docente a deshabilitar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.teacher.disable_teacher(teacher_id)
        input("Presione Enter para continuar...")

    def list_teachers(self):
        system("cls")
        print("Lista de docentes\n")
        self.teacher.list_teachers()
        input("Presione Enter para continuar...")

    def view_teacher(self):
        system("cls")
        print("Visualizar docente\n")
        try:
            teacher_id = int(input("Ingrese el ID del docente a visualizar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.teacher.view_teacher(teacher_id)
        input("Presione Enter para continuar...")

    # Métodos para registrar, modificar, habilitar, deshabilitar, listar y visualizar aulas
    def register_classroom(self):
        system("cls")
        print("Registro de aula\n")
        classroom_name = input("Ingrese el nombre del aula: ")
        try:
            capacity = int(input("Ingrese la capacidad del aula: "))
        except ValueError:
            print("La capacidad debe ser un número entero positivo")
            input("Presione Enter para continuar...")
            return
        classroom_id = self.classroom.generate_classroom_id()
        if self.classroom.validate_classroom_data(classroom_id, classroom_name, capacity):
            classroom = Classroom(classroom_id, classroom_name, capacity)
            if self.classroom.register_classroom(classroom):
                print(f"Aula registrada con ID: {classroom_id}")
                print("\nAula registrada exitosamente!")
                input("Presione Enter para continuar...")
            else:
                print("Error al registrar el aula. Intente nuevamente.")
                input("Presione Enter para continuar...")
        else:
            print("Error: Datos del aula no válidos")
            input("Presione Enter para continuar...")

    def modify_classroom(self):
        system("cls")
        print("Modificar aula\n")
        try:
            classroom_id = int(input("Ingrese el ID del aula a modificar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        new_name = input("Nuevo nombre (dejar vacío para no cambiar): ")
        new_capacity = input("Nueva capacidad (dejar vacío para no cambiar): ")
        if new_name == "": new_name = None
        if new_capacity == "":
            new_capacity = None
        else:
            try:
                new_capacity = int(new_capacity)
            except ValueError:
                print("La capacidad debe ser un número entero positivo")
                input("Presione Enter para continuar...")
                return
        self.classroom.modify_classroom(classroom_id, new_name, new_capacity)
        input("Presione Enter para continuar...")

    def enable_classroom(self):
        system("cls")
        print("Habilitar aula\n")
        try:
            classroom_id = int(input("Ingrese el ID del aula a habilitar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.classroom.enable_classroom(classroom_id)
        input("Presione Enter para continuar...")

    def disable_classroom(self):
        system("cls")
        print("Deshabilitar aula\n")
        try:
            classroom_id = int(input("Ingrese el ID del aula a deshabilitar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.classroom.disable_classroom(classroom_id)
        input("Presione Enter para continuar...")

    def list_classrooms(self):
        system("cls")
        print("Lista de aulas\n")
        self.classroom.list_classrooms()
        input("Presione Enter para continuar...")

    def view_classroom(self):
        system("cls")
        print("Visualizar aula\n")
        try:
            classroom_id = int(input("Ingrese el ID del aula a visualizar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.classroom.view_classroom(classroom_id)
        input("Presione Enter para continuar...")

    # Métodos para registrar, modificar, habilitar, deshabilitar, listar y visualizar materias
    def register_subject(self):
        system("cls")
        print("Registro de materia\n")
        subject_name = input("Ingrese el nombre de la materia: ")
        subject_id = self.subject.generate_subject_id()
        if self.subject.validate_subject_data(subject_id, subject_name):
            subject = Subject(subject_id, subject_name)
            if self.subject.register_subject(subject):
                print(f"Materia registrada con ID: {subject_id}")
                print("\nMateria registrada exitosamente!")
                input("Presione Enter para continuar...")
            else:
                print("Error al registrar la materia. Intente nuevamente.")
                input("Presione Enter para continuar...")
        else:
            print("Error: Datos de la materia no válidos")
            input("Presione Enter para continuar...")

    def modify_subject(self):
        system("cls")
        print("Modificar materia\n")
        try:
            subject_id = int(input("Ingrese el ID de la materia a modificar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        new_name = input("Nuevo nombre (dejar vacío para no cambiar): ")
        if new_name == "": new_name = None
        self.subject.modify_subject(subject_id, new_name)
        input("Presione Enter para continuar...")

    def enable_subject(self):
        system("cls")
        print("Habilitar materia\n")
        try:
            subject_id = int(input("Ingrese el ID de la materia a habilitar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.subject.enable_subject(subject_id)
        input("Presione Enter para continuar...")

    def disable_subject(self):
        system("cls")
        print("Deshabilitar materia\n")
        try:
            subject_id = int(input("Ingrese el ID de la materia a deshabilitar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.subject.disable_subject(subject_id)
        input("Presione Enter para continuar...")

    def list_subjects(self):
        system("cls")
        print("Lista de materias\n")
        self.subject.list_subjects()
        input("Presione Enter para continuar...")

    def view_subject(self):
        system("cls")
        print("Visualizar materia\n")
        try:
            subject_id = int(input("Ingrese el ID de la materia a visualizar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.subject.view_subject(subject_id)
        input("Presione Enter para continuar...")

    # Métodos para registrar, modificar, habilitar, deshabilitar, listar y visualizar asistencias
    def register_attendance(self):
        # Usamos el método de la nueva clase
        self.attendance.register_attendance()
        input("Presione Enter para continuar...")

    def list_attendances(self):
        print("Listar asistencias por:")
        print("1. Fecha")
        print("2. Aula")
        print("3. Grado")
        print("4. Estudiante")
        opcion = input("Elija una opción: ")
        if opcion == '1':
            valor = input("Ingrese la fecha (YYYY-MM-DD): ")
            self.attendance.attendance_list('fecha', valor)
        elif opcion == '2':
            valor = input("Ingrese el número de aula: ")
            self.attendance.attendance_list('aula', valor)
        elif opcion == '3':
            valor = input("Ingrese el grado: ")
            self.attendance.attendance_list('grado', valor)
        elif opcion == '4':
            valor = input("Ingrese el nombre del estudiante: ")
            self.attendance.attendance_list('estudiante', valor)
        else:
            print("Opción no válida.")
        input("Presione Enter para continuar...")

    def modify_attendance(self):
        system("cls")
        print("Modificar asistencia\n")
        print("Funcionalidad no implementada aún.")
        input("Presione Enter para continuar...")

    def enable_attendance(self):
        system("cls")
        print("Habilitar asistencia\n")
        print("Funcionalidad no implementada aún.")
        input("Presione Enter para continuar...")

    def disable_attendance(self):
        system("cls")
        print("Deshabilitar asistencia\n")
        print("Funcionalidad no implementada aún.")
        input("Presione Enter para continuar...")

    def view_attendance(self):
        system("cls")
        print("Visualizar asistencia\n")
        try:
            attendance_id = int(input("Ingrese el ID de la asistencia a visualizar: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            input("Presione Enter para continuar...")
            return
        self.attendance.view_attendance(attendance_id)
        input("Presione Enter para continuar...")

    #report methods
    def report_student_count(self):
        system("cls")
        print("Reporte de cantidad de estudiantes\n")
        total = self.attendance.get_total_students()
        print(f"Total de estudiantes registrados: {total}")
        input("Presione Enter para continuar...")

    def report_students_by_grade(self):
        system("cls")
        print("Reporte de cantidad de estudiantes por grado\n")
        data = self.attendance.get_students_by_grade()
        for grade, count in data.items():
            print(f"Grado {grade}: {count} estudiantes")
        input("Presione Enter para continuar...")

    def report_attendance_by_date(self):
        system("cls")
        print("Reporte de estudiantes con asistencia por fecha\n")
        data = self.attendance.get_attendance_by_date()
        for date, count in data.items():
            print(f"Fecha {date}: {count} asistencias")
        input("Presione Enter para continuar...")

    def report_absence_by_date(self):
        system("cls")
        print("Reporte de estudiantes con inasistencia por fecha\n")
        data = self.attendance.get_absence_by_date()
        for date, count in data.items():
            print(f"Fecha {date}: {count} inasistencias")
        input("Presione Enter para continuar...")

    def report_unjustified_absence_by_date(self):
        system("cls")
        print("Reporte de inasistencias injustificadas por fecha\n")
        data = self.attendance.get_unjustified_absence_by_date()
        for date, count in data.items():
            print(f"Fecha {date}: {count} inasistencias injustificadas")
        input("Presione Enter para continuar...")

    def report_justified_absence_by_date(self):
        system("cls")
        print("Reporte de inasistencias justificadas por fecha\n")
        data = self.attendance.get_justified_absence_by_date()
        for date, count in data.items():
            print(f"Fecha {date}: {count} inasistencias justificadas")
        input("Presione Enter para continuar...")

    def report_option(self):
        report = f"Total Students: {self.report_student_count}\n"
        report += "Students by Grade:\n"
        for grade, count in self.report_students_by_grade.items():
            report += f"  Grade {grade}: {count}\n"
        report += "Attendance by Date:\n"
        for date, count in self.report_attendance_by_date.items():
            report += f"  {date}: {count}\n"
        report += "Absence by Date:\n"
        for date, count in self.report_absence_by_date.items():
            report += f"  {date}: {count}\n"
        report += "Unjustified Absence by Date:\n"
        for date, count in self.report_unjustified_absence_by_date.items():
            report += f"  {date}: {count}\n"
        report += "Justified Absence by Date:\n"
        for date, count in self.report_justified_absence_by_date.items():
            report += f"  {date}: {count}\n"
            report = Report(report_student_count=self.attendance.get_total_students(),
                            report_students_by_grade=self.attendance.get_students_by_grade(),
                            report_attendance_by_date=self.attendance.get_attendance_by_date(),
                            report_absence_by_date=self.attendance.get_absence_by_date(),
                            report_unjustified_absence_by_date=self.attendance.get_unjustified_absence_by_date(),
                            report_justified_absence_by_date=self.attendance.get_justified_absence_by_date())
        return report

    def show_main_menu(self):
        while True:
            system("cls")
            print("\033[0m=================================")
            print("           Colegio BSJ           ")
            print("=================================\n")
            print("Menú principal: \n")
            print("1. Opciones para estudiantes")
            print("2. Opciones para docentes")
            print("3. Opciones para materias")
            print("4. Opciones para grados")
            print("5. Opciones para aulas")
            print("6. Opciones para asistencias")
            print("7. Opciones para reportes")
            print("8. SALIR\n")

            try:
                option = int(input("Ingrese el códio de la opción a realizar: "))

                if option == 1:
                    system("cls")
                    print("=================================")
                    print("           Colegio BSJ           ")
                    print("=================================\n")
                    print("Menú de opciones de estudiantes: \n")
                    print("1. Registrar estudiante")
                    print("2. Modificar estudiante")
                    print("3. Habilitar estudiante")
                    print("4. Deshabilitar estudiante")
                    print("5. Listar estudiantes")
                    print("6. Visualizar estudiante")     
                    print("7. SALIR\n")

                    try:

                        student_option = int(input("Ingrese el código de la opción deseada: "))

                        if student_option == 1:
                            self.register_student()

                        elif student_option == 2:
                            self.modify_student()

                        elif student_option == 3:
                            self.enable_student()

                        elif student_option == 4:
                            self.disable_student()

                        elif student_option == 5:
                            self.list_students()

                        elif student_option == 6:
                            self.view_student()

                        elif student_option == 7:
                            print("Saliendo del menú de estudiantes...")
                            input("Presione Enter para continuar...")

                        else:
                            print("La opción ingresada no es válida")
                            input("Presione Enter para continuar...")
                        
                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
                        input("Presione Enter para continuar...")

                elif option == 2:
                    system("cls")
                    print("=================================")
                    print("           Colegio BSJ           ")
                    print("=================================\n")
                    print("Menú de opciones de docentes: \n")
                    print("1. Registrar docente")
                    print("2. Modificar docente")
                    print("3. Habilitar docente")
                    print("4. Deshabilitar docente")
                    print("5. Listar docentes")
                    print("6. Visualizar docente")     
                    print("7. SALIR\n")

                    try:
                        teacher_option = int(input("Ingrese el código de la opción deseada: "))

                        if teacher_option == 1:
                            self.register_teacher()
                        elif teacher_option == 2:
                            self.modify_teacher()
                        elif teacher_option == 3:
                            self.enable_teacher()
                        elif teacher_option == 4:
                            self.disable_teacher()
                        elif teacher_option == 5:
                            self.list_teachers()
                        elif teacher_option == 6:
                            self.view_teacher()
                        elif teacher_option == 7:
                            print("Saliendo del menú de docentes...")
                            input("Presione Enter para continuar...")
                        else:
                            print("La opción ingresada no es válida")
                            input("Presione Enter para continuar...")
                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
                        input("Presione Enter para continuar...")

                elif option == 3:
                    system("cls")
                    print("=================================")
                    print("           Colegio BSJ           ")
                    print("=================================\n")
                    print("Menú de opciones de materias: \n")
                    print("1. Registrar materia")
                    print("2. Modificar materia")
                    print("3. Habilitar materia")
                    print("4. Deshabilitar materia")
                    print("5. Listar materias")
                    print("6. Visualizar materia")     
                    print("7. SALIR\n")

                    try:
                        subject_option = int(input("Ingrese el código de la opción deseada: "))

                        if subject_option == 1:
                            self.register_subject()

                        elif subject_option == 2:
                            self.modify_subject()

                        elif subject_option == 3:
                            self.enable_subject()

                        elif subject_option == 4:
                            self.disable_subject()

                        elif subject_option == 5:
                            self.list_subjects()

                        elif subject_option == 6:
                            self.view_subject()

                        elif subject_option == 7:
                            print("Saliendo del menú de materias...")
                            input("Presione Enter para continuar...")

                        else:
                            print("La opción ingresada no es válida")
                            input("Presione Enter para continuar...")

                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
                        input("Presione Enter para continuar...")

                elif option == 4:
                    system("cls")
                    print("=================================")
                    print("           Colegio BSJ           ")
                    print("=================================\n")
                    print("Menú de opciones de grados: \n")
                    print("1. Registrar grado")
                    print("2. Modificar grado")
                    print("3. Habilitar grado")
                    print("4. Deshabilitar grado")
                    print("5. Listar grados")
                    print("6. Visualizar grado")     
                    print("7. SALIR\n")

                    try:
                        grade_option = int(input("Ingrese el código de la opción deseada: "))

                        if grade_option == 1:
                            self.register_grade()

                        elif grade_option == 2:
                            self.modify_grade()

                        elif grade_option == 3:
                            self.enable_grade()

                        elif grade_option == 4:
                            self.disable_grade()

                        elif grade_option == 5:
                            self.list_grades()

                        elif grade_option == 6:
                            self.view_grade()

                        elif grade_option == 7:
                            print("Saliendo del menú de grados...")
                            input("Presione Enter para continuar...")
                        
                        else:
                            print("La opción ingresada no es válida")
                            input("Presione Enter para continuar...")

                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
                        input("Presione Enter para continuar...")

                elif option == 5:
                    system("cls")
                    print("=================================")
                    print("           Colegio BSJ           ")
                    print("=================================\n")
                    print("Menú de opciones de aulas: \n")
                    print("1. Registrar aula")
                    print("2. Modificar aula")
                    print("3. Habilitar aula")
                    print("4. Deshabilitar aula")
                    print("5. Listar aulas")
                    print("6. Visualizar aula")     
                    print("7. SALIR\n")

                    try:
                        classroom_option = int(input("Ingrese el código de la opción deseada: "))

                        if classroom_option == 1:
                            self.register_classroom()

                        elif classroom_option == 2:
                            self.modify_classroom()

                        elif classroom_option == 3:
                            self.enable_classroom()

                        elif classroom_option == 4:
                            self.disable_classroom()

                        elif classroom_option == 5:
                            self.list_classrooms()

                        elif classroom_option == 6:
                            self.view_classroom()

                        elif classroom_option == 7:
                            print("Saliendo del menú de aulas...")
                            input("Presione Enter para continuar...")

                        else:
                            print("La opción ingresada no es válida")
                            input("Presione Enter para continuar...")

                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
                        input("Presione Enter para continuar...")
                    
                elif option == 6:
                    system("cls")
                    print("=================================")
                    print("           Colegio BSJ           ")
                    print("=================================\n")
                    print("Menú de opciones de asistencias: \n")
                    print("1. Registrar asistencia")
                    print("2. Modificar asistencia")
                    print("3. Habilitar asistencia")
                    print("4. Deshabilitar asistencia")
                    print("5. Listar asistencias")
                    print("6. Visualizar asistencia")     
                    print("7. SALIR\n")

                    try:
                        attendance_option = int(input("Ingrese el código de la opción deseada: "))

                        if attendance_option == 1:
                            self.register_attendance()

                        elif attendance_option == 2:
                            self.modify_attendance()

                        elif attendance_option == 3:
                            self.enable_attendance()

                        elif attendance_option == 4:
                            self.disable_attendance()

                        elif attendance_option == 5:
                            self.list_attendances()

                        elif attendance_option == 6:
                            self.view_attendance()

                        elif attendance_option == 7:
                            print("Saliendo del menú de asistencias...")
                            input("Presione Enter para continuar...")

                        else:
                            print("La opción ingresada no es válida")
                            input("Presione Enter para continuar...")

                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
                        input("Presione Enter para continuar...")

                elif option == 7:
                    system("cls")
                    print("=================================")
                    print("           Colegio BSJ           ")
                    print("=================================\n")
                    print("Menú de opciones de reportes: \n")
                    print("1. Reporte de cantidad de estudiantes")
                    print("2. Reporte de cantidad de estudiantes por grado")
                    print("3. Reporte de cantidad de estudiantes que tienen asistencia por fecha")
                    print("4. Reporte de cantiad de estudiantes que tienen inasistencia por fecha")
                    print("5. Reporte de cantidad de estudiantes que tienen inasistencia injustificada por fecha")
                    print("6. Reporte de cantidad de estudiantes que tienen inasistencia justificada por fecha")  
                    print("7. SALIR\n")

                    try:
                        report_option = int(input("Ingrese el código de la opción deseada: "))
                        if report_option == 1:
                            self.report_student_count()

                        elif report_option == 2:
                            self.report_students_by_grade()

                        elif report_option == 3:
                            self.report_attendance_by_date()

                        elif report_option == 4:
                            self.report_absence_by_date()

                        elif report_option == 5:
                            self.report_unjustified_absence_by_date()

                        elif report_option == 6:
                            self.report_justified_absence_by_date()

                        elif report_option == 7:
                            print("Saliendo del menú de reportes...")
                            input("Presione Enter para continuar...")

                        else:
                            print("La opción ingresada no es válida")
                            input("Presione Enter para continuar...")

                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
                        input("Presione Enter para continuar...")

                elif option == 8:
                    system("cls")
                    print("=================================")
                    print("           Colegio BSJ           ")
                    print("=================================\n")
                    print("Saliendo del sistema...")
                    input("Presione Enter para continuar...")
                    break

                else:
                    print("La opción ingresada no es válida")
                    input("Presione Enter para continuar...")

            except ValueError:
                print("Error: Debe ingresar un número entero.")
                input("Presione Enter para continuar...")   

if __name__ == '__main__':
    menu = Menu()
    menu.show_main_menu()