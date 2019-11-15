
# Remember that a model is a representation of a database table in code.

# crear base de datos
```console
mysql -u root
create user 'admin'@'localhost' identified by 'admin';
create database grupo8;
grant all privileges on grupo8 .* to 'admin'@'localhost';
```

### crear tablas con sqlalchemy
```console
sh runshell.sh
>>> from flaskps import db
>>> db.create_all()
```

### output de ejemplo Model User y Rol 
> 2019-11-14 22:00:37,395 INFO sqlalchemy.engine.base.Engine COMMIT
> 2019-11-14 22:00:37,398 INFO sqlalchemy.engine.base.Engine
> CREATE TABLE users (
> 	created_at DATE,
> 	updated_at DATE,
> 	id INTEGER NOT NULL AUTO_INCREMENT,
> 	is_admin BOOL,
> 	username VARCHAR(60) NOT NULL,
> 	email VARCHAR(60) NOT NULL,
> 	name VARCHAR(60),
> 	surname VARCHAR(60),
> 	active BOOL,
> 	password_hash VARCHAR(128),
> 	PRIMARY KEY (id),
> 	CHECK (is_admin IN (0, 1)),
> 	UNIQUE (username),
> 	UNIQUE (email),
> 	CHECK (active IN (0, 1))
> )
> 
> 
> 2019-11-14 22:00:37,398 INFO sqlalchemy.engine.base.Engine {}
> 2019-11-14 22:00:37,432 INFO sqlalchemy.engine.base.Engine COMMIT
> 2019-11-14 22:00:37,433 INFO sqlalchemy.engine.base.Engine
> CREATE TABLE rol (
> 	id INTEGER NOT NULL AUTO_INCREMENT,
> 	name VARCHAR(60) NOT NULL,
> 	PRIMARY KEY (id),
> 	UNIQUE (name)
> )



### crear migraciones
```console
flask db migrate
```

### aplicar migracion
antes de aplicar las migraciones, asegurese de tener seteado la aplicacion. Para saber en que proyecto se aplican las migraciones
```console
export FLASK_APP=run.py
flask db upgrade
```


## Correr servidor local localhost:5000
```console
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run
```


### Estructura (Blueprints)

Home - tendra las declaradas las vistas de home y dashboard
Admin - tendra todo lo relacionado con la administracion (dependiendo del roll) forms and views
Auth - tendra todo lo relacionado con la autenticacion (login, exepciones) forms and views

└── dream-team
    ├── flaskps
    │   ├── __init__.py
    │   ├── admin
    │   │   ├── __init__.py
    │   │   ├── forms.py
    │   │   └── views.py
    │   ├── auth
    │   │   ├── __init__.py
    │   │   ├── forms.py
    │   │   └── views.py
    │   ├── home
    │   │   ├── __init__.py
    │   │   └── views.py
    │   ├── models.py
    │   ├── static
    │   └── templates
    ├── config.py
    ├── instance
    │   └── config.py
    ├── migrations
    │   ├── README
    │   ├── alembic.ini
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       └── a1a1d8b30202_.py
    ├── requirements.txt
    └── run.py


### instanciar base de datos y crear ADMIN inicial
```console
from flaskps import db
db.create_all()
from flaskps.users.models import User
# crea usuario
user = User(
    username='superadmin',
    email='admin@admin.com',
)
user.password = 'admin'

# lo guarda en la db
db.session.add(user)
db.session.commit()


User.query.all() # te trae todos los usuarios
```
