from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TeacherLoad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    hours_worked = db.Column(db.Float, nullable=False)
    report_period = db.Column(db.String(50), nullable=False)

