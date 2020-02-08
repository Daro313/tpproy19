# TODO LIST

#### DOCENTES
CRUD-DOCENTE


#### Estudiantes

Agregar api
* tipo de documento
* localidad


#### Ciclo lectivo
* crear modelo ciclo lectivo 
* Crear vista de ciclo lectivo
* template (agregar multiples talleres)


#### Talleres

* crear modelo
	* atributos: (docente, estudiantes, nombre)
* crear vista
* crear template (permiete agregar varios estudiantes y docentes)




<<<<<<< HEAD
### MEJORA

USER verificar is__active:

ALTA STUdiante
  * agregar campo: nombre en tutor


CONFIG 
  * que se reflejen los cambios de los 
=======

# creacion de roles con sus permisos

```console
from flaskps import db
from flaskps.app.users.models import Rol, User
from flaskps.app.users.constants import *
from flaskps.app.configurations.models import Configurations

user = User(
    username='superadmin',
    email='admin@admin.com',
)
user.password = 'admin'
db.session.add(user)

conf = Configurations(
  description='escuela orquesta beriso',
  title='escuela orquesta',
  email='escuela@orquesta.mail.com'
)
db.session.add(conf)

administrador = Rol('administrador', ADMIN_PERMISOS)
docente = Rol('docente', DOCENTE_PERMISOS)
preceptor = Rol('preceptor', PRECEPTOR_PERMISOS)

db.session.add(administrador)
db.session.add(docente)
db.session.add(preceptor)

user.roles.append(administrador)

db.session.commit()
```
>>>>>>> 42609108a9e38cbb309480b4a106c1564d4e1467
