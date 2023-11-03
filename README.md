# Flask School Database App

Used seeder library:
[Flask Seeder](https://pypi.org/project/Flask-Seeder/)

### 0. Install necessary libraries
          
```bash

pip install Flask
pip install flask-sqlalchemy
pip install Flask-Migrate
pip install Flask-Seeder

```

### 1. Create DB instance
          
```bash

python
from app import db
db.create_all()
exit()

```

### 2. Initialize migrations

```bash

python -m flask --app school-app db init
python -m flask --app school-app db migrate -m "Initial migration"
python -m flask --app school-app db upgrade

```

### 3. New migrations, based on the changes to db models

```bash

python -m flask --app school-app db migrate -m "New migration"
python -m flask --app school-app db upgrade

```

### 4. Run app
          
```bash

python -m flask --app school-app run

```

### 5. Navigate to see seeded list of students
          
[Localhost Page](http://127.0.0.1:5000/)