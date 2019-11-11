# Remember that a model is a representation of a database table in code.

# crear base de datos
```console
mysql -u root
create user 'admin'@'localhost' identified by 'admin';
create database grupo8;
grant all privileges on grupo8 .* to 'admin'@'localhost';
```


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


# relaciones
https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
ejemplo de modelo a sql
CREATE TABLE invoices (
   id INTEGER NOT NULL,
   custid INTEGER,
   invno INTEGER,
   amount INTEGER,
   PRIMARY KEY (id),
   FOREIGN KEY(custid) REFERENCES customers (id)
)
