# Los problemas invisibles que matan el rendimiento en Django

## Consultas N+1
Es un cuello de botella de rendimiento común en aplicaciones que interactúan con bases de datos. Ocurre cuando una aplicación ejecuta N consultas adicionales para recuperar datos que podrían haberse obtenido con una sola consulta. Esto da como resultado N+1 consultas totales en lugar de solo 1, lo que genera una degradación significativa del rendimiento, especialmente a medida que crece su conjunto de datos.

Ejemplo:
```python
for post in Post.objects.all():
    print(post.author.name)
```

Esto genera 1 consulta para posts + N consultas para autores

Esto en Django se soluciona agregando el metodo "select_related":
```python
Post.objects.select_related("author")
```


## Falta de índices en la base de datos
Los índices optimizan la recuperación de información en una tabla, permitiendo consultas más rápidas sin necesidad de recorrer todos los registros.

Este es probablemente el segundo problema más grave.
```python
User.objects.filter(email="test@gmail.com")
```
Sin índices ocurre un escaneo de toda la tabla. En producción con millones de filas provoca una degradación severa del rendimiento.

Para agregar un índice en el ORM de Django, debes usar:
```python
class User(models.Model):
    email = models.EmailField(db_index=True)
```


## Evaluación prematura del QuerySet
Los QuerySets son lazy, pero muchos los evalúan accidentalmente.
```python
qs = User.objects.all()
if len(qs) > 0:
	...
```
Correcto:
```python
if qs.exists():
```
El metodo 'exists()' es útil para búsquedas relacionadas con la existencia de objetos en un QuerySet; devuelve "True" si el QuerySet contiene resultados y "False" si no. Intenta ejecutar la consulta de la forma más sencilla y rápida posible.


## Cargar datos innecesarios (overfetching)
Al realizar una consulta donde necesitas todos los datos de una tabla. Ejecutarias:

```python
users = User.objects.all()
```

¿Y si solo necesitas el name?

```python
# Retorna una instancia del modelo
User.objects.only("name") 
```
o

```python
# Retorna un diccionario
User.objects.values("name")
```

o

```python
# Listas de tuplas
User.objects.values_list("name")
```

## Falta de select_related / prefetch_related
Relacionado con N+1 pero más amplio.

* select_related realiza un JOIN SQL y solo funciona con ForeignKey y OneToOne.

prefetch_related → segunda query optimizada

Regla simple:
ForeignKey → select_related
ManyToMany → prefetch_related

## Uso incorrecto de count()
```python
len(User.objects.all())
```

```python
User.objects.count()
```

https://docs.djangoproject.com/en/6.0/ref/models/querysets/#only


## No usar transacciones correctamente
Problema común:
```python
for item in items:
    item.save()
```
Al estar dentro de un ciclo for, esto ejecuta una query por cada transacción.

Al usar transacciones, esto agrupa todas las queries en una sola transacción.

Correcto:
```python
from django.db import transaction

with transaction.atomic():
    for item in items:
        item.save()
```

https://docs.djangoproject.com/en/6.0/topics/db/transactions/


## No usar bulk operations
```python
for user in users:
    user.save()
```
```python
User.objects.bulk_create(users)
```


## No usar django-debug-toolbar


## Linkografia
*https://docs.djangoproject.com/en/6.0/ref/models/querysets/#select-related
*https://www.w3schools.com/sql/sql_create_index.asp
*https://docs.djangoproject.com/en/6.0/ref/models/querysets/#exists
* 
