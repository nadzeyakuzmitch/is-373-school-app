from flask import Flask, Blueprint, render_template, request, redirect
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder, Seeder, Faker, generator

# Factory with models creation and seeder set up
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

    # This initializes seeder for our app
    seeder = FlaskSeeder()

    # This is a database model of student which holds id, name and age of a student; if changed need to create and run migration
    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(20), unique=False)
        last_name = db.Column(db.String(20), unique=False)
        age = db.Column(db.Integer)
    
        # This is a method  that representing how records will look in the database
        def __repr__(self):
            return f"Name : {self.first_name}, Age: {self.age}"

    @app.route('/')
    def index():
        # Reading all of the students records from the database
        students = Student.query.all()
        return render_template('index.html', students=students)
    

    # These functions are to seed students and it's API wrapper
    @app.route('/seed', methods=["POST"])
    def seedRequest():
        count = request.form.get("count")
        seedStudents(int(count))
        return redirect('/')
    
    def seedStudents(count):
        # Deleting old students first
        db.session.query(Student).delete()

        # Model to seed based on
        faker = Faker(
            cls=Student,
            init={
                "id": generator.Sequence(),
                "first_name": generator.Name(),
                "last_name": generator.Name(),
                "age": generator.Integer(start=18, end=100)
            }
        )
        
        # This is the code to create students amount based on specified count
        for student in faker.create(count):
            db.session.add(student)
        db.session.commit()

    # API wrapper for create database function
    @app.route('/create', methods=["POST"])
    def createRequest():
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        age = request.form.get("age")
    
        if first_name != '' and last_name != '' and age is not None:
            createStudent(first_name, last_name, age)
            return redirect('/')
        else:
            return redirect('/')

    # API wrapper for update and delete database functions
    @app.route('/update', methods=["POST"])
    def updateRequest():
        action = request.form.get("submit")
        id = request.form.get("id")

        if action == "update":
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            age = request.form.get("age")
            if first_name != '' and last_name != '' and age is not None:
                updateStudent(id, first_name, last_name, age)
        else:
            deleteStudent(id)
        
        return redirect('/')
    
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




