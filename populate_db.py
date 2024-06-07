from app import app
from models import db, TeacherLoad

with app.app_context():
    db.create_all()

    if not TeacherLoad.query.first():
        sample_data = [
            TeacherLoad(teacher_name="Ivan Ivanov", subject="Math", hours_worked=120.5, report_period="2023-01"),
            TeacherLoad(teacher_name="Anna Petrova", subject="Physics", hours_worked=98.0, report_period="2023-01"),
            TeacherLoad(teacher_name="Sergey Sergeev", subject="Chemistry", hours_worked=110.75,
                        report_period="2023-01"),
            TeacherLoad(teacher_name="Olga Smirnova", subject="Biology", hours_worked=115.0, report_period="2023-01"),
            TeacherLoad(teacher_name="Dmitry Sidorov", subject="History", hours_worked=105.25, report_period="2023-01"),
            TeacherLoad(teacher_name="Elena Ivanova", subject="English", hours_worked=102.5, report_period="2023-01"),
            TeacherLoad(teacher_name="Nikolay Petrov", subject="Geography", hours_worked=97.0, report_period="2023-01"),
            TeacherLoad(teacher_name="Maria Kuznetsova", subject="Literature", hours_worked=112.75,
                        report_period="2023-01"),
            TeacherLoad(teacher_name="Alexey Popov", subject="Computer Science", hours_worked=108.5,
                        report_period="2023-01"),
            TeacherLoad(teacher_name="Ekaterina Smirnova", subject="Art", hours_worked=100.0, report_period="2023-01"),
            TeacherLoad(teacher_name="Maxim Ivanov", subject="Physical Education", hours_worked=95.25,
                        report_period="2023-01"),
            TeacherLoad(teacher_name="Tatiana Sokolova", subject="Music", hours_worked=99.0, report_period="2023-01"),
            TeacherLoad(teacher_name="Andrey Voronov", subject="Economics", hours_worked=103.75,
                        report_period="2023-01"),
            TeacherLoad(teacher_name="Viktoriya Pavlova", subject="Chemistry", hours_worked=107.0,
                        report_period="2023-01"),
            TeacherLoad(teacher_name="Sergey Ivanov", subject="Math", hours_worked=125.5, report_period="2023-01")
        ]
        db.session.bulk_save_objects(sample_data)
        db.session.commit()
