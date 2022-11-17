"""Data model"""

from config import db, mm

class Student(db.Model):
    __tablename__ = "STUDENT"
    name = db.Column(db.String, primary_key=True)
    major = db.Column(db.String)
    gpa = db.Column(db.Float)
    gradyear = db.Column(db.Integer)


class StudentSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        sqla_session = db.session
