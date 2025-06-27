import datetime
from grade import Grade
from student import Student
from attendance import Attendance

class Report:
    def __init__(self, report_student_count=0, report_students_by_grade=None, report_attendance_by_date=None, report_absence_by_date=None, report_unjustified_absence_by_date=None, report_justified_absence_by_date=None, title="", content=""):
        self.report_student_count = report_student_count
        self.report_students_by_grade = report_students_by_grade if report_students_by_grade is not None else {}
        self.report_attendance_by_date = report_attendance_by_date if report_attendance_by_date is not None else {}
        self.report_absence_by_date = report_absence_by_date if report_absence_by_date is not None else {}
        self.report_unjustified_absence_by_date = report_unjustified_absence_by_date if report_unjustified_absence_by_date is not None else {}
        self.report_justified_absence_by_date = report_justified_absence_by_date if report_justified_absence_by_date is not None else {}

