# Flask School Database App

### 1. Create DB instance
          
```bash

python
from app import db
db.create_all()
exit()

```

### 2. Initialize migrations

```bash

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

```

### 3. New migrations, based on the changes to db models

```bash

flask db migrate -m "New migration"
flask db upgrade

```

### 4. Run app
          
```bash

flask --app school-app run

```