## Índice 📑

- [Consultas N+1](#consultas-n1)
- [Falta de índices en la base de datos](#falta-de-índices-en-la-base-de-datos)
- [Evaluación prematura del QuerySet](#evaluación-prematura-del-queryset)
- [Cargar datos innecesarios (overfetching)](#cargar-datos-innecesarios-overfetching)
- [Falta de select related y prefetch related](#falta-de-select-related-y-prefetch-related)
- [Uso incorrecto de count()](#uso-incorrecto-de-count)
- [No usar transacciones correctamente](#no-usar-transacciones-correctamente)
- [No usar bulk operations](#no-usar-bulk-operations)
- [Uso eficiente de annotate()](#uso-eficiente-de-annotate)
- [No usar django debug toolbar](#no-usar-django-debug-toolbar)
- [No usar django silk para profiling](#no-usar-django-silk-para-profiling)
- [Linkografía](#linkografía)


## Consultas N+1 🐌
Es un cuello de botella de rendimiento común en aplicaciones que interactúan con bases de datos. Ocurre cuando una aplicación ejecuta N consultas adicionales para recuperar datos que podrían haberse obtenido con una sola consulta. Esto da como resultado N+1 consultas totales en lugar de solo 1, lo que genera una degradación significativa del rendimiento, especialmente a medida que crece su conjunto de datos.

Ejemplo:
```python
for post in Post.objects.all():
    print(post.author.name)
```

Esto genera 1 consulta para posts + N consultas para autores

Esto en Django se soluciona agregando el método `select_related`:
```python
posts = Post.objects.select_related("author")

for post in posts:
    print(post.author.name)
```


## Falta de índices en la base de datos 📚
Los `índices` optimizan la recuperación de información en una tabla, permitiendo consultas más rápidas sin necesidad de recorrer todos los registros.

Este es uno de los problemas más comunes en aplicaciones con grandes volúmenes de datos.
```python
User.objects.filter(email="test@gmail.com")
```
Sin índices, ocurre un escaneo completo de la tabla. En producción con millones de filas provoca una degradación severa del rendimiento.

Para agregar un índice en el ORM de Django, debes usar:
```python
class User(models.Model):
    email = models.EmailField(db_index=True)
```


## Evaluación prematura del QuerySet ⚡
Los QuerySets son lazy, pero muchos los evalúan de forma errónea:
```python
qs = User.objects.all()
if len(qs) > 0:
	...
```

Un uso correcto de es verificar su existencia con `exists()`:
```python
if qs.exists():
```
El método `exists()` es útil para búsquedas relacionadas con la existencia de objetos en un QuerySet; devuelve "True" si el QuerySet contiene resultados y "False" si no. Intenta ejecutar la consulta de la forma más sencilla y rápida posible. No es adecuado cuando necesitas acceder a los objetos posteriormente.


## Cargar datos innecesarios (overfetching) 📦
Al realizar una consulta donde necesitas todos los datos de una tabla. Ejecutarías:

```python
users = User.objects.all()
```

Pero ¿Y si solo necesitas el name (además del id)? Deberias solicitar solo a ese dato. Para eso existe `only()`, `values()` o `values_list()` dependiendo del tipo de estructura de datos que quieras retornar:

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
User.objects.values_list("name", flat=True)
```


## Falta de select related y prefetch related 🔗
Al utilizar Django ORM, acceder a objetos relacionados puede causar el problema de consulta N+1, donde se ejecutan múltiples consultas de base de datos innecesarias. Django proporciona `select_related()` y `prefetch_related()` para resolver esto y mejorar el rendimiento.

**select_related()** recupera objetos relacionados en una única consulta SQL mediante JOIN. Más adecuado para relaciones ForeignKey y OneToOneField.

Ejemplo:
```python
Post.objects.select_related("author")
```

En cambio **prefetch_related()** ejecuta consultas de base de datos separadas y combina los resultados en Python. Más adecuado para relaciones ManyToMany, ForeignKey inversas y OneToOne inversas

Ejemplo:
```python
books = Book.objects.prefetch_related('authors')

for book in books:
    print(book.title)
    for author in book.authors.all():
        print(author.name)
```

En casos más complejos, donde necesites usar prefetch_related + filtrado, ordenado, etc. Django proporciona el objeto **Prefetch**, que permite tener un control más preciso sobre cómo se cargan los datos relacionados.

Esto es útil cuando necesitas:

* Filtrar los objetos relacionados
* Ordenarlos
* O asignarlos a un atributo personalizado

Ejemplo:
```python
from django.db.models import Prefetch

books = Book.objects.prefetch_related(
    Prefetch(
        "authors",
        queryset=Author.objects.filter(active=True)
    )
)

for book in books:
    for author in book.authors.all():
        print(author.name)
```

## Uso incorrecto de count() 🔢
El método `count()` devuelve un **número entero** que representa la cantidad de objetos en la base de datos que coinciden con el QuerySet.

Ejemplo:
```python
User.objects.count()
```

Un mal uso de devolver lo mismo que count() es:
```python
len(User.objects.all())
```
`count()` ejecuta `SELECT COUNT(*)` directamente en la base de datos, mientras que `len()` carga todos los objetos en memoria.


## No usar transacciones correctamente 🔒
Django utiliza autocommit por defecto, lo que significa que cada operación `.save()`, `.create()` o `.update()` se ejecuta como una transacción independiente.

Esto tiene dos consecuencias importantes:
* Mayor overhead por múltiples commits
* Riesgo de inconsistencias si ocurre un error a mitad de una operación compleja

Problema común:
```python
for item in items:
    item.processed = True
    item.save()
```

Aquí Django ejecuta: 1 UPDATE = 1 COMMIT por cada iteración. Si tienes 10.000 objetos, tendrás: 10.000 commits, esto produce overhead innecesario y mayor tiempo total de ejecución

La solución con transaction.atomic():

```python
from django.db import transaction

with transaction.atomic():
    for item in items:
        item.processed = True
        item.save()
```

Ahora Django ejecuta: 10.000 UPDATE = 1 solo COMMIT, pero no reduce las queries


## No usar bulk operations 🚀
Este método inserta la lista de objetos proporcionada en la base de datos de manera eficiente y devuelve los objetos creados como una lista, en el mismo orden proporcionado:

```python
users = [
    User(username="user1"),
    User(username="user2"),
]
User.objects.bulk_create(users)
```


## Uso eficiente de annotate() 📊
El método **annotate()** permite agregar información calculada a cada objeto del QuerySet usando agregaciones SQL. Esto evita ejecutar consultas adicionales innecesarias.

Problema común:
```python
posts = Post.objects.all()

for post in posts:
    print(post.title, post.comments.count())
```

Esto genera:

* 1 consulta para los posts
* N consultas adicionales para contar los comentarios (problema N+1)

Solución con annotate():
```python
from django.db.models import Count

posts = Post.objects.annotate(comment_count=Count("comments"))

for post in posts:
    print(post.title, post.comment_count)
```

Esto genera una consulta SQL, ya que el conteo se realiza en la base de datos.

Ventajas:
* Reduce el número de consultas
* Aprovecha la optimización del motor de base de datos
* Mejora significativamente el rendimiento en grandes volúmenes de datos

También puedes usar otras funciones como:
```python
from django.db.models import Count, Sum, Avg, Max, Min

User.objects.annotate(
    post_count=Count("posts"),
    avg_score=Avg("posts__score")
)
```


## No usar django debug toolbar 🔎
`django-debug-toolbar` es una herramienta que permite ver información detallada sobre el rendimiento de tu aplicación en tiempo real.

Entre otras cosas, muestra:
* Número de consultas SQL ejecutadas
* Tiempo de ejecución de cada consulta
* Queries duplicadas
* Tiempo total de respuesta
* Uso de caché

Esto permite detectar problemas como:
* Consultas N+1
* Consultas innecesarias
* Consultas lentas
* Falta de índices


## No usar django silk para profiling 🔬
Optimizar sin medir es uno de los errores más comunes. `django-silk` es una herramienta de profiling que permite analizar el rendimiento real de tu aplicación. A diferencia de django-debug-toolbar, django-silk:

* Guarda historial de requests
* Permite analizar queries en detalle
* Muestra tiempo de ejecución exacto
* Permite profiling de funciones Python


## Linkografía 📖
* https://docs.djangoproject.com/en/6.0/ref/models/querysets/#select-related
* https://www.w3schools.com/sql/sql_create_index.asp
* https://docs.djangoproject.com/en/6.0/ref/models/querysets/#exists
* https://docs.djangoproject.com/en/6.0/ref/models/querysets/#count
* https://docs.djangoproject.com/en/6.0/topics/db/transactions/
* https://docs.djangoproject.com/en/6.0/ref/models/querysets/#bulk-create

