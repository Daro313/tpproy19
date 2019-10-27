# Remember that a model is a representation of a database table in code.

# crear base de datos
mysql -u root
create user 'admin'@'localhost' identified by 'admin';<Paste>
create database grupo8;
grant all privileges on grupo8 .* to 'admin'@'localhost';



## Correr servidor local localhost:5000
```console
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run
```


### crear migraciones
```console
flask db migrate
```

### aplicar migracion
```console
flask db upgrade
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
