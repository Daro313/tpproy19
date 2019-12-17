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
from flaskps.app.users.models import Rol
from flaskps.app.users.constants import *

administrador = Rol('administrador', ADMIN_PERMISOS)
docente = Rol('docente', DOCENTE_PERMISOS)
preceptor = Rol('preceptor', PRECEPTOR_PERMISOS)

administrador.permisos = ','.join(map(str, ADMIN_PERMISOS)
docente.permisos = ','.join(map(str, DOCENTE_PERMISOS)
preceptor.permisos = ','.join(map(str, PRECEPTOR_PERMISOS)

db.session.add(administrador)
db.session.add(docente)
db.session.add(preceptor)
db.session.commit()
```
>>>>>>> 42609108a9e38cbb309480b4a106c1564d4e1467
