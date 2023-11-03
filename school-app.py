from flask import Flask, Blueprint, render_template
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    # This is URL configuration of the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

    # This is to suppress the warning from the console (not required, but annoying otherwise)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'
    
    # This is to create database instance
    db = SQLAlchemy(app)

    # This initializes settings for migrations
    migrate = Migrate(app, db)

    # This is a database model of student which holds id, name and age of a student
    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(20), unique=False, nullable=False)
        last_name = db.Column(db.String(20), unique=False, nullable=False)
        age = db.Column(db.Integer, nullable=False)
    
        # This is a method  that representing how records will look in the database
        def __repr__(self):
            return f"Name : {self.first_name}, Age: {self.age}"

    @app.route('/')
    def index():
        # Getting all of the students records from the database
        students = Student.query.all()
        return render_template('index.html', students=students)
    
    ## CRUD functions below
    # This is function to create new student with specified data
    def createStudent(first_name, last_name, age):
        newStudent = Student(first_name=first_name, last_name=last_name, age=age)
        db.session.add(newStudent)
        db.session.commit()
        return
    
    # This is function to read a student by specified id
    def readStudent(id):
        student = db.session.execute(db.select(Student).filter_by(id=id)).scalar_one()
        return

    # This is function to update student by his id with specified data
    def updateStudent(id, first_name, last_name, age):
        student = Student.query.get(id)
        student.first_name = first_name
        student.last_name = last_name
        student.age = age
        db.session.commit()
        return

    # This is function to delete student by his id
    def deleteStudent(id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return
    
    return app




